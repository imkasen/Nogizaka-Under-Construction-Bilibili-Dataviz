# 获得视频的 BV 号

import requests
import json


id_tyyh = "2301165"  # 天翼羽魂 id
search_keyword1 = "乃木坂工事中 坂道之诗"
search_keyword2 = "乃木坂工事中 不够热"

# 请求 URL
url = "https://api.bilibili.com/x/space/arc/search"

# 请求头
headers = {
    "User-Agent": "Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_0) AppleWebKit/537.36 (KHTML, like Gecko) \
     Chrome/70.0.3538.110 Safari/537.36"
}

params = {
    "mid": id_tyyh,
    "ps": "30",
    "tid": "0",
    "pn": "1",
    "keyword": search_keyword1,
    "order": "pubdate",
    "jsonp": "jsonp"
}

proxies = {
     "http": "153.36.134.176:9999"
}

response = requests.get(
    url=url,
    headers=headers,
    params=params,
    proxies=proxies
)

results = response.json()
total_page_num = int(results["data"]["page"]["count"] / results["data"]["page"]["ps"] + 1)
print(total_page_num)
