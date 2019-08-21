From STRATO Hosting Basic and up python is enabled on the server. [Hosting plans](https://www.strato.de/hosting/#features)

You can connect to the sever via SSH through `ssh <your domain>@ssh.strato.de`. The Password is you 'Masterpasswort'.

Since you have neither sudo access nor apt-get or something similar, you have to improvise.

First download and install PIP in the user dir and then install Django:

```
wget https://bootstrap.pypa.io/get-pip.py
python get-pip.py --user
~/.local/bin/pip install django --user
```

Next you migh have to add the location of the 'sites-packages' folder to the python path. It should be `~/.local/lib/python2.7/site-packages` but it might be a different python version on your folder. You need to put this dir into the python path variable. You have to options for that:
* set pythonpath variable through `set PYTHONPATH=${PYTHONPATH}:"~/.local/lib/python2.7/site-packages"`
* add this to the start of your script:
```
import sys,site
if site.getusersitepackages() not in sys.path:
	print sys.path.append(site.getusersitepackages())
```

To execute 'django-admin' use this command: `~/.local/bin/django-admin`.

To start a new project use `~/.local/bin/django-admin startproject <project name>`.


/home/strato/www/fs/www.fschaeffeler.de/htdocs/
