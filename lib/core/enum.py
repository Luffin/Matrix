class PATH:
    ROOT_PATH = ''
    SCRIPT_PATH = ''
    OUTPUT_PATH = ''


class TARGET:
    SINGLE_MODE = 1
    FILE_MODE = 2
    IP_MASK_MODE = 3
    IP_RANGE_MODE = 4
    GOOGLE_MODE = 5
    SHODAN_MODE = 6
    ZOOM_EYE_MODE = 7

    single_target = ''
    file_target = ''
    ip_mask_target = ''

    google = ''
    shodan = ''
    zoom_eye = ''

    handle_mode = 0


class ENGINE:
    pass


class CONF:
    '''User defined variables'''
    # output file name
    OUTPUT_FILENAME = ''
    # script name
    SCRIPT_NAME = ''
