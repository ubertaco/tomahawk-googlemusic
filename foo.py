#!/usr/bin/env python2
import sys, os
# add libdir to pythonpath
cwd = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.join(cwd, "lib"))
import gmapi.api as gmusic

gmconn = gmusic.Api()
