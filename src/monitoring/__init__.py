from http import HTTPStatus

__version__ = '0.1.0'


def health_check():
    """
    Show we're alive and kicking

    :return:
    """
    return None, HTTPStatus.NO_CONTENT