from main import bot
import asyncio
import telebot
import cmds
import add
import chk
import defs
import sc
import services.mongodb
import services.redisdb
import zc
asyncio.run(bot.polling())
