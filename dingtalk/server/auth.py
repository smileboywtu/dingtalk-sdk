# -*- coding: utf-8 -*-

"""

manage the dingtalk token

"""

import time
import requests
from .servers import urls


def get_new_token(corpid, secret):
    """get new access token from dingtalk server

    @params:
        corpid -- id for micro app
        secret -- secret for micro app
    @return:
        http response
    """
    url = urls.get('token', '')

    if not url:
        raise Exception('token server url not set')

    params = {

    }

    resp = requests.get(
        url,
        params=params
    ).json()

    return resp


def check_token(func):
    """check if the token is invalid

    """
    cache = {}
    def __wrapper__(**kwargs):
        """use cache token or create new"""
        if not cache.get('token', '') or \
            cache.get('expire', 0) + 7200 < time.time():
            resp = get_new_token(**kwargs)
            if resp['errcode'] != 0:
                raise Exception('HttpError: %s', resp['errmsg'])
            cache['token'] = resp['token']
            cache['expire'] = time.time()
        return cache['token']
    return __wrapper__


@check_token
def get_access_token(corpid, secret):
    """get the access token

    """
    pass
