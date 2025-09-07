from pyrogram import Client, filters
from pyrogram.types import Message

from loader import app, logger

@app.on_message(filters.command(["status"]))
async def status_reply(client: Client, message: Message):
    try:
        await message.reply("Наверное работает")
    except Exception as exeption:
        logger.error("Чёто не работает: {exeption}", exc_info=True)

@app.on_message(filters.command(["tag"]) & filters.group)
async def everyone_command(client: Client, message: Message):
    try:
        if message.reply_to_message_id is not None:
            message.reply("Тегнутые люди должны выполнить задание/проявить активность", reply_to_message_id= message.reply_to_message_id)
        else:
            message.reply("Тегнутые люди должны выполнить задание/проявить активность", quote=True)
        
    except Exception as exeption:
        logger.error("Ошибка при попытке протегать: {exeption}", exc_info=True)