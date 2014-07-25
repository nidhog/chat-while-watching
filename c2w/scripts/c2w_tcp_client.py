#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import argparse
import subprocess
import os

parser = argparse.ArgumentParser(description='c2w Client (TCP Version)')
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
                        'c2w_tcp_client.py')]
if options.debugFlag:
    cmdLine.append('-e')
    print 'about to call: ', cmdLine
if options.lossPr > 0:
    cmdLine.append('-l ' + str(options.lossPr))
try:
    retcode = subprocess.call(cmdLine)
except KeyboardInterrupt:
    pass  # ignore CTRL-C
