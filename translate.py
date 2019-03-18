#!/usr/bin/env python
# -*- coding:utf-8 -*- 
# Author: Sizepeng Zhao

import requests
import random
import hashlib
import json


class trans():
    def __init__(self):
        self.appid ='20190307000274854'
        self.key = 'WWBPRjInI96ehr8d4qCw'
        self.url = 'http://api.fanyi.baidu.com/api/trans/vip/translate?'
        self.from_language = 'zh'
        self.to_language = 'zh'

    def change_fl(self, fl):
        self.from_language = fl
        #print(self.from_language, 'set')

    def change_tl(self, tl):
        self.to_language = tl
        #print(self.to_language, 'set')

    def translate(self, q, salt=random.randint(32768, 65536)):
        #q为待翻译文本
        sign = self.appid + q + str(salt) + self.key
        sign = sign.encode('utf-8')
        sign_new = hashlib.md5(sign).hexdigest()
        new_url = self.url + 'q=' + q + '&from=' + self.from_language + '&to=' + self.to_language + '&appid=' + \
            self.appid + '&salt=' + str(salt) + '&sign=' + sign_new
        res = requests.get(new_url)
        json_data = json.loads(res.text)
        translate_result = json_data["trans_result"][0]["dst"]
        #print(translate_result)
        return translate_result


