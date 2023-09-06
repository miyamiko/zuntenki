import requests
import json
import urllib.parse
import time
todouhuken=['北海道',16000,
'青森県',20000,
'岩手県',30000,
'宮城県',40000,
'秋田県',50000,
'山形県',60000,
'福島県',70000,
'茨城県',80000,
'栃木県',90000,
'群馬県',100000,
'埼玉県',110000,
'千葉県',120000,
'東京都',130000,
'神奈川県',140000,
'山梨県',190000,
'長野県',200000,
'岐阜県',210000,
'静岡県',220000,
'愛知県',230000,
'三重県',240000,
'新潟県',150000,
'富山県',160000,
'石川県',170000,
'福井県',180000,
'滋賀県',250000,
'京都府',260000,
'大阪府',270000,
'兵庫県',280000,
'奈良県',290000,
'和歌山県',300000,
'鳥取県',310000,
'島根県',320000,
'岡山県',330000,
'広島県',340000,
'徳島県',360000,
'香川県',370000,
'愛媛県',380000,
'高知県',390000,
'山口県',350000,
'福岡県',400000,
'佐賀県',410000,
'長崎県',420000,
'熊本県',430000,
'大分県',440000,
'宮崎県',450000,
'鹿児島県',460100,
'沖縄',471000]
no_todouhuken=['北海道',16000,
'青森',20000,
'岩手',30000,
'宮城',40000,
'秋田',50000,
'山形',60000,
'福島',70000,
'茨城',80000,
'栃木',90000,
'群馬',100000,
'埼玉',110000,
'千葉',120000,
'東京',130000,
'神奈川',140000,
'山梨',190000,
'長野',200000,
'岐阜',210000,
'静岡',220000,
'愛知',230000,
'三重',240000,
'新潟',150000,
'富山',160000,
'石川',170000,
'福井',180000,
'滋賀',250000,
'京都',260000,
'大阪',270000,
'兵庫',280000,
'奈良',290000,
'和歌山',300000,
'鳥取',310000,
'島根',320000,
'岡山',330000,
'広島',340000,
'徳島',360000,
'香川',370000,
'愛媛',380000,
'高知',390000,
'山口',350000,
'福岡',400000,
'佐賀',410000,
'長崎',420000,
'熊本',430000,
'大分',440000,
'宮崎',450000,
'鹿児島',460100,
'沖縄',471000]

def tenki(search_word):
    area=todouhuken[::2]
    area2=no_todouhuken[::2]
    acode=todouhuken[1::2]+no_todouhuken[1::2]
    index=777#見つからないとき
    # search_word = '高知県の天気は'
    for i, word in enumerate(area+area2):
        if any(s in word for s in search_word) and not any(s in word for s in ['県','府','都']):
            if word in search_word:
                print(word)
                index = i
                break
    if index!=777:
        print(acode[index])
    else:
        if '京都' in search_word:#京都は上の'都'ではじかれてしまうので対策
            word='京都'
            print(word)
            index=25
            print(acode[index])
        else:
            print('見つかりませんでした')
            tenki='この地域は対応していません'
    if index!=777:
        url = "https://www.jma.go.jp/bosai/forecast/data/overview_forecast/"
        areaCode=acode[index]
        # encoded_text = urllib.parse.quote(text.encode("utf-8"))
        full_url = url + str(areaCode) + ".json"
        try:
            response = requests.get(full_url)
            resjson=json.loads(response.text)
            rtenki=resjson['text'].split('\n\n　')[1]
            tenki=rtenki[:22]
        except:
            tenki='この地域は対応していません'
        print(tenki)
    return tenki

