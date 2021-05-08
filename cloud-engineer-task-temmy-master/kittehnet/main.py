import mysql.connector
from mysql.connector import Error
from os import environ

from flask import Flask
app = Flask(__name__)
app.config.from_pyfile('kittehnet.cfg')

if 'LOG_LEVEL' in environ:
    app.logger.setLevel(environ.get('LOG_LEVEL'))
else:
    app.logger.setLevel('CRITICAL')


def check_db():
    print('checking db connections')
    try:
        db = app.config['DB']
        connect = mysql.connector.connect(
                user=db['user'],
                password=db['password'],
                database=db['database'],
                host=db['host'],
                )
        if connect.is_connected():
            return True
    except Error as err:
        app.logger.error('MySQL connection error: %s' + str(err))
        return False


@app.route('/')
def hello():
    return 'Welcome to KittehNet!'


@app.route('/purr')
def purr():
    if check_db():
        return 'miaow'
    else:
        return 'hiss', 503
