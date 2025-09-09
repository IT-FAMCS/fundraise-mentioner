from pyrogram import Client, filters
from pyrogram.types import Message
import random
from loader import app, logger


@app.on_message(filters.command(["status"]))
async def status_reply(client: Client, message: Message):
    try:
        await message.reply("Работает")
    except Exception as exeption:
        logger.error(f"Чёто не работает: {exeption}", exc_info=True)


@app.on_message(filters.command(["rand"]) & filters.group)
async def rand_command(client: Client, message: Message):
    try:
        args = message.text.split()
        if len(args) < 2 or not args[1].isdecimal():
            await message.reply("Аргументом комманды должно быть количество людей, которых вы хотите заставить работать", quote=True)
            return
        
        mention_users_num = int(args[1])
        users_links = []

        async for user in app.get_chat_members(message.chat.id):
            if user.user.is_bot or user.user.is_deleted or message.from_user.id == user.user.id:
                continue
            users_links.append(f"[💀](tg://user?id={user.user.id})")

        if(mention_users_num > len(users_links) or mention_users_num < 1):
            await message.reply("Введите нормальное количество людей")
            return
        
        if message.reply_to_message_id is not None:
            await message.reply("Тегнутые люди должны выполнить задание/проявить активность", reply_to_message_id=message.reply_to_message_id)
        else:
            await message.reply("Тегнутые люди должны выполнить задание/проявить активность", quote=True)
        
        mention_users= random.sample(users_links, mention_users_num)
        for i in range(0, mention_users_num, 5):
            await message.reply(''.join(mention_users[i:i+5]), quote=False)
    except Exception as exeption:
        logger.error(
            f"Ошибка при попытке протегать: {exeption}", exc_info=True)
