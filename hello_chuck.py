#!/usr/bin/env python3
import requests as re

res = re.get(url='https://api.chucknorris.io/jokes/random')
res = res.json()['value']
print(res)