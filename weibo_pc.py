import requests
import json
from pyquery import PyQuery as pq
import re
input_cookies = raw_input()
weibo_cookies = requests.cookies.RequestsCookieJar()

weibo_cookies_data = input_cookies.split('; ')
for item in weibo_cookies_data:
    item_cookie = item.split('=')
    weibo_cookies.set(item_cookie[0],item_cookie[1],domain='weibo.com', path='/')

response = requests.get('https://weibo.com/p/aj/v6/mblog/mbloglist?ajwvr=6&domain=100505&rightmod=1&wvr=6&mod=personnumber&is_all=1&pagebar=0&pl_name=Pl_Official_MyProfileFeed__20&id=1005056086787012&script_uri=/hakureiRanun/profile&feed_type=0&page=1&pre_page=1&domain_op=100505&__rnd=1544162929846',cookies=weibo_cookies)
content =  json.loads(response.content)
html = pq(content['data'])
# print html('div[node-type=feed_list_content]').text().encode('GBK','ignore')
# print html('div[action-type=feed_list_page_morelist] ul li:first-child').text().encode('GBK','ignore')
pattern1 = re.compile('[0-9]+')
weibo_data = html('div[tbinfo]')
for i in range(len(weibo_data)):
    # print weibo_data('div[node-type=feed_list_content]').eq(i).text().encode('GBK','ignore')
    # print pattern1.findall(weibo_data('ul.WB_row_line li:first-child a').eq(i).text().encode('GBK','ignore'))
    # print pattern1.findall(weibo_data('ul.WB_row_line li:nth-child(2) a').eq(i).text().encode('GBK','ignore'))
    # print pattern1.findall(weibo_data('ul.WB_row_line li:nth-child(3) a').eq(i).text().encode('GBK','ignore'))
    # print pattern1.findall(weibo_data('ul.WB_row_line li:nth-child(4) a').eq(i).text().encode('GBK','ignore'))
    print len(weibo_data('div[node-type=feed_list_content] a[action-type=feed_list_url]').eq(i).text())
# with open('weibo.html','wb') as file:
#     file.write(content['data'].encode('utf-8','ignore'))