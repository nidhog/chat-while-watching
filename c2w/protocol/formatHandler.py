# -*- coding: utf-8 -*-

import struct
import ctypes
import sys

DATA_LENGTH_L = 16
TYPE_FIELD_L = 4
RT_L = 2
HEADER_L = 6

# Big endian or little endian
HEADER_FORMAT = '!BBBBH'
MAX_USERNAME_L = 30
MAX_MESSAGE_L = 140
MAX_MOVIETITLE_L = 100

# Maximum packet size set to the maximum allowed size for ICMP data: 65507
MAX_PACKET_SIZE = 65507
# timeout value set to 3 seconds
TIMEOUT_VALUE   = 3

"""
The format of a packet is as follows:
0                   1                   2                   3
0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2 3 4 5 6 7 8 9 0 1 2
+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+
|F|A|       |   |               |               |               |
|R|C| Type  | RT|Sequence Number|User Identifier|Destination Id |
|G|K|       |   |               |               |               |
+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+
|       Data Length             |                               |
+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+                               |
|                                                               |
.                                                               .
.                               Data                            .
.                                                               .
|                                                               |
+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+−+

the FRG, ACK, TYPE, RT, Sequence Number, User Identifier, Destination Id
and Data Length fields will often be defined repectively as frg, ack,
type_field, rt, seq_number, u_id, d_id and data_length

Since the Data field depends on the Type of the message, it will be
unpacked depending on the Type field

"""

type_value = {
    'login':0b0000,
    'disconnect':0b1111,
    'message':0b0001,
    'room':0b1000,
    'leave_private_chat':0b0111,
    'movie_list':0b0011,
    'user_list':0b0101,
    'message_fwd':0b1100,
    'private_chat':0b1010,
    'leave_private_chat_fwd':0b1001,
    'ayt':0b0110,
    'error':0b1110
    }

rt_value = {
    'main_room':0b00,
    'movie_room':0b01,
    'private_chat':0b10,
    'not_applicable':0b11
    }


# 
def pack_into_format(frg,ack,type_field,rt,seq_number, u_id, d_id, data_length):
    #
    buff = ctypes.create_string_buffer(HEADER_L+data_length)
    #
    first_byte = 0b00000000
    # in case the rt or type_field are higher than normal
    if( len(bin(rt))-2 > RT_L):
        sys.exit('ERROR :  RT = '+format(rt)+' - * RT (Room Type) field is too big * -')
    first_byte += rt
    if(len(bin(type_field))-2 > TYPE_FIELD_L):
        sys.exit('ERROR :  Type = '+format(type_field)+' - * Type field is too big * -')
    first_byte += type_field << 2
    # frg and ack fields can be either True (1) or False (0)
    if frg:
        first_byte += 0b10000000
    if ack:
        first_byte += 0b01000000

    #
    if(seq_number>255 or u_id >255 or d_id > 255):
        sys.exit('Error :  Sequence Number, User Id or Destination Id field is too big'+
                 '')
    struct.pack_into(HEADER_FORMAT, buff, 0, first_byte, seq_number, u_id, d_id, data_length)
    # data_length is the length of the data in bytes
    # struct.pack_into(format(data_length)+'B',buff, HEADER_L, data)
    
    return buff

def unpack_format(buff):
    
    raw_header = struct.unpack_from(HEADER_FORMAT, buff)
    # the first byte contains the FRG, ACK, Type and RT fields
    frg_ack_type_rt = raw_header [0]
    # get the FRG field
    frg_val =   frg_ack_type_rt & 0b10000000
    frg = (frg_val == 128)
    # get back our lovely ack
    ack_val =   frg_ack_type_rt & 0b01000000
    ack = (ack_val == 64)
    # get type_field
    type_field =frg_ack_type_rt & 0b00111100
    rt =        frg_ack_type_rt & 0b00000011
    type_field = type_field >> 2    
    # get the rest of the bytes, i.e: Sequence Number, User Id, Destination Id, Data Length
    seq_number = raw_header [1]
    u_id = raw_header [2]
    d_id = raw_header [3]
    data_length = raw_header [4]
    return frg, ack, type_field, rt, seq_number, u_id, d_id, data_length

# packing and unpacking the Data field will depend on the Type field
    
def conquer_data_by_type(complete_buffer):
    unpacked_header = unpack_format(complete_buffer)
    frg =           unpacked_header[0]
    ack =           unpacked_header[1]
    type_field =    unpacked_header[2]
    data_length =   unpacked_header[7]
    if(type_field == type_value['login']):
        # In case the type of the message is a login request the data field
        # contains the username
        # The length of the username is determined by the data length
        # and it should'nt be higher than the MAX_USERNAME_L value
        offset = HEADER_L
        data = struct.unpack_from(format(data_length)+'s', complete_buffer,offset)
        username=data[0]
        return unpacked_header, username
    elif(type_field == type_value['disconnect']):
        pass
        # I don't think we really need this one
    elif(type_field == type_value['message']):
        pass
        #
    elif(type_field == type_value['room']):
        if(ack):
            pass
            # unpacking stuff goes here
    elif(type_field == type_value['leave_private_chat']):
        pass
        # I don't think we really need this one
    elif(type_field == type_value['movie_list']):
        pass
        # Too lazy to do this one
    elif(type_field == type_value['user_list']):
        pass
        #
    elif(type_field == type_value['message_fwd']):
        pass
        #
    elif(type_field == type_value['private_chat']):
        pass
        #
    elif(type_field == type_value['leave_private_chat_fwd']):
        pass
        #
    elif(type_field == type_value['ayt']):
        pass
        #
    elif(type_field == type_value['error']):
        pass
        #
        
    
            
    

