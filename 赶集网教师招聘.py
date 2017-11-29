#爬取赶集网教师招聘信息
# -*- coding:utf-8 -*-
import urllib
import urllib2
import re

user_agent = 'Mozilla/5.0 (Windows NT 6.1) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.113 Safari/537.36'
headers = { 'User-Agent' : user_agent }


url = 'http://wx.ganji.com/zpjiaoshi/'

try:
    request = urllib2.Request(url, headers=headers)
    response = urllib2.urlopen(request)

    html = response.read().decode('utf-8')

except urllib2.URLError, e:
    if hasattr(e,"code"):
        print e.code
    if hasattr(e,"reason"):
        print e.reason

all_pattern = re.compile('<dt>.*?<a href=".*?">(.*?)</a>.*?<div class="new-dl-company"><a href=".*?".*?>(.*?)</a>.*?<div class="new-dl-salary">(.*?)</div>.*?<div class="new-dl-tags">.*?<i>(.*?)</i>',re.S)
all_list = re.findall(all_pattern, html)
for item in all_list:
    print "position:" + item[0]
    print "location:" + item[1]
    print "salary:" + item[2].strip()
    print "treatment:" + item[3]
    print "-----------------------------------"

#输入回车加载下一页，输入Q退出
    input = raw_input()
    if input == "":
        print "nextPage:"
        continue
    elif input =="Q":
        break
