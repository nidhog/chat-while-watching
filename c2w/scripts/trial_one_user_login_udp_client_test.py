#!/usr/bin/env python2.7
# -*- coding: utf-8 -*-

import argparse
import subprocess
import os
from c2w.scripts._trial_generic import get_spec

spec = get_spec(['g6', 'g14'])

trial_class = 'c2w.test.protocol.udp_client_test.c2wUdpChatClientTestCase'
cmdLine = ['trial',
           trial_class + '.test_one_user_login_udp_client_test']
try:
    retcode = subprocess.call(cmdLine)
except KeyboardInterrupt:
    pass  # ignore CTRL-C
