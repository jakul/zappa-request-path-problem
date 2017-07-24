from flask import Flask
from flask import request


the_app = Flask(__name__)


@the_app.route('/info')
def return_info():
    return str({'request.url': request.url})
