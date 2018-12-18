from urllib.parse import  urlencode


import requests


base_url = 'http://weixin.sogou.com/weixin?'
## 添加注释
# 1
def get_html(url):
    try:
        response = request.get(url)
    except:  sdsdsds

def get_index(keyword , page):
    data= {
        'query':keyword,
        'type':2,
        'page':page
    }
    queries = urlencode(data)
    url = base_url + queries


