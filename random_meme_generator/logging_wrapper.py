import os
import logging


log_level: dict = {
    'ERROR': logging.ERROR,
    'INFO': logging.INFO,
    'DEBUG': logging.DEBUG,
    'WARNING': logging.WARNING
}


class LoggerWrapper:
    """LoggerWrapper"""

    def __init__(self, format, dt_format, name):
        self.format = format
        self.dt_format = dt_format
        self.name = name
        self.formatter = logging.Formatter(fmt=self.format, datefmt=self.dt_format)

    @staticmethod
    def validate_config_dict(config_dict: dict):
        """validate_config_dict

        Args:
            config_dict (dict): Logger Config Dict
        """
        if config_dict.get('log_level') is None:
            raise ValueError("Config Level not Defined")
        
        if config_dict['log_level'].upper() not in log_level.keys():
            raise ValueError("Invalid Log Level")
        
        if (config_dict.get('file_path') is not None) and (not isinstance(config_dict.get('file_path'), str)):
            raise ValueError("File Patg must be of type string")

    def create_logger(
        self, 
        config_dict: dict
    ):
        """create_logger
            Create logger instance
        Args:
            config_dict (dict): Config Dict for Logger Wrapper. It includes - 
                                1. Log Level(log_level): Can either be 'ERROR, INFO, or DEBUG'
                                2. File Path(file_path): File Path for log file in disk. If File path is empty file handler
                                                            will not be initialized
        """
        LoggerWrapper.validate_config_dict(config_dict=config_dict)
        
        _logger = logging.getLogger(self.name)

        c_handler = logging.StreamHandler()
        c_handler.setFormatter(self.formatter)
        _logger.addHandler(c_handler)

        if (config_dict.get('file_path') is not None) and os.path.exists(config_dict.get('file_path')):
            f_handler = logging.FileHandler(config_dict['file_path'])
            f_handler.setFormatter(self.formatter)
            _logger.addHandler(f_handler)
        
        _logger.setLevel(log_level[config_dict['log_level'].upper()])

        return _logger
