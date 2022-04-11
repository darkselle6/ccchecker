# This is a simple echo bot using the decorator mechanism.
# It echoes any incoming text messages.

from telebot.async_telebot import AsyncTeleBot
import asyncio
import logging
logging.basicConfig(level=logging.DEBUG, 
                    format='%(asctime)s - %(name)s - %(levelname)s - %(message)s') 
bot = AsyncTeleBot('5142948808:AAGO4SQp7MfDOI2vzsxhpPp2_e6NWLyOcUQ')

admins = [5197853005]
file = open('groups.txt','r')
# Handle '/start' and '/help'
@bot.message_handler(commands=['help', 'start'])
async def send_welcome(message):
    first = await bot.reply_to(message, """\
Starting Bot\
""")
    await bot.edit_message_text("Heya How are you ??\nWant to Check ccs?? Send /cmds for more",message.chat.id,first.id,parse_mode="HTML")

#asyncio.run(bot.polling())