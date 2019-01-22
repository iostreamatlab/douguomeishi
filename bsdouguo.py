# -*- coding: UTF-8 -*-
"""
 获取豆果美食
"""

import requests
from bs4 import BeautifulSoup
from datetime import datetime, timedelta


# 获得指定开始排行
def get_url(root_url,start):
    return root_url+str(start)

def get_review(page_url):
    cooks_list=[]
    response=requests.get(page_url)
    soup=BeautifulSoup(response.text,"lxml")
    soup=soup.find('ul','cook-list')
    for tag_li in soup.find_all('li','clearfix'):
        dict={}
        dict['cook-name']=tag_li.find('div','cook-info').find('a').string
        dict['major']=tag_li.find('p','major').string
        cooks_list.append(dict)
    return cooks_list

if __name__ == "__main__":
    root_url="https://www.douguo.com/ingredients/腐竹/"
    start=20
    while(start<140):
        cooks_list=get_review(get_url(root_url,start))
        for cook_dict in cooks_list:
            print('cook name:'+cook_dict.get('cook-name'))
            print('majpr:'+cook_dict.get('major'))
            print('------------------------------------------------------')
        start+=20

