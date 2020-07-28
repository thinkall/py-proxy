# !/usr/bin/python3
# -*- coding:utf-8 -*-
# Author: Li JIANG
# Modified from "http://www.lyyyuna.com/2016/01/16/http-proxy-get1/"
"""
BEGIN
function:
    proxy server
description:
    proxy server based on python3
    need tcp connection support
END
"""

from http.server import BaseHTTPRequestHandler, HTTPServer
import socket
import urllib


class MyHandler(BaseHTTPRequestHandler):
    def do_GET(self):
        uri = self.path
        # print uri
        print(uri)

        proto, rest = urllib.parse.splittype(uri)
        host, rest = urllib.parse.splithost(rest)
        # print host
        path = rest
        host, port = urllib.parse.splitnport(host)
        if port < 0:
            port = 80
        # print host
        host_ip = socket.gethostbyname(host)
        # print port

        del self.headers['Proxy-Connection']
        self.headers['Connection'] = 'close'

        send_data = 'GET ' + path + ' ' + self.protocol_version + '\r\n'
        head = ''
        for key, val in self.headers.items():
            head = head + "%s: %s\r\n" % (key, val)
        send_data = send_data + head + '\r\n'
        # print send_data
        so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        so.connect((host_ip, port))
        so.sendall(send_data.encode())

        # 因为采用非长连接，所以会关闭连接， recv 会退出
        data = ''.encode()
        while True:
            tmp = so.recv(4096)
            if not tmp:
                break
            data = data + tmp

        # socprint data
        so.close()

        self.wfile.write(data)
    # do_CONNECT = do_GET


def main():
    try:
        server = HTTPServer(('', 3128), MyHandler)
        print('Welcome to the machine...')
        server.serve_forever()
    except KeyboardInterrupt:
        print('^C received, shutting down server')
        server.socket.close()


if __name__ == '__main__':
    main()
