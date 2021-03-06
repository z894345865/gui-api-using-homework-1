#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Sizepeng Zhao

import requests
import random
import hashlib
import json


class trans():
    def __init__(self):
        #API接口所需的参数
        self.appid ='20190307000274854'
        self.key = 'WWBPRjInI96ehr8d4qCw'
        self.url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'
        self.from_language = 'auto'
        self.to_language = 'zh'

    #改变待翻译文本的语言
    def change_fl(self, fl):
        self.from_language = fl

    #改变翻译出的文本的语言
    def change_tl(self, tl):
        self.to_language = tl

    def translate(self, q, salt=random.randint(32768, 65536)):
        #q为待翻译文本
        #拼接字符串appid+q+salt+key
        sign = self.appid + q + str(salt) + self.key
        #计算md5加密前，需将字符串更改为utf-8编码
        sign = sign.encode('utf-8')
        #md5加密得到签名sign
        sign_new = hashlib.md5(sign).hexdigest()
        new_url = self.url + 'q=' + q + '&from=' + self.from_language + '&to=' + self.to_language + '&appid=' + \
            self.appid + '&salt=' + str(salt) + '&sign=' + sign_new
        res = requests.get(new_url)
        json_data = json.loads(res.text)
        translate_result = json_data["trans_result"][0]["dst"]
        return translate_result


