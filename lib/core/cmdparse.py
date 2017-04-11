import argparse
import sys

from log import logger

OPTIONS_HELP = {
    'Init': {
        'description': 'this is a argparse demo',
        'epilog': 'this is end',
    },
    'Script': {
        '-s': {
            'metavar': 'Scipt Name',
            'dest': 'script_name',
            'help': 'use script',
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
            'help': 'generate target IP from IP/MASK (e.g. 192.168.1.1/24)',
        }
    },
    'Search Engines': {
        '-Gg': {
            'metavar': 'Google',
            'dest': 'google',
            'help': 'search target by using Google.',
        },
        '-Ze': {
            'metavar': 'Zoom Eye',
            'dest': 'zomm_eye',
            'help': 'search target by using Zoom Eye.',
        },
        '-Sd': {
            'metavar': 'Shodan',
            'dest': 'shodan',
            'help': 'search target by using Shodan.',
        }
    },
    'Output': {
        '-o': {
            'metavar': 'Output',
            'dest': 'output',
            'help': 'output the result to given name',
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
    _target = target.add_mutually_exclusive_group(required=True)
    _target.add_argument('-u', metavar=OPTIONS_HELP['Target']['-u']['metavar'],
                         dest=OPTIONS_HELP['Target']['-u']['dest'],
                         help=OPTIONS_HELP['Target']['-u']['help'])
    _target.add_argument('-iF', metavar=OPTIONS_HELP['Target']['-iF']['metavar'],
                         dest=OPTIONS_HELP['Target']['-iF']['dest'],
                         help=OPTIONS_HELP['Target']['-iF']['help'])
    _target.add_argument('-iN', metavar=OPTIONS_HELP['Target']['-iN']['metavar'],
                         dest=OPTIONS_HELP['Target']['-iN']['dest'],
                         help=OPTIONS_HELP['Target']['-iN']['help'])

    script = parser.add_argument_group('Script')
    script.add_argument('-s', metavar=OPTIONS_HELP['Script']['-s']['metavar'],
                        dest=OPTIONS_HELP['Script']['-s']['dest'],
                        help=OPTIONS_HELP['Script']['-s']['help'])
    script.add_argument('--show', action='store_true', help=OPTIONS_HELP['Script']['--show']['help'])

    search = parser.add_argument_group('Search Engines')
    _search = search.add_mutually_exclusive_group()
    _search.add_argument('-Gg', metavar=OPTIONS_HELP['Search Engines']['-Gg']['metavar'],
                         dest=OPTIONS_HELP['Search Engines']['-Gg']['dest'],
                         help=OPTIONS_HELP['Search Engines']['-Gg']['help'])
    _search.add_argument('-Ze', metavar=OPTIONS_HELP['Search Engines']['-Ze']['metavar'],
                         dest=OPTIONS_HELP['Search Engines']['-Ze']['dest'],
                         help=OPTIONS_HELP['Search Engines']['-Ze']['help'])
    _search.add_argument('-Sd', metavar=OPTIONS_HELP['Search Engines']['-Sd']['metavar'],
                         dest=OPTIONS_HELP['Search Engines']['-Sd']['dest'],
                         help=OPTIONS_HELP['Search Engines']['-Sd']['help'])

    output = parser.add_argument_group('Output')
    output.add_argument('-o', metavar=OPTIONS_HELP['Output']['-o']['metavar'],
                        dest=OPTIONS_HELP['Output']['-o']['dest'],
                        help=OPTIONS_HELP['Output']['-o']['help'])

    misc = parser.add_argument_group('Misc')
    misc.add_argument('-v', '--version', action='version', version='test 1.0')
    misc.add_argument('-h', '--help', action='help', help='show this help message and exit')

    args = parser.parse_args()
    logger.info('Parsing options...')
    return args


if __name__ == '__main__':
    print cmdparser()
