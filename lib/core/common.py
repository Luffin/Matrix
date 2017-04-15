import os
import sys

from data import paths
from log import logger


def setPath():
    paths.SCRIPT_PATH = os.path.join(paths.ROOT_PATH, 'script')
    paths.OUTPUT_PATH = os.path.join(paths.ROOT_PATH, 'output')


def checkFile(path):
    path = path.strip()
    if not os.path.exists(path):
        msg = "The given file: '%s' does not exist. Please check and reset." % path
        sys.exit(logger.error(msg))
    if not os.path.isfile(path):
        msg = "The given file: '%s' is not a file. Please check and reset." % path
        sys.exit(logger.error(msg))
    try:
        with open(path, 'rb'):
            pass
    except Exception:
        msg = 'Unable to read file: %s' % path
        sys.exit(logger.error(msg))


def transPathtoImpType(path):
    path, file = os.path.split(path)
    filename, suffix = os.path.splitext(file)
    return path, filename, suffix
