import random
from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('fsd.cfg')


@app.route('/')
def hello():
    return 'HI'


@app.route('/health')
def health():
    return 'OK'


@app.route('/sentiment')
def sentiment():
    return random.choice(app.config['CAT_MOOD'])
