import urlparse


def is_legal_url(url):
    schemes = ('http', 'https')
    parse_result = urlparse.urlparse(url)

    if parse_result.scheme not in schemes:
        return False
    return True


# def ():
    # pass
