# -*- coding:UTF-8 -*-
import http.client
import hashlib  # md5替换
import urllib
import random
import requests
import json

def httptranslate(from_ext, to_ext, txt):  # 接收三个字符串参数
    appid = '20190524000301423'  # 你的appid
    secretKey = 'hVArCh3lUlj7kwzrERCF'  # 你的密钥
    myurl = '/api/trans/vip/translate'
    q = txt
    fromLang = from_ext
    toLang = to_ext
    salt = random.randint(32768, 65536)
    sign = appid + q + str(salt) + secretKey
    # 对签名进行加密
    m2 = hashlib.md5(sign.encode(encoding='UTF-8')).hexdigest()
    myurl = myurl + '?appid=' + appid + '&q=' + urllib.parse.quote(
        q) + '&from=' + fromLang + '&to=' + toLang + '&salt=' + str(salt) + '&sign=' + m2

    try:
        re = requests.get("https://fanyi-api.baidu.com" + myurl)
        dic = json.loads(re.text)
        result=dic["trans_result"][0]["dst"]
        return result

    except Exception as e:
        return "NULL"


def tochinese(txt):
    chinese=httptranslate("en","zh",txt)
    return chinese

def toenglish(txt):
    eng=httptranslate("zh","en",txt)
    return eng
