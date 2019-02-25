# -*- coding: utf-8 -*-

import requests
from django.conf import settings
import datetime, pytz
from json.decoder import JSONDecodeError


def get_url(mileage_from=None, mileage_to=None):
    if mileage_from and mileage_to:
        ml = 'ml={}%3A{}&'.format(mileage_from, mileage_to)
    else:
        ml = ''
    return settings.TARGET_RESOURCE.format(ml)


def make_api_request(request_method='get', params=None,
                     data=None, **kwargs):
    requests_method = getattr(requests, request_method)
    api_url = get_url(5000, 125000)
    if kwargs:
        for value in kwargs.values():
            api_url = api_url.format(value)
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_10_1) AppleWebKit/537.36 (KHTML, like Gecko) '
                             'Chrome/39.0.2171.95 Safari/537.36',
               'accept-language': 'ru,en-US;q=0.9,en;q=0.8',
               'cache-control': 'no-cache'}
    return requests_method(api_url, params=params, headers=headers, data=data)
    # if return_json and response.status_code in (200, 201):
    #     try:
    #         return response.json()
    #     except JSONDecodeError:
    #         return response.text
