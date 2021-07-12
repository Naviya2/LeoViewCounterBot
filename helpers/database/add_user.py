# (c) @Naviya2

from configs import Config
from helpers.database.access_db import db
from pyrogram import Client
from pyrogram.types import Message


async def AddUserToDatabase(event: Client, message: Message):
    if not await db.is_user_exist(message.from_user.id):
        await db.add_user(message.from_user.id)
        if Config.LOG_CHANNEL is not None:
            await client.send_message(
                int(Config.LOG_CHANNEL),
                f"#NEW_USER: \n\nNew User [{message.from_user.first_name}](tg://user?id={message.from_user.id}) started using @leoviewcounterbot 🇱🇰"
            )
