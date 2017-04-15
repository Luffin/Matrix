import os

from core.optioninit import initoptions
from core.cmdparse import cmdparser
from core.common import setPath
from core.data import paths

from controller.loader import loadScript, loadTarget


def main():
    paths.ROOT_PATH = os.path.abspath(os.path.join(os.path.dirname(__file__), os.pardir))
    setPath()
    args = cmdparser()
    initoptions(args)
    loadScript()
    loadTarget()
    # print args
