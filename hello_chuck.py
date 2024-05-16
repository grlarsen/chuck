#!/usr/bin/env python3
import requests as re
import time

def chuck(i):
    res = re.get(url='https://api.chucknorris.io/jokes/random')
    res = res.json()['value']
    print(i, res)

if __name__=='__main__':
    for i in range(100):
        chuck(i)
        time.sleep(1)