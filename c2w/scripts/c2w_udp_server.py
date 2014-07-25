#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import argparse
import subprocess
import os

parser = argparse.ArgumentParser(description='c2w Server (UDP Version)')
parser.add_argument('-p', '--port', dest='server_port', type=int,
                    help='The port number to be used for listening.')
parser.add_argument('-n', '--no-video',
                        dest='noVideoFlag',
                        help='Do not use the video part.',
                        action="store_true", default=False)
parser.add_argument('-s', '--stream-video',
                    dest='streamVideoFlag',
                    help='Enable sending the video stream to other ' +
                    'computers (if this option is not given, only ' +
                    'on the local machine will be able to receive the ' +
                    'video stream).',
                    action="store_true", default=False)
parser.add_argument('-e', '--debug',
                    dest='debugFlag',
                    help='Raise the log level to debug',
                    action="store_true",
                    default=False)
parser.add_argument('-l', '--loss-pr', dest='lossPr',
                    help='The packet loss probability for outgoing ' +
                    'packets.', type=float, default=0)

options = parser.parse_args()
c2wPath = '~stockrsm/res302/c2w/main'
cmdLine = [os.path.join(os.path.expanduser(c2wPath),
                        'c2w_udp_server.py')]
if options.server_port is not None:
    cmdLine.append('-p ' + str(options.server_port))
if options.lossPr > 0:
    cmdLine.append('-l ' + str(options.lossPr))
if options.streamVideoFlag:
    cmdLine.append('-s')
if options.noVideoFlag:
    cmdLine.append('-n')
if options.debugFlag:
    cmdLine.append('-e')
    print 'about to call: ', cmdLine
try:
    retcode = subprocess.call(cmdLine)
except KeyboardInterrupt:
    pass  # ignore CTRL-C
