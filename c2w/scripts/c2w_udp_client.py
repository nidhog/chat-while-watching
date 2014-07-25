#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import argparse
import subprocess
import os

parser = argparse.ArgumentParser(description='c2w Client (UDP Version)')
parser.add_argument('-e', '--debug',
                    dest='debugFlag',
                    help='Raise the log level to debug',
                    action="store_true",
                    default=False)

options = parser.parse_args()
c2wPath = '~stockrsm/res302/c2w/main'
cmdLine = [os.path.join(os.path.expanduser(c2wPath),
                        'c2w_udp_client.py')]
if options.debugFlag:
    cmdLine.append('-e')
    print 'about to call: ', cmdLine
try:
    retcode = subprocess.call(cmdLine)
except KeyboardInterrupt:
    pass  # ignore CTRL-C
