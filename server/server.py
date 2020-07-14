#!/usr/bin/env python3

import http.server
import socketserver

handler = http.server.SimpleHTTPRequestHandler

with socketserver.TCPServer(("", 2222), handler) as httpd:
    httpd.serve_forever()