# coding=utf-8

import requests
from bs4 import BeautifulSoup
import traceback

try:
    url = 'http://openaccess.thecvf.com/CVPR2017.py'  # If you need CVPR2018 papers,just change 2017 to 2018 here,
    prefix = 'http://openaccess.thecvf.com/'
    html = requests.get(url).content
    soup = BeautifulSoup(html, "lxml")
    a_list = soup.find_all('a')
    for everya in a_list:
        text = everya.text.strip()
        if text == "pdf":
            href = everya.get("href").strip()
            try:
                content = requests.get(prefix+href).content
                last = href.rfind('/')
                name = href[last+1:]
                with open("G:/CVPR2017/%s" % name, 'wb') as f:  # You may change to "path/to/your/folder"
                    f.write(content)
                print("Finish downloading %s" % name)
            except:
                print(traceback.format_exc(), 'when downloading %s' % href)
except:
    print(traceback.format_exc())
    pass