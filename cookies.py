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
for val in cookies:
    print(val)
    
