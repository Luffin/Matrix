import argparse
import sys

# from log import logger
from config import Version

OPTIONS_HELP = {
    'Init': {
        'description': 'this is a argparse demo',
        'epilog': 'this is end',
    },
    'Script': {
        '-s': {
            'metavar': 'Scipt Name',
            'dest': 'script_name',
            'help': 'use script. (e.g. [-s st02-045] or [-s script/struts/st02-045.py])',
        },
        '--show': {
            'help': 'show all scripts on ./script by listing script names',
        },
    },
    'Target': {
        '-u': {
            'metavar': 'Target',
            'dest': 'target',
            'help': 'single target to test',
        },
        '-iF': {
            'metavar': 'Filename',
            'dest': 'filename',
            'help': 'load targets from input file',
        },
        '-iN': {
            'metavar': 'IP/MASK',
            'dest': 'ip',
            'help': 'generate target IP from IP/MASK (e.g. 192.168.1.0/24)',
        },
        '-iR': {
            'metavar': 'IP Range',
            'dest': 'ip_range',
            'help': 'generate target IP from IP range (e.g. 192.168.1.25-155)'
        },
        '-Gg': {
            'metavar': 'Google',
            'dest': 'google',
            'help': 'search targets by using Google.',
        },
        '-Ze': {
            'metavar': 'Zoom Eye',
            'dest': 'zoom_eye',
            'help': 'search targets by using Zoom Eye.',
        },
        '-Sd': {
            'metavar': 'Shodan',
            'dest': 'shodan',
            'help': 'search targets by using Shodan.',
        }
    },
    'Output': {
        '-o': {
            'metavar': 'Output',
            'dest': 'output',
            'help': 'output the result to given name. Default will be set like ROOT_PATH/output/20170101_12_30.txt',
        }
    },
    # 'Misc': {
    #     '-v': {
    #         'dest': 'version',
    #         'help': 'show version',
    #     }
    # },
}


class Myparser(argparse.ArgumentParser):
    # http://stackoverflow.com/questions/4042452/display-help-message-with-python-argparse-when-script-is-called-without-any-argu
    def error(self, message):
        self.print_help()
        sys.stderr.write('error: %s\n' % message)
        sys.exit(2)


def cmdparser():
    parser = Myparser(
        description='this is a argparse demo.',
        epilog='this is end',
        add_help=False,
    )

    target = parser.add_argument_group('Target')
    _target = target.add_mutually_exclusive_group()
    _target.add_argument('-u', metavar=OPTIONS_HELP['Target']['-u']['metavar'],
                         dest=OPTIONS_HELP['Target']['-u']['dest'],
                         help=OPTIONS_HELP['Target']['-u']['help'])
    _target.add_argument('-iF', metavar=OPTIONS_HELP['Target']['-iF']['metavar'],
                         dest=OPTIONS_HELP['Target']['-iF']['dest'],
                         help=OPTIONS_HELP['Target']['-iF']['help'])
    _target.add_argument('-iN', metavar=OPTIONS_HELP['Target']['-iN']['metavar'],
                         dest=OPTIONS_HELP['Target']['-iN']['dest'],
                         help=OPTIONS_HELP['Target']['-iN']['help'])
    _target.add_argument('-iR', metavar=OPTIONS_HELP['Target']['-iR']['metavar'],
                         dest=OPTIONS_HELP['Target']['-iR']['dest'],
                         help=OPTIONS_HELP['Target']['-iR']['help'])
    _target.add_argument('-Gg', metavar=OPTIONS_HELP['Target']['-Gg']['metavar'],
                         dest=OPTIONS_HELP['Target']['-Gg']['dest'],
                         help=OPTIONS_HELP['Target']['-Gg']['help'])
    _target.add_argument('-Ze', metavar=OPTIONS_HELP['Target']['-Ze']['metavar'],
                         dest=OPTIONS_HELP['Target']['-Ze']['dest'],
                         help=OPTIONS_HELP['Target']['-Ze']['help'])
    _target.add_argument('-Sd', metavar=OPTIONS_HELP['Target']['-Sd']['metavar'],
                         dest=OPTIONS_HELP['Target']['-Sd']['dest'],
                         help=OPTIONS_HELP['Target']['-Sd']['help'])

    script = parser.add_argument_group('Script')
    script.add_argument('-s', metavar=OPTIONS_HELP['Script']['-s']['metavar'],
                        dest=OPTIONS_HELP['Script']['-s']['dest'],
                        help=OPTIONS_HELP['Script']['-s']['help'])
    script.add_argument('--show', action='store_true', help=OPTIONS_HELP['Script']['--show']['help'])

    # search = parser.add_argument_group('Search Engines')
    # _search = search.add_mutually_exclusive_group()

    output = parser.add_argument_group('Output')
    output.add_argument('-o', metavar=OPTIONS_HELP['Output']['-o']['metavar'],
                        dest=OPTIONS_HELP['Output']['-o']['dest'],
                        help=OPTIONS_HELP['Output']['-o']['help'])

    misc = parser.add_argument_group('Misc')
    misc.add_argument('-v', '--version', action='version', version=Version)
    misc.add_argument('-h', '--help', action='help', help='show this help message and exit')

    args = parser.parse_args()
    # logger.info('Parsing options...')
    if len(sys.argv) < 2:
        sys.exit(parser.print_help())
    return args


if __name__ == '__main__':
    print cmdparser()
