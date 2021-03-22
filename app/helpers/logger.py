# simple logger for debugging
import logging
import sys
import time
from logging.handlers import TimedRotatingFileHandler

FORMATTER = logging.Formatter(
    '%(asctime)s - %(levelname)7s - %(filename)30s:%(lineno)4d - %(message)s',
    '%Y-%m-%dT%H:%M:%SZ'
)

def set_console_handler():
    console_handler = logging.StreamHandler(sys.stdout)
    console_handler.setFormatter(FORMATTER)
    return console_handler

def set_file_handler():
    file_handler = TimedRotatingFileHandler('ml-engine-api.log', when="midnight")
    file_handler.setFormatter(FORMATTER)
    return file_handler

def log():
    logging.Formatter.converter = time.gmtime
    logger = logging.getLogger('ml-engine-api')
    logger,setLevel(logging.DEBUG)
    logger.addHandler(set_console_handler())
    logger.addHandler(set_file_handler())
    logger.propagate = False
    return logger

logger = log()
    

    
    
