# -*- coding: utf-8 -*-

import requests
import json
from pyecharts import options as opts
from pyecharts.charts import Map
from pyecharts.faker import Faker

r = requests.get(
    'https://view.inews.qq.com/g2/getOnsInfo?name=disease_h5').json()

c = (Map()
     .add(series_name="确诊人数", data_pair=list(map(lambda province: [province['name'], province['total']['nowConfirm']], json.loads(
         r['data'])['areaTree'][0]['children'])), maptype="china")
     .set_global_opts(
    title_opts=opts.TitleOpts(title="中国疫情图"),
    visualmap_opts=opts.VisualMapOpts(max_=3600, is_piecewise=True, pieces=[
        {"max": 5000, "min": 1001, "label": ">1000", "color": "#8A0808"},
        {"max": 1000, "min": 500, "label": "500-1000", "color": "#B40404"},
        {"max": 499, "min": 100, "label": "100-499", "color": "#DF0101"},
        {"max": 99, "min": 10, "label": "10-99", "color": "#F78181"},
        {"max": 9, "min": 1, "label": "1-9", "color": "#F5A9A9"},
    ]),
)
    .render("web-spider/web-spider-map.html"))
