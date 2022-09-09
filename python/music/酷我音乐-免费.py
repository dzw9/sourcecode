import requests
import re
url1='https://www.kuwo.cn/api/v1/www/music/playUrl?mid=203818448' #付费音乐加&type=convert_url3&br=320kmp3
response1=requests.get(url1)
url2='https://www.kuwo.cn/play_detail/203818448'
response2=requests.get(url2).text
title=re.findall('<title>(.*?)_Zyboy忠宇',response2)[0]
print(title)
json_data=response1.json()  #字典类型数据  text字符串文本  content二进制数据
music_url=json_data['data']['url']
print(music_url)
music=requests.get(url=music_url).content
with open('music/'+title+'.mp3',mode='wb') as f:
    f.write(music)
    print('保存完成')