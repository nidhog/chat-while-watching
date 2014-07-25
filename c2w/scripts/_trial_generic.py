import os
import sys


def get_spec(authorized_specs):
    try:
        ppath = os.environ['SPEC']
        if not ppath in authorized_specs:
            print "Sorry but tests are only available for: ", authorized_specs
            sys.exit(1)
        return ppath
    except KeyError:
        print "Fatal Error: the SPEC environment variable MUST \
            be defined with either g14 or g6"
        sys.exit()
