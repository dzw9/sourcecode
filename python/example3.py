import requests
from pprint import pprint
import json
url=f'https://kyfw.12306.cn/otn/leftTicket/query?leftTicketDTO.train_date=2022-08-18&leftTicketDTO.from_station=HZH&leftTicketDTO.to_station=UMW&purpose_codes=ADULT'
headers={
    'Host': 'kyfw.12306.cn',
    'Cookie': '_uab_collina=165978923031249592631788; tk=n1pJzJ7sJ3XRmY41A4jb6P5t4_XANwWa_rdQIoaZ5ok1uBbS36d1d0; JSESSIONID=A67E372D7F0974C9273B017B3C0BFEF2; BIGipServerotn=1190134282.64545.0000; BIGipServerpool_passport=165937674.50215.0000; RAIL_EXPIRATION=1660074361915; RAIL_DEVICEID=FraPayr7trYZOGe3IoV86KOLJBrR5hd_1iEnCpSxulsbA2XhMHac5uS4XJm4wDki1vDu-spRXH5G_Ah7bQDu3722-ObMvVspZws04pG4WUIk2I6Aprn5hygi3wJfjDJQO0n5V4qALEYmzap8GPVW6Fko1twFG5sq; highContrastMode=defaltMode; guidesStatus=off; cursorStatus=off; route=c5c62a339e7744272a54643b3be5bf64; _jc_save_fromStation=%u676D%u5DDE%2CHZH; _jc_save_toDate=2022-08-06; _jc_save_wfdc_flag=dc; current_captcha_type=Z; _jc_save_toStation=%u516D%u76D8%u6C34%2CUMW; _jc_save_fromDate=2022-08-18',
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.0.0 Safari/537.36'
}
response=requests.get(url=url,headers=headers)
json_data=response.json()
#pprint(json_data)
train=json_data['data']['result']
print(train)
print(str(train).split("|"))
trainstr=str(train).split("|")
num=0
for str in trainstr:
    print(str,'|',num)
    num+=1