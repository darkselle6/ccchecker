from main import *  

@bot.message_handler(commands=['add'])
async def bin(message):
	if message.from_user.id not in admins:
		await bot.reply_to(message,"Only Authorized for Mod and owners")
	else:
		file = open('groups.txt', 'r') 
		if str(message.chat.id) + "\n" not in file.readlines():
                     file = open('groups.txt', 'a+') 
                     file.write(str(message.chat.id) + "\n")
                     file.close()
                     await bot.reply_to(message,"Now Added")
		else:
			await bot.reply_to(message,"Already Added")
