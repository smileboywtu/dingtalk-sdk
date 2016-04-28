# -*- coding: utf-8 -*-

"""

manager the media file

version: python 2.7.11

"""

import requests
from .servers import urls
from .auth import get_access_token


def upload_media(name, data, type, mime):
    """upload media to dingtalk

    @params:
        name -- file name
        data -- binary data
        type -- file type
        mime -- file mime type
    @return:
        http -- return http information
    """
    url = urls.get('media_upload', '')
    access_token = get_access_token()

    if not url:
        return None

    params = {
        'access_token': access_token,
        'type': type
    }

    files = [
        ('media', (name, data, mime))
    ]

    resp = requests.post(
        url,
        params=params,
        files=files
    ).json()

    return resp
