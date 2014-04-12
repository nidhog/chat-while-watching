chat-while-watching
===================

The "c2w" application allows users to chat while watching a movie


-------------
The c2w protocol is based on the
client−server model. The goal of this protocol is to realise the
application "c2w" which allows users to chat while watching a movie.
Note that this is just a proposition for the c2w protocol
specification.


Introduction
------------
The c2w protocol is an application layer protocol that is intended
for the c2w application. The goal of this application is to enable
clients to watch videos present in the server and to chat in the same
time.
In the c2w application, a client starts by logging in with his
username and the port number of the server to address a request of
connection to the server. If this request is successful, the client
gets in the main−room where he can either chat with other clients or
choose to join a movie room so he can Chat While Watching. In the
main room, the client sees a list of all the users with their
availability and a ist of all the movies available. In a movie room,
a client has access to a list of all the users in the same room.
Wherever he is, the client can select another client to start a
private chat with. And of course, the client can disconnect by
leaving the main room. Clients can use either UDP or TCP to exchange
messages with the server.
This document defines the protocol used by the clients to talk with
the server and vice−versa. It includes the requirements needed to
implement the c2w protocol. The c2w protocol enables working with an
unreliable transportation protocol such as UDP.
In our protocol, we have a unique format for all the packets, but
since these packets are of different types, there are differences in
the data field.
While no security considerations were taken into account, the
provided specifications allow improving the c2w protocol for
security.
