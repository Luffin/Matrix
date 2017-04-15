import os
import glob
import sys
import time

from data import paths, conf, targets
from log import logger
from common import checkFile


def initoptions(args):
    update(args)
    showScript(args)
    setTarget(args)
    setScript(args)
    setOutput(args)
    print args


def update(args):
    pass


def showScript(args):
    if args.show:
        script_name_list = [_.split(os.sep)[-1] for _ in glob.glob(os.path.join(paths.SCRIPT_PATH, '*.py')) if '__init__' not in _]
        total = len(script_name_list)
        msg = 'The number of script: %d\n' % total
        for script_name in script_name_list:
            msg += '\t%s\n' % script_name.rstrip('.py')
        sys.exit(msg)


def setTarget(args):
    single_target = args.target
    filename_target = args.filename
    ip_mask_target = args.ip
    ip_range_target = args.ip_range
    google = args.google
    shodan = args.shodan
    zoom_eye = args.zoom_eye

    def _single_target(target):
        targets.single_target = target
        targets.handle_mode = targets.SINGLE_MODE

    def _file_target(target):
        checkFile(filename_target)
        targets.file_target = target
        targets.handle_mode = targets.FILE_MODE

    def _ip_mask_target(target):
        targets.ip_mask_target = target
        targets.handle_mode = targets.IP_MASK_MODE

    def _ip_range_target(target):
        targets.ip_range_target = target
        targets.handle_mode = targets.IP_RANGE_MODE

    def _google_target(target):
        targets.google = target
        targets.handle_mode = targets.GOOGLE_MODE

    def _shodan_target(target):
        targets.shodan = target
        targets.handle_mode = targets.SHODAN_MODE

    def _zoom_eye_target(target):
        targets.zoom_eye = target
        targets.handle_mode = targets.ZOOM_EYE_MODE

    if single_target:
        _single_target(single_target)
    elif filename_target:
        _file_target(filename_target)
    elif ip_mask_target:
        _ip_mask_target(ip_mask_target)
    elif ip_range_target:
        _ip_range_target(ip_range_target)
    elif google:
        _google_target(google)
    elif shodan:
        _shodan_target(shodan)
    elif zoom_eye:
        _zoom_eye_target(zoom_eye)


def setScript(args):
    script_name = args.script_name

    if not script_name:
        msg = '-s argument is required. Set -s argument to use script. (e.g. [-s st02-045] or [-s script/struts/st02-045.py])'
        sys.exit(logger.error(msg))

    if script_name.endswith('.py'):
        if paths.SCRIPT_PATH in script_name:
            script_path = os.path.join(paths.SCRIPT_PATH, script_name)
            checkFile(script_path)
            conf.SCRIPT_NAME = script_path
        else:
            checkFile(script_name)
            conf.SCRIPT_NAME = script_name
    else:
        if not os.path.splitext(script_name)[-1]:
            script_path = os.path.join(paths.SCRIPT_PATH, script_name + '.py')
            checkFile(script_path)
            conf.SCRIPT_NAME = script_path
        else:
            checkFile(script_name)
            conf.SCRIPT_NAME = script_name

    msg = 'Use script: %s' % conf.SCRIPT_NAME  # os.path.split(conf.SCRIPT_NAME)[-1].rstrip('.py')
    logger.success(msg)


def setOutput(args):
    conf.OUTPUT_FILENAME = args.output if args.output else os.path.join(paths.OUTPUT_PATH, time.strftime("%Y%m%d_%H_%M", time.localtime()) + '.txt')
