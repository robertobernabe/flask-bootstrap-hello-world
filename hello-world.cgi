#!/usr/bin/python
import sys
import site
if site.getusersitepackages() not in sys.path:
    print sys.path.append(site.getusersitepackages())

from wsgiref.handlers import CGIHandler
from hello_world import app
import os

environ = {
    'SERVER_NAME': '',
    'SERVER_PORT': '',
}
os.environ['SERVER_NAME'] = ''
os.environ['SERVER_PORT'] = ''


CGIHandler().run(app)
