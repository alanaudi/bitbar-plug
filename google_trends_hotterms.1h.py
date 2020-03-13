#!/usr/local/bin/python3
# -*- coding: utf-8 -*-
#
# <bitbar.title>Google Trends Hot Terms in Taiwan</bitbar.title>
# <bitbar.version>v1.0</bitbar.version>
# <bitbar.author>alanaudi</bitbar.author>
# <bitbar.author.github>alanaudi</bitbar.author.github>
# <bitbar.desc>Show Current Hot Terms</bitbar.desc>
# <bitbar.image>https://i.imgur.com/MLItE66.png</bitbar.image>
# <bitbar.dependencies>python3</bitbar.dependencies>
# <bitbar.abouturl>https://github.com/alanaudi/bitbar-plug</bitbar.abouturl>
#
# by alanaudi

# Standard import
import re
import json
from datetime import date
# Third-party import
import requests

date = date.today().strftime("%Y%m%d")
res = requests.get(F"https://trends.google.com/trends/api/dailytrends?hl=zh-TW&tz=-480&ed={date}&geo=TW&ns=15")
real_response = re.sub(r"\)\]\}\',\n", "", res.text)
item_list = json.loads(real_response)['default']['trendingSearchesDays'][0]['trendingSearches']
rank_list = ["①", "②", "③", "④", "⑤", "⑥", "⑦", "⑧", "⑨", "⑩", "⑪", "⑫", "⑬", "⑭", "⑮", "⑯", "⑰", "⑱", "⑲", "⑳"]

for index, item in enumerate(item_list):
    print(F"{rank_list[index]} {item['title']['query']}")
