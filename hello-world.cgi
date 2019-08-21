#!/usr/bin/python
from wsgiref.handlers import CGIHandler
from hello_world import app

CGIHandler().run(app)
