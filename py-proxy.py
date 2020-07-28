# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Li JIANG
"""
BEGIN
function:
    proxy server
description:
    proxy server based on python3
    no need for tcp connection support, http connection is enough
    support both http and https
END
"""

from flask import Flask, request, jsonify
from flask_cors import CORS
from flask_apscheduler import APScheduler
import time
import requests
import urllib.parse
import json


class Initializer(Flask):
    """
        Class to initialize the REST API
    """
    def __init__(self, name):
        # super(Initializer, self).__init__(name)  # python2
        super().__init__(name)  # python3
        self.cnt = 0
        self.crawl_cnt = 0


app = Initializer(name=__name__)
# support CORS
CORS(app, resources={r"/*": {"origins": "*"}})


@app.route('/', methods=['GET'])
def index():
    return 'Welcome to the test system!'


def str2dict(data):
    data = data.split('&')
    data1 = {}
    for kv in data:
        k, v = kv.split('=')
        data1[k] = v
    return data1


@app.route('/proxy', methods=['GET'])
def proxy():
    print(request.url)
    url = request.args.get('url', '')
    assert url[0:4] == 'http'
    headers = request.args.get('headers', '')
    data = request.args.get('data', '')
    method = request.args.get('method', 'GET')
    if headers != '':
        headers = eval(headers)
    if data != '':
        data = eval(data)
    headers['User-Agent'] = 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, ' \
                            'like Gecko) Chrome/50.0.2661.102 Safari/537.36'
    if method == 'POST':
        response = requests.post(url, headers=headers, data=data, verify=False)
    else:
        response = requests.get(url, headers=headers, verify=False)
    # print(response.text)
    return response.text, response.status_code


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3128, debug=True)
