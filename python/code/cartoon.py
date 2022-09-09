import requests
import re
from tqdm import tqdm

headers = {
    'cookie': 'QC005=a43c7ad82fc48176cc85b5c4129ecbd7; QC006=171d92e872d2967b3c05d24c69d2869f; QP0030=1; T00404=8138835866884491d9d8a998fac8af01; QC173=0; P00004=.1645087284.d5626a1ae5; QC160=%7B%22type%22%3A2%7D; QC170=1; Hm_lvt_53b7374a63c37483e5dd97d78d9bb36e=1645085663,1645254492,1645443011,1646143938; QC021=%5B%7B%22key%22%3A%22%E5%A5%A5%E7%89%B9%E6%9B%BC%22%7D%2C%7B%22key%22%3A%22%E4%B8%80%E9%97%AA%E4%B8%80%E9%97%AA%E4%BA%AE%E6%98%9F%E6%98%9F%22%7D%2C%7B%22key%22%3A%22%E7%88%B1%E6%83%85%E5%85%AC%E5%AF%93%22%7D%2C%7B%22key%22%3A%22%E6%B5%B7%E8%B4%BC%E7%8E%8B%22%7D%2C%7B%22key%22%3A%22%E6%82%AC%E5%B4%96%E4%B9%8B%E4%B8%8A%22%7D%2C%7B%22key%22%3A%22%E7%86%8A%E5%87%BA%E6%B2%A1%22%7D%5D; QP007=0; QY_PUSHMSG_ID=a43c7ad82fc48176cc85b5c4129ecbd7; TQC030=1; QP008=0; T00700=EgcI9L-tIRABEgcI58DtIRAB; QC008=1640937178.1653121537.1653141412.8; nu=0; P00001=99oQ98bPstG6fxeEyhAD6m3EpddiZo1PZ6x0pNiFQzcWbm3JDuaNga85yqDIzHm27kt9M4f; P00007=99oQ98bPstG6fxeEyhAD6m3EpddiZo1PZ6x0pNiFQzcWbm3JDuaNga85yqDIzHm27kt9M4f; P00003=1637120337; P00002=%7B%22uid%22%3A1637120337%2C%22pru%22%3A1637120337%2C%22user_name%22%3A%22199****7649%22%2C%22nickname%22%3A%22%5Cu5bcc%5Cu58eb%5Cu5c71%5Cu4e0b2010duo%22%2C%22pnickname%22%3A%22%5Cu5bcc%5Cu58eb%5Cu5c71%5Cu4e0b2010duo%22%2C%22type%22%3A11%2C%22email%22%3A%22%22%7D; P00010=1637120337; P01010=1653148800; P00PRU=1637120337; QC175=%7B%22upd%22%3Atrue%2C%22ct%22%3A1653141454429%7D; QC163=1; QP0013=16; QP0037=0; QP0034=%7B%22v%22%3A1%2C%22dm%22%3A%7B%22wv%22%3A1%7D%2C%22m%22%3A%7B%22wm-vp9%22%3A1%2C%22wm-av1%22%3A1%7D%7D; QP006=%7B%22code%22%3A%22A10002%22%2C%22locale%22%3A%22cn_s%22%2C%22name%22%3A%22%E6%A3%80%E6%B5%8B%E5%88%B0%E8%B4%A6%E5%8F%B7%E8%A2%AB%E5%A4%9A%E4%BA%BA%E5%85%B1%E4%BA%AB%EF%BC%8C%E4%BC%9A%E5%91%98%E6%9D%83%E7%9B%8A%E5%B7%B2%E6%9A%82%E5%81%9C%EF%BC%8C%E8%AF%B7%E4%BF%AE%E6%94%B9%E5%AF%86%E7%A0%81%22%2C%22button_name%22%3A%22%E4%BF%AE%E6%94%B9%E5%AF%86%E7%A0%81%22%2C%22button_url%22%3A%22https%3A%2F%2Fhelp.iqiyi.com%2Fm%2F5HNoR1oC%2FquestionInfo%2F1305.html%22%7D; QYABEX={"mergedAbtest":"3075_A,1550_B,4270_A,1707_B","PCW_1_new_player":{"value":"0","abtest":"3075_A"},"pcw_home_hover":{"value":"1","abtest":"1550_B"},"PCW_1_player_vipbtn":{"value":"0","abtest":"4270_A"},"PCW-Home-List":{"value":"1","abtest":"1707_B"}}; QC179=%7B%22vipTypes%22%3A%2216%22%2C%22userIcon%22%3A%22https%3A//img7.iqiyipic.com/passport/20200101/90/90/passport_1637120337_157780421165796_130_130.jpg%22%2C%22iconPendant%22%3A%22%22%2C%22uid%22%3A%221637120337%22%7D; c11637120337=1653141825942; c241637120337=1653141825942; __dfp=a1e1a229d2d3f749d5b2a6c2427248ea7cac684687c9eca03d7c70318a8a8a9967@1654238959090@1652942960090; PCAU=0; QP0027=7; QP0033=1; QY00001=1637120337; QC159=%7B%22color%22%3A%22FFFFFF%22%2C%22channelConfig%22%3A1%2C%22isOpen%22%3A1%2C%22speed%22%3A10%2C%22density%22%3A40%2C%22opacity%22%3A86%2C%22isFilterColorFont%22%3A1%2C%22isOpenMask%22%3A0%2C%22proofShield%22%3A0%2C%22forcedFontSize%22%3A24%2C%22isFilterImage%22%3A1%2C%22defaultSwitch%22%3A0%2C%22hideRoleTip%22%3A1%2C%22hadTip%22%3A1%7D; QP0036=2022521%7C12.239; QC007=https%2525252525252525252525253A%2525252525252525252525252F%2525252525252525252525252Fwww.baidu.com%2525252525252525252525252Flink%2525252525252525252525253Furl%2525252525252525252525253DXAEKzWasUb-NpH69tGHWnERYdhOQHtQtyN30Yd9AWE3%25252525252525252525252526wd%2525252525252525252525253D%25252525252525252525252526eqid%2525252525252525252525253Dedc8bc0d001fc32e000000066288f10a; QC010=91379870; IMS=IggQARj_mKSUBioyCiAzNjE5ZDJmYjZlNTE2MTE4NGFkZTMzOTFjMTk0OWI1ZBAAIggI0AUQAhiwCShvMAVyJAogMzYxOWQyZmI2ZTUxNjExODRhZGUzMzkxYzE5NDliNWQQAIoBJAoiCiAzNjE5ZDJmYjZlNTE2MTE4NGFkZTMzOTFjMTk0OWI1ZA',
    'origin': 'https://www.iqiyi.com',
    'referer': 'https://www.iqiyi.com/v_27ga7s278wk.html?vfrm=pcw_dianying&vfrmblk=E&vfrmrst=711219_dianying_top_video_play4',
    'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36',
}
url = 'https://cache.video.iqiyi.com/dash?tvid=8127243558006200&bid=100&vid=9b7e5dc83572dd765e31e27afcdaf219&src=01010031010000000000&vt=0&rs=1&uid=1637120337&ori=pcw&ps=1&k_uid=a43c7ad82fc48176cc85b5c4129ecbd7&pt=0&d=0&s=&lid=&cf=&ct=&authKey=e185d81f6c107463868c1ee12bd76f29&k_tag=1&dfp=a1e1a229d2d3f749d5b2a6c2427248ea7cac684687c9eca03d7c70318a8a8a9967&locale=zh_cn&prio=%7B%22ff%22%3A%22f4v%22%2C%22code%22%3A2%7D&pck=99oQ98bPstG6fxeEyhAD6m3EpddiZo1PZ6x0pNiFQzcWbm3JDuaNga85yqDIzHm27kt9M4f&k_err_retries=0&up=&qd_v=2&tm=1653141865779&qdy=a&qds=0&k_ft1=706436220846084&k_ft4=1161084347621380&k_ft5=262145&bop=%7B%22version%22%3A%2210.0%22%2C%22dfp%22%3A%22a1e1a229d2d3f749d5b2a6c2427248ea7cac684687c9eca03d7c70318a8a8a9967%22%7D&ut=16&vf=a13791f173ecf007e7340cddbf941d16'
response = requests.get(url=url, headers=headers)
json_data = response.json()
m3u8 = json_data['data']['program']['video'][1]['m3u8']
ts_list = re.sub('#E.*', '', m3u8)
ts_list = ts_list.split()
for ts in tqdm(ts_list):
    ts_data = requests.get(ts).content
    with open('黄金蜘蛛城.mp4', mode='ab') as f:
        f.write(ts_data)