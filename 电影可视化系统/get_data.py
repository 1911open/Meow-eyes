# -*- coding: utf-8 -*-
# Time    : 2018/12/10 10:36
# Author  : 辛放
# Email   : 1374520110@qq.com
# ID      : SZ160110115
# File    : register.py
# Software: PyCharm

import re
import time
import pymysql
import requests
from bs4 import BeautifulSoup
from fontTools.ttLib import TTFont
from hashlib import sha1
import random

head = """
Accept:text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8
Accept-Encoding:gzip, deflate, br
Accept-Language:zh-CN,zh;q=0.8
Cache-Control:max-age=0
Connection:keep-alive
Host:maoyan.com
Upgrade-Insecure-Requests:1
Content-Type:application/x-www-form-urlencoded; charset=UTF-8
User-Agent:Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/59.0.3071.86 Safari/537.36
"""

def load(name,pwd):
    db = pymysql.connect(host='localhost',port=3306,user='root',passwd='201314xIn',db='maoyan',charset='utf8')
# 接收用户输入
    res = name
    # 对密码加密
    # m = sha1()
    # s = m.update(pwd.encode("utf-8"))
    # print(s)
    pwd2=sha1(pwd.encode('utf-8')).hexdigest()
    # 根据用户名查询密码

    sql = 'select password from userinfo where name=%s'
    cursor = db.cursor()
    cursor.execute(sql,res)
    psw = cursor.fetchall()
    db.commit()
    cursor.close()
    db.close()
    if psw == ():
        return 0
    elif psw[0][0] == pwd2:
        return 1
    else:
        return 2

def str_to_dict(header):
    """
    构造请求头,可以在不同函数里构造不同的请求头
    """
    header_dict = {}
    header = header.split('\n')
    for h in header:
        h = h.strip()
        if h:
            k, v = h.split(':', 1)
            header_dict[k] = v.strip()
    return header_dict


def get_url():
    """
    获取电影详情页链接
    """
    for k in range(4):
        for i in range(0, 300, 30):
            time.sleep(random.random()*3)
            url = 'https://maoyan.com/films?showType=3&sortId=3&yearId=' + str(k+10) + '&offset=' + str(i)
            host = 'Referer:https://maoyan.com/films?showType=3&yearId=10&sortId=3'
            header = head + host
            headers = str_to_dict(header)
            try:
                response = requests.get(url=url, headers=headers)
            except:
                continue
            html = response.text
            soup = BeautifulSoup(html, 'html.parser')
            data_1 = soup.find_all('div', {'class': 'channel-detail movie-item-title'})
            data_2 = soup.find_all('div', {'class': 'channel-detail channel-detail-orange'})
            num = 0
            for item in data_1:
                num += 1
                time.sleep(random.random()*3)
                url_1 = item.select('a')[0]['href']
                if data_2[num-1].get_text() != '暂无评分':
                    print('********************',num,'start********************')
                    url = 'https://maoyan.com' + url_1
                    print(url)
                    for message in get_message(url):
                        print(message)
                        to_mysql(message)
                    print('********************',num,'end********************\n')
                else:
                    continue


