import os


class Config:
    LOGGER_FORMAT = "%(asctime)s-%(filename)s-%(funcName)s-%(lineno)s-%(levelname)s-%(message)s"
    DATE_FORMAT = '%d-%b-%y %H:%M:%S'

    LOGGER_CONFIG_DICT = {
        'log_level': 'info',
        'file_path': os.environ.get('file_path', 'app.log')
    }
