import logging

def log():
    logger = logging.getLogger('mylog')
    logger.setLevel(logging.INFO)
    return logger