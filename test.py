#!/usr/bin/env python3.5
#-- coding: utf-8 --
import requests

req= requests.get('https://www.cryptocompare.com/api/data/coinlist/%27)
donnee=req.json()
l=donnee['Data']
user = input("quel crypto vous interesse chere cyberinvestisseur du deepweb ?\n")
if(user=="liste"):
    for i in l:
        print(l[i]['Symbol'])
else:
    req = requests.get('https://min-api.cryptocompare.com/data/price?fsym=ETH&tsyms=%27+user+%27,%27+%27USD%27)
    d=req.json()
    for i in d:
        print(i+" "+str(d[i]))

