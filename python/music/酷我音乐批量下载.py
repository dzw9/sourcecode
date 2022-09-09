import requests
import re
import os
key = input('请输入你要搜索的歌曲或者歌手名:')
os.mkdir(f'音乐/kuwomusic/{key}') #创建目录
url1=f'https://www.kuwo.cn/api/www/search/searchMusicBykeyWord?key={key}&pn=1&rn=30&httpsStatus=1&reqId=e83a5051-0cf5-11ed-bc32-15ed49d9574c'
headers={
    'Cookie': 'Hm_lvt_cdb524f42f0ce19b169a8071123a4797=1658844692; _ga=GA1.2.2074337943.1658844692; _gid=GA1.2.415006749.1658844692; Hm_lpvt_cdb524f42f0ce19b169a8071123a4797=1658848452; kw_token=STFXRNKGUKL',
    'csrf': 'STFXRNKGUKL',
    'Host': 'www.kuwo.cn',
    'Referer': 'https://www.kuwo.cn/search/list?key=%E5%91%A8%E6%9D%B0%E4%BC%A6',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
response=requests.get(url=url1,headers=headers)
print(response)
json_data=response.json()  #字典类型数据  text字符串文本  content二进制数据
data_list=json_data['data']['list']
for data in data_list:
    rid=data['rid']
    artist=data['artist']
    name=data['name']
    print(rid,name,artist)
    info_url=f'https://www.kuwo.cn/api/v1/www/music/playUrl?mid={rid}&type=convert_url3&br=320kmp3'
    music_url=requests.get(url=info_url).json()['data']['url']
    music_data=requests.get(music_url).content
    with open(f'音乐/kuwomusic/{key}/{name}-{artist}.mp3',mode='wb') as f:
        f.write(music_data)
        print('保存完成')