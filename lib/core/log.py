import logging
import sys

from colorlog import ColoredFormatter


def set_logger(fmt='%(log_color)s[%(asctime)s] [%(levelname)s] %(message)s'):
    logging.addLevelName(10, 'SUCCESS')
    logging.addLevelName(9, 'INFO')
    logging.addLevelName(8, 'WARNING')
    logging.addLevelName(7, 'ERROR')

    formatter = ColoredFormatter(
        fmt,
        datefmt='%H:%M:%S',
        log_colors={
            logging.getLevelName(10): 'green',
            logging.getLevelName(9): 'cyan',
            logging.getLevelName(8): 'yellow',
            logging.getLevelName(7): 'red',
        }
    )

    logger = logging.getLogger('test')
    handler = logging.StreamHandler(sys.stdout)
    handler.setFormatter(formatter)
    logger.addHandler(handler)
    logger.setLevel(logging.getLevelName('ERROR'))

    return logger


class MyLogger():
    """Easy to output color log"""
    def __init__(self):
        self.logger = set_logger()

    def success(self, msg):
        self.logger.log(10, msg)

    def info(self, msg):
        self.logger.log(9, msg)

    def warning(self, msg):
        self.logger.log(8, msg)

    def error(self, msg):
        self.logger.log(7, msg)


logger = MyLogger()

if __name__ == '__main__':
    logger = MyLogger()

    logger.success('success')
    logger.info('information')
    logger.warning('warning')
    logger.error('error')
