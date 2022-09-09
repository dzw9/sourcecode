from urllib import response
import requests
import re
url='https://music.163.com/#/playlist?id=7050074027'
response=requests.get(url)
#print(response.text)
html_data=response.text
info_list=re.findall('<li><a href="/song\?id=(.*?)">(.*?)</a></li>',html_data) #匹配？加\
#print(info_list)
for info in info_list:
    music_url='https://music.163.com/song/media/outer/url?id='+str(info[0])
    music_data=requests.get(music_url).content
    open(f'音乐/'+info[1]+'.flac',mode='wb').write(music_data)
    print(info[1],'保存完成')   # media-搜索-ctrl+F查找-点击{}
print('全部保存完成')