#!/usr/bin/python
try:
    import sys
    import os
    import site

    if site.getusersitepackages() not in sys.path:
        sys.path.append(site.getusersitepackages())
    homeDir = os.path.expanduser("~")
    sys.path.append(homeDir + "/flask-bootstrap-hello-world")

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

except:
    print "Content-type: text/plain\n\n"
    print "Unexpected error:", sys.exc_info()[0]
