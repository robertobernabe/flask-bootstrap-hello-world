#!/usr/bin/python
import os
print "Content-type: text/plain\n\n"
print "Hello Python"
for env in os.environ:
    print env + "=" + os.environ[env]