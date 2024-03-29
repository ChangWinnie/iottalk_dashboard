# -*- coding: utf-8 -*
import requests
import time
from io import open

region = 'Tainan'
url = 'https://www.cwb.gov.tw/V7/observe/24real/Data/46741.htm'


def f(url, fn):
 headers = {
     'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_13_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'
 }
 res = requests.get(url, headers=headers)
 res.encoding = 'utf-8'

 open(fn,'wb').write(res.text.encode('utf-8'))

fn = region+ '.html'.format(0,0)
f(url, fn)


from bs4 import BeautifulSoup

def get_element(soup, tag, class_name):
    data = []
    table = soup.find(tag, attrs={'class':class_name})
    rows = table.find_all('tr')
    del rows[0]
    
    for row in rows:
        first_col = row.find_all('th')
        cols = row.find_all('td')
        cols.insert(0, first_col[0])
        cols = [ele.text.strip() for ele in cols]
        data.append([ele for ele in cols if ele]) 
    return data

   
file_name = region+".html"

f = open (file_name,'r', encoding='utf-8')
s = f.readlines()
s = ''.join(s)

soup = BeautifulSoup(s, "lxml")

df_tmp = get_element(soup, 'table','BoxTable')
#print("df_tmp==========",df_tmp[0])

#########################################################################################
import pandas as pd
#print ('Region :', region,'Building table ...')
col_list = ['觀測時間', '溫度(°C)', '溫度(°F)', '天氣', '風向', '風力 (m/s)|(級)', '陣風 (m/s)|(級)', '能見度(公里)', '相對溼度(%)', '海平面氣壓(百帕)', '當日累積雨量(毫米)', '日照時數(小時)']
df = pd.DataFrame(columns = col_list)
df_tmp = pd.DataFrame(df_tmp)
df_tmp.columns = col_list
df = pd.concat([df, df_tmp], axis=0)   
df = df.reset_index(drop=True)    
#print(df)

timee = df['觀測時間'][0]
temperature = df['溫度(°C)'][0]
winddir = df['風向'][0]
windpow = df['風力 (m/s)|(級)'][0]
humidity = df['相對溼度(%)'][0]
rain = df['當日累積雨量(毫米)'][0]
pressure = df['海平面氣壓(百帕)'][0]
#allstring = "time:" + timee+ "tem:" + temperature + " wind_dir:" + winddir + " wind_pow:" + windpow + " hum:" + humidity + " rain:"+rain

#print("溫度：",allstring)
df.to_csv(( region + '.csv'), encoding = 'utf-8')

import requests, time
import csmapi, DAN
from datetime import datetime as dt

ServerURL = 'https://2.iottalk.tw' #Change to your IoTtalk IP or None for autoSearching
Reg_addr='aaaaaasd' # if None, Reg_addr = MAC address

DAN.profile['dm_name']='Dummy_Device'
DAN.profile['df_list']=['AtPressure', 'Humidity', 'windspeed', 'rain', 'Temperature','Dummy_Control']
#DAN.profile['d_name']= 'changhsinjung' 

DAN.device_registration_with_retry(ServerURL, Reg_addr)
#alias = DAN.get_alias('Dummy_Sensor')
#print(alias)

while 1:
    try:
        #DAN.push("Dummy_Sensor",allstring)
        DAN.push ('AtPressure', pressure)
        DAN.push ('Humidity', humidity)
        DAN.push ('windspeed', windpow)
        DAN.push ('rain',rain)
        DAN.push("Temperature",temperature)
		#x = DAN.pull("Dummy_Control")
        #print("x=====",x)

    except Exception as e:
        print(e)

    time.sleep(5)

