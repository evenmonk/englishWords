#!/usr/bin/env python3

import urllib.request

fp = urllib.request.urlopen("http://localhost:2222/")

encodedContent = fp.read()
decodedContent = encodedContent.decode("utf8")

print(decodedContent)

# Закрываем соединение с сервером.
fp.close()