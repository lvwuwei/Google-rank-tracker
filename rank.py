import sys
import re
import random
from random import randint
import robobrowser
from robobrowser import RoboBrowser
import werkzeug
import datetime
import csv
import pandas as pd
import time

# 添加以下导入语句用于处理代理
import requests

# Terminal arguments to pass when running the script
if len(sys.argv) < 3:
    print("Usage: python rank.py example.com mobile")
    sys.exit(1)

sitename = sys.argv[1]
device = sys.argv[2]


# 读取代理列表
with open('GoodProxy.txt', 'r') as proxy_file:
    proxies = [line.strip() for line in proxy_file]

# 其余代码保持不变

# ...

# 创建 RoboBrowser 实例时，将代理应用于 requests 模块
def create_browser(user_agent, proxy):
    browser = RoboBrowser(
        history=False,
        user_agent=user_agent,
        parser='html.parser'
    )

    # 将代理应用于 requests 模块
    browser.session.proxies = {'http': proxy, 'https': proxy}
    
    return browser

# 在 mobile() 和 desktop() 函数中使用 create_browser() 函数
def mobile(keyword, sitename, device, useragent, proxy):
    browser = create_browser(useragent, proxy)
    
    # 其余 mobile() 函数的代码

def desktop(keyword, sitename, device, useragent, proxy):
    browser = create_browser(useragent, proxy)
    
    # 其余 desktop() 函数的代码
# Keyword file
keywords = pd.read_excel('keywords.xls')
# user agent checker. Here depending on what the user agent was passed in th sys arguments we perform different functions.

# Initialize useragent with a default value
useragent = ''

# 在主循环中选择代理并调用相应的函数
for keyword in keywords['Keywords']:
    print(keyword)
    
    # 随机选择一个代理
    selected_proxy = random.choice(proxies)
    
    if device == 'mobile':
        mobile(keyword, sitename, device, useragent, selected_proxy)
    elif device == 'desktop':
        desktop(keyword, sitename, device, useragent, selected_proxy)
    else:
        print(" X_X You didn't specify a user agent. We will still run the script but your filename will have a weird name")
        mobile(keyword, sitename, device, useragent, selected_proxy)
    
    t = randint(1, 10)
    print('Sleeping time is', t, 'Seconds')
    time.sleep(t)
