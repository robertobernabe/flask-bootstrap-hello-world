from flask import Flask

app = Flask(__name__)

from hello_world import routes

