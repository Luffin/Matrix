import imp
import sys

from lib.core.data import conf, targets
from lib.core.config import Requied_function_name
from lib.core.common import transPathtoImpType
from lib.core.log import logger


def loadScript():
    path, script_name, suffix = transPathtoImpType(conf.SCRIPT_NAME)

    try:
        file, pathname, description = imp.find_module(script_name, [path])
        script = imp.load_module('*', file, pathname, description)
        if not hasattr(script, Requied_function_name):
            msg = "Can not find the required function: '%s()' in the given script. " % Requied_function_name
            if suffix != '.py':
                msg += "Maybe the given script '%s%s' is not a Python file." % (script_name, suffix)
            msg += 'Please check and reset.'
            sys.exit(logger.error(msg))
    except ImportError as e:
        sys.exit(logger.error(str(e)))


def loadTarget():

    def _single_mode(target):
        print target

    def _file_mode(target):
        with open(target, 'rb') as f:
            targets_list = f.readlines()

        targets_list = [_.strip() for _ in targets_list]
        for i in targets_list:
            print i

    def _ip_mask_mode(target):
        print target

    def _ip_range_mode(target):
        start = int(target.strip().split('-')[0].split('.')[-1])
        stop = int(target.strip().split('-')[-1]) + 1
        body = target.strip().split('-')[0].split('.')[:3]
        ip_list = []

        for num in xrange(start, stop):
            ip_list.append('.'.join(body) + '.%s' % str(num))

        for ip in ip_list:
            print ip

    def _google_mode(target):
        pass

    def _shodan_mode(target):
        pass

    def _zoom_eye_mode(target):
        pass

    if targets.handle_mode == targets.SINGLE_MODE:
        _single_mode(targets.single_target)
    elif targets.handle_mode == targets.FILE_MODE:
        _file_mode(targets.file_target)
    elif targets.handle_mode == targets.IP_MASK_MODE:
        _ip_mask_mode(targets.ip_mask_target)
    elif targets.handle_mode == targets.IP_RANGE_MODE:
        _ip_range_mode(targets.ip_range_target)
    elif targets.handle_mode == targets.GOOGLE_MODE:
        _google_mode(targets.google)
    elif targets.handle_mode == targets.SHODAN_MODE:
        _shodan_mode(targets.shodan)
    elif targets.handle_mode == targets.ZOOM_EYE_MODE:
        _zoom_eye_mode(targets.zoom_eye)
