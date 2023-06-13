import requests
import threading
import os
import sys
import time
import random
import asyncio
from itertools import cycle

URL = 'https://discord.com/api/v9/applications'

os.system('')
def token_er():
    os.system('cls || clear')
    token = input("Token?:  ")
    
    if requests.get("https://discord.com/api/v9/users/@me", headers={"Authorization": f'{token}'}).status_code == 200:
        return token
    else:
        print('Invalid Token')
        ti
        return token_er()

token = token_er()

def bypassHeader(token):
    return {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:102.0) Gecko/20100101 Firefox/102.0',
        'Accept': '*/*',
        'Accept-Language': 'fr,fr-FR;q=0.8,en-US;q=0.5,en;q=0.3',
        'Accept-Encoding': 'gzip, deflate, br',
        'Content-Type': 'application/json',
        'X-Context-Properties': 'eyJsb2NhdGlvbiI6IkpvaW4gR3VpbGQiLCJsb2NhdGlvbl9ndWlsZF9pZCI6Ijk4OTkxOTY0NTY4MTE4ODk1NCIsImxvY2F0aW9uX2NoYW5uZWxfaWQiOiI5OTAzMTc0ODgxNzg4NjgyMjQiLCJsb2NhdGlvbl9jaGFubmVsX3R5cGUiOjB9',
        'Authorization': token,
        'X-Super-Properties': 'eyJvcyI6IldpbmRvd3MiLCJicm93c2VyIjoiRmlyZWZveCIsImRldmljZSI6IiIsInN5c3RlbV9sb2NhbGUiOiJmciIsImJyb3dzZXJfdXNlcl9hZ2VudCI6Ik1vemlsbGEvNS4wIChXaW5kb3dzIE5UIDEwLjA7IFdpbjY0OyB4NjQ7IHJ2OjEwMi4wKSBHZWNrby8yMDEwMDEwMSBGaXJlZm94LzEwMi4wIiwiYnJvd3Nlcl92ZXJzaW9uIjoiMTAyLjAiLCJvc192ZXJzaW9uIjoiMTAiLCJyZWZlcnJlciI6IiIsInJlZmVycmluZ19kb21haW4iOiIiLCJyZWZlcnJlcl9jdXJyZW50IjoiIiwicmVmZXJyaW5nX2RvbWFpbl9jdXJyZW50IjoiIiwicmVsZWFzZV9jaGFubmVsIjoic3RhYmxlIiwiY2xpZW50X2J1aWxkX251bWJlciI6MTM2MjQwLCJjbGllbnRfZXZlbnRfc291cmNlIjpudWxsfQ==',
        'X-Discord-Locale': 'en-US',
        'X-Debug-Options': 'bugReporterEnabled',
        'Origin': 'https://discord.com',
        'DNT': '1',
        'Connection': 'keep-alive',
        'Referer': 'https://discord.com/developers/applications', 
        'Cookie': '__dcfduid=21183630021f11edb7e89582009dfd5e; __sdcfduid=21183631021f11edb7e89582009dfd5ee4936758ec8c8a248427f80a1732a58e4e71502891b76ca0584dc6fafa653638; locale=en-US',
        'Sec-Fetch-Dest': 'empty',
        'Sec-Fetch-Mode': 'cors',
        'Sec-Fetch-Site': 'same-origin',
        'TE': 'trailers',
    }
    
def bot_creator(session, name):
    json1 = {
        'name': name,
        'team_id': None
    }

    r = session.post(URL, headers=bypassHeader(token), json=json1)
    
    if r.status_code == 429:
        print('Ratelimited! Failed to create bot')
        try:
            time.sleep(r.json()['retry_after'])
        except:
            pass
    elif r.status_code == 201:
        print(f'Created Bot with name {name} \t\t\t\t[{r.json()["id"]}')

async def main():
    os.system('cls || clear')
    os.system('mode 90, 20 & title made by: lone#4279 (Bot maker/spammer)')
    print('''
    
    \033[38;2;255;200;0m   █▀▄▀█ ██   █  █▀ ▄███▄   █▄▄▄▄     
    \033[38;2;255;175;0m   █ █ █ █ █  █▄█   █▀   ▀  █  ▄▀     Made by: lone#4279
    \033[38;2;255;150;0m   █ ▄ █ █▄▄█ █▀▄   ██▄▄    █▀▀▌      Github: https://github.com/airlone
    \033[38;2;255;125;0m   █   █ █  █ █  █  █▄   ▄▀ █  █  
    \033[38;2;255;100;0m      █     █   █   ▀███▀     █   
    \033[38;2;255;75;0m     ▀     █   ▀             ▀    
    \033[38;2;255;50;0m          ▀                       \033[0m
    ''')
    
    
    amt = input("How many bots to create?:  ")
    names = input("Names? [use , for more than one]:  ")
    session = requests.Session()
    if ',' in names:
        nd = cycle(names.split(','))
    else:
        nd = names
     
    for i in range(int(amt)):
        try:
            no = next(nd)
        except:
            no = nd
        bot_creator(session, no)
        
    await asyncio.sleep(2)    
    await main()

if __name__ == "__main__":
    asyncio.run(main())        