#!/usr/bin/python3
from http.cookiejar import CookieJar
import datetime
cookie_jar = CookieJar()
from urllib.request import *
opener = build_opener(HTTPCookieProcessor(cookie_jar))
opener.open('http://www.github.com')
print(len(cookie_jar))
print(cookie_jar)
cookies = list(cookie_jar)
print(cookies[0].name)
print(cookies[0].expires)
print(datetime.datetime.fromtimestamp(cookies[0].expires))