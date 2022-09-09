from cgitb import text
from itertools import tee
import requests
import re
url='https://ssr1.scrape.center/'
for page in range(1,11):
    index_url=f'{url}page/{page}'
    #print(index_url)
    response=requests.get(index_url)
    for i in range(10*(page-1)+1,10*(page-1)+11):
        infourl=f'{url}detail/{i}'
        inforesponse=requests.get(infourl)
        print(inforesponse)
        title=re.findall('<h2 data-v-63864230="" class="m-b-sm">(.*?)</h2>',inforesponse.text)[0]
        print(title)
