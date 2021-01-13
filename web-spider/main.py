# -*- coding: utf-8 -*-

import requests
import json

r = requests.get('https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5')

print(r.json())
