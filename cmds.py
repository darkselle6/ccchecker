from main import bot

@bot.message_handler(commands=['cmds'])
async def send_command(message):
    msg = await bot.reply_to(message, """\
Getting Commands\
""")
    await bot.edit_message_text("XTRA VERSION 1.9 | COMMANDS\n\nSTRIPE AUTH— <code>/chk</code> [Reviewed: 07.04.2022] [GATE IS OFF ]\nSTRIPE AUTH 2— <code>/sc</code> [Reviewed: 10.04.2022] ",message.chat.id,msg.id,parse_mode="HTML")
