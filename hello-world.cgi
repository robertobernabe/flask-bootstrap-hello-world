#!/usr/bin/python
try:
    import sys
    import site

    if site.getusersitepackages() not in sys.path:
        sys.path.append(site.getusersitepackages())

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

except Exception as e:
    print "Content-type: text/plain\n\n"
    print e.message