from flask import Flask
from logging_wrapper import LoggerWrapper
from config import Config

app = Flask(__name__)
app.config.from_object(Config)

app.logger = LoggerWrapper(
    format=app.config['LOGGER_FORMAT'], 
    dt_format=app.config['DATE_FORMAT'], 
    name=__name__
).create_logger(config_dict=app.config['LOGGER_CONFIG_DICT'])

app.app_context().push()

from memes_gen import memes_gen
app.register_blueprint(memes_gen)

@app.route('/', methods=["GET"])
def index():
    return {
        'usage': '/memes?count=<number of memes>'
    }

@app.route('/health_check', methods=["GET"])
def health_check():
    app.logger.info('Service is up & running')
    resp = {
        "message": "Service is up & running"
    }
    return resp