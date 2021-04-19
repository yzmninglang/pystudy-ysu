import re
import requests
import time
import json
def getweather():
    head={'User-Agent': "Mozilla/5.0 (Linux; U; Android 10; en; Mi MIX 2S Build/QQ3A.200805.001) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/57.0.2987.108 UCBrowser/12.10.0.1163 UCTurbo/1.10.3.900 Mobile Safari/537.36"  }

    url="http://mip.chinaz.com/"

    text=requests.get(url=url,headers=head).content.decode("utf-8")
    location=re.findall('中国(.*?)[电移联][信动通]',text,re.DOTALL)[0]

    provence="河北省、山西省、辽宁省、吉林省、黑龙江省、江苏省、浙江省、安徽省、福建省、江西省、山东省、台湾省、河南省、湖北省、湖南省、广东省、海南省、四川省、贵州省、云南省、陕西省、甘肃省、青海省"
    provences=provence.replace("省","").split('、')
    for i in provences:
        if i in location:
            locations=location.strip(i)
        # print(locations)
    b=str(time.time()).split(".")
    timestamp=b[0]+b[1][0:3]
    print(timestamp)
    print(locations)
    if len(locations)>3:
        locations=locations[0:3]
    else:
        locations=locations
    # locations="秦皇岛"
    url="http://toy1.weather.com.cn/search?cityname={}&callback=success_jsonpCallback&_={}".format(locations,int(timestamp)-2000000)
    text=requests.get(url=url,headers=head).content.decode("utf-8")
    # print()
    print(text)
    text=re.findall('"ref":"([0-9]*?)~.*?~'.format(locations),text,re.DOTALL)[0]
    print(text)
    getweatherurl="http://d1.weather.com.cn/dingzhi/{}.html".format(text)
    content=requests.get(url=getweatherurl,headers=head).content.decode("utf-8")
    content=re.findall("=({.*?}.*?})",content,re.DOTALL)[0]
    weather=json.loads(content)
    return weather["weatherinfo"]
print(getweather())
# getweather()

