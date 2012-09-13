#!/usr/bin/env python

import sys
import base64
from shaext import shaext
    
keylen = int("14")
orig_msg = "count=10&lat=37.351&user_id=1&long=-119.827&waffle=eggo"
orig_sig = "5030dc36bf7aefef3267bd71b051df10f6ccd1d1"
add_msg = "&waffle=liege"

ext = shaext(orig_msg, keylen, orig_sig)
ext.add(add_msg)

(new_msg, new_sig)= ext.final()
        
print "new msg: " + repr(new_msg)
print "base64: " + base64.b64encode(new_msg)
print "new sig: " + new_sig
