import requests

from requests.exceptions import ConnectionError, HTTPError
from flask import Flask, render_template
from os import environ

app = Flask(__name__)
app.config.from_pyfile('pawserver.cfg')

if 'LOG_LEVEL' in environ:
    app.logger.setLevel(environ.get('LOG_LEVEL'))


def check_animal_networks():
    platform_status = {}
    for platform, config in app.config['PLATFORMS'].items():
        try:
            r = requests.get(
                config['url'] + config['status_check'], timeout=0.01)
            r.raise_for_status()
            platform_status[platform] = r.text
            app.logger.debug(
                    'Platform repsonse: %s - %s', platform, str(r.text))
        except ConnectionError as err:
            app.logger.error(
                    'Connection Error for: %s - %s', platform, str(err))
            platform_status[platform] = 'connection error'
        except HTTPError as err:
            app.logger.error('HTTP Error for: %s - %s', platform, str(err))
            platform_status[platform] = 'http error'
    return platform_status


@app.route('/')
def hello():
    status = check_animal_networks()
    return render_template('index.html', platform_status=status)


@app.route('/checkz')
def checkz():
    return check_animal_networks()