def get_message(url):
    """
    获取电影详情页里的信息
    """
    time.sleep(random.random()*3+5)
    data = {}
    host = """refer: https://maoyan.com/films
    """
    header = head + host
    headers = str_to_dict(header)
    try:
        response = requests.get(url=url, headers=headers)
    except:
        return data
    u = response.text
    # 破解猫眼文字反爬
    (maoyan_num_list, utf8last) = get_numbers(u)
    # 获取电影信息
    soup = BeautifulSoup(u, "html.parser")
    mw = soup.find_all('span', {'class': 'stonefont'})
    score = soup.find_all('span', {'class': 'score-num'})
    unit = soup.find_all('span', {'class': 'unit'})
    ell = soup.find_all('li', {'class': 'ellipsis'})
    name = soup.find_all('h3', {'class': 'name'})
    people = soup.find_all('a', {'class': 'name'})
    # 返回电影信息
    if name:
        data["name"] = name[0].get_text()
    data["time"] = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime(time.time()))
    if ell:
        type = ell[0].get_text().split(',')
        if len(type)>0:
            data["type1"] = type[0]
        if len(type)>1:
            data["type2"] = type[1]
        if len(type)>2:
            data["type3"] = type[2]
        if len(type)>3:
            data["type4"] = type[3]
        if len(type)>4:
            data["type5"] = type[4]
        if len(ell[1].get_text().split('/'))>0:
            data["country"] = ell[1].get_text().split('/')[0].replace('\n','').replace(' ','')
        if len(ell[1].get_text().split('/'))>1:
            data["length"] = ell[1].get_text().split('/')[1].replace('\n','').replace(' ','')
        try:
            if ell[2].get_text()[:10]:
                string = ell[2].get_text()[:10]
            if string.split('-')[0]:
                data['year'] = int(string.split('-')[0])
            if string.split('-')[0]:
                data['month'] = int(string.split('-')[1])
            if string.split('-')[2]:
                data['day'] = int(string.split('-')[2])
        except:
            pass
    if people:
        data['director'] = people[0].get_text().replace('\n', '').replace(' ','')
        if len(people) > 2:
            data['actor1'] = people[1].get_text().replace('\n', '').replace(' ','')
        if len(people) > 3:
            data['actor2'] = people[2].get_text().replace('\n', '').replace(' ','')
        if len(people) > 4:
            data['actor3'] = people[3].get_text().replace('\n', '').replace(' ','')
        if len(people) > 5:
            data['actor4'] = people[4].get_text().replace('\n', '').replace(' ','')
    # 因为会出现没有票房的电影,所以这里需要判断
    if unit:
        if len(unit) > 0 and len(score) > 0:
            bom = ['分', score[0].get_text().replace('.', '').replace('万', ''), unit[0].get_text()]
        for i in range(len(mw)):
            moviewish = mw[i].get_text().encode('utf-8')
            moviewish = str(moviewish, encoding='utf-8')
            # 通过比对获取反爬文字信息
            for j in range(len(utf8last)):
                moviewish = moviewish.replace(utf8last[j], maoyan_num_list[j])
            if i == 0:
                data["score"] = moviewish + '分'
            elif i == 1:
                if '万' in moviewish:
                    data["people"] = int(float(moviewish.replace('万', '')) * 10000)
                else:
                    data["people"] = int(float(moviewish))
            else:
                if '万' == bom[i]:
                    data["box_office"] = int(float(moviewish) * 10000)
                else:
                    data["box_office"] = int(float(moviewish) * 100000000)
    else:
        for i in range(len(mw)):
            moviewish = mw[i].get_text().encode('utf-8')
            moviewish = str(moviewish, encoding='utf-8')
            for j in range(len(utf8last)):
                moviewish = moviewish.replace(utf8last[j], maoyan_num_list[j])
            if i == 0:
                data["score"] = moviewish + '分'
            else:
                if '万' in moviewish:
                    data["people"] = int(float(moviewish.replace('万', '')) * 10000)
                else:
                    data["people"] = int(float(moviewish))
    yield data


def to_mysql(data):
    """
    信息写入mysql
    """
    table = 'films'
    keys = ', '.join(data.keys())
    values = ', '.join(['%s'] * len(data))
    db = pymysql.connect(host='localhost', user='root', password='201314xIn', port=3306, db='maoyan')
    cursor = db.cursor()
    sql = 'INSERT INTO {table}({keys}) VALUES ({values})'.format(table=table, keys=keys, values=values)
    try:
        if cursor.execute(sql, tuple(data.values())):
            print("Successful")
            db.commit()
    except:
        print('Failed')
        db.rollback()
    db.close()


def get_numbers(u):
    """
    对猫眼的文字反爬进行破解
    """
    cmp = re.compile("url\('(//.*.woff)'\) format\('woff'\)")
    rst = cmp.findall(u)
    if  rst:
        ttf = requests.get("https:" + rst[0], stream=True)
    with open("get_numbers/maoyan.woff", "wb") as pdf:
        for chunk in ttf.iter_content(chunk_size=1024):
            if chunk:
                pdf.write(chunk)
    base_font = TTFont('get_numbers/base.woff')
    maoyanFont = TTFont('get_numbers/maoyan.woff')
    maoyan_unicode_list = maoyanFont['cmap'].tables[0].ttFont.getGlyphOrder()
    maoyan_num_list = []
    base_num_list = ['.', '3', '0', '8', '9', '4', '1', '5', '2', '7', '6']
    base_unicode_list = ['x', 'uniE273', 'uniECD9', 'uniE5C1', 'uniE0D4', 'uniE426', 'uniF3C3', 'uniF275', 'uniE8BC', 'uniE793', 'uniE712']
    for i in range(1, 12):
        maoyan_glyph = maoyanFont['glyf'][maoyan_unicode_list[i]]
        for j in range(11):
            base_glyph = base_font['glyf'][base_unicode_list[j]]
            if maoyan_glyph == base_glyph:
                maoyan_num_list.append(base_num_list[j])
                break
    maoyan_unicode_list[1] = 'uni0078'
    utf8List = [eval(r"'\u" + uni[3:] + "'").encode("utf-8") for uni in maoyan_unicode_list[1:]]
    utf8last = []
    for i in range(len(utf8List)):
        utf8List[i] = str(utf8List[i], encoding='utf-8')
        utf8last.append(utf8List[i])
    return (maoyan_num_list, utf8last)


def main():
    get_url()


if __name__ == '__main__':
    main()
