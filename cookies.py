#!/usr/bin/python3
from http.cookiejar import CookieJar
cook = CookieJar()
from urllib.request import *
opener = build_opener(HTTPCookieProcessor(cook))
opener.open('http://www.github.com')
print(len(cook))