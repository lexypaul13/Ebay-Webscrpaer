#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Dec 12 15:52:45 2019

@author: alexpaul
"""
from bs4 import BeautifulSoup
import requests

URL = 'https://www.ebay.com/itm/Apple-MacBook-Pro-15-Retina-Core-i7-16GB-1TB-SSD-OS-2018-3-YEAR-WARRANTY/143440997572?_trkparms=ispr%3D1&hash=item2165bfecc4:g:~m8AAOSwyMVd3Dfd&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qUr9BI06g4qApQUQIftO0yWCcbMsEOWChb89V0YNyLo5CMHYieABqMek6xrLVPeP%2Bn2jkS%2BNt6Qde32tChuHthRgeOqWSKJD%2BKe%2FYgjW4iYmSvM1i14NTco4o7PiOb8YsNmTJBiONjZVrz5tiOUDj5TEskfy%2B6PAglAZQ2Y3%2FANt0uJo1kKOu6L5ezuWM%2BAhdOOPWgUcju3H3CyjISoRu4LMRRcB%2FsK5Xg81y2%2BgFtC97zYxtpmC2P1rGC60ptAUGyKJ2QS08zFIEbiq0GAx5WMez4Dxtb73E%2B5kb4xpzESdovgmHOeJr2IkUevMxfzLDxnBSKB8zzh80Vr6ALImkk5%2BspqE7mty7oAXn%2Bjw2gbEZNQJ31wjaD%2FvkOO6Nas7Vm2oWkCxiEJz9ZtFG%2FzDbKga5A4tX2y40yjfLBJZqXmtWIHBwsYTQCzAiuNpe9D7Uf%2FH4KVQzYqGTvpb%2BMA%2B1%2BawGJ8kuDybaPzmAmuDhUWAhnI24U2Dtc6F290xIcPRO%2BcZ1vIlRBXBS1N7HtaoDQJ5RG2cQhAP2NeV493Bh4skQgke%2FfxxnNnSKiMxtGEJ6i%2FutvhftYYt441xnW2BwV6%2FWw8WGNY7LvBw9D3%2B1pfc1kpu1lPQVQMYayGDhaICOQlA%2FpTTYEaIzYBgZnlOANzmVl1qWVvcJZ2ljDw4bz1YZQ4dB2X87ZTbq1M%2F66p7iJOvFwKEPo2SygAZMwrmupe7Uj61gF5%2BbGhMEXO888F%2Fw%3D%3D&checksum=1434409975720f0a0bb0d8e5410e814448a44c4bce6c&enc=AQAEAAACQBPxNw%2BVj6nta7CKEs3N0qUr9BI06g4qApQUQIftO0yWCcbMsEOWChb89V0YNyLo5CMHYieABqMek6xrLVPeP%2Bn2jkS%2BNt6Qde32tChuHthRgeOqWSKJD%2BKe%2FYgjW4iYmSvM1i14NTco4o7PiOb8YsNmTJBiONjZVrz5tiOUDj5TEskfy%2B6PAglAZQ2Y3%2FANt0uJo1kKOu6L5ezuWM%2BAhdOOPWgUcju3H3CyjISoRu4LMRRcB%2FsK5Xg81y2%2BgFtC97zYxtpmC2P1rGC60ptAUGyKJ2QS08zFIEbiq0GAx5WMez4Dxtb73E%2B5kb4xpzESdovgmHOeJr2IkUevMxfzLDxnBSKB8zzh80Vr6ALImkk5%2BspqE7mty7oAXn%2Bjw2gbEZNQJ31wjaD%2FvkOO6Nas7Vm2oWkCxiEJz9ZtFG%2FzDbKga5A4tX2y40yjfLBJZqXmtWIHBwsYTQCzAiuNpe9D7Uf%2FH4KVQzYqGTvpb%2BMA%2B1%2BawGJ8kuDybaPzmAmuDhUWAhnI24U2Dtc6F290xIcPRO%2BcZ1vIlRBXBS1N7HtaoDQJ5RG2cQhAP2NeV493Bh4skQgke%2FfxxnNnSKiMxtGEJ6i%2FutvhftYYt441xnW2BwV6%2FWw8WGNY7LvBw9D3%2B1pfc1kpu1lPQVQMYayGDhaICOQlA%2FpTTYEaIzYBgZnlOANzmVl1qWVvcJZ2ljDw4bz1YZQ4dB2X87ZTbq1M%2F66p7iJOvFwKEPo2SygAZMwrmupe7Uj61gF5%2BbGhMEXO888F%2Fw%3D%3D&checksum=1434409975720f0a0bb0d8e5410e814448a44c4bce6c'
 
headers = {"User-agent": 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_14_6) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/13.0.4 Safari/605.1.15'}

#return data from website 
page = requests.get(URL)

soup = BeautifulSoup(page.content, 'html.parser')
title = soup.find(id="itemTitle")

price = soup.find(id= "prcIsum")
price_of_item = float(price.get_text().strip("US $"))
print(title.get_text().strip("Details about"))
            

def price_check(item):
    if(item < 1000):
        print('The items price has dropped!')
    else:
            print('price is till high')
    


price_check(price_of_item)

