#!/usr/bin/python
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
