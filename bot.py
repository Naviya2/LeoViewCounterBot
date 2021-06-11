# (c) 2021-22 < @Naviya2 >
# < Leo Projects >

import logging
import asyncio
from telethon import TelegramClient, events, Button
from decouple import config
from telethon.tl.functions.users import GetFullUserRequest

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s', level=logging.WARNING)

# start the bot
print("Starting...")
try:
    apiid = config("APP_ID", cast=int)
    apihash = config("API_HASH")
    bottoken = config("BOT_TOKEN")
    FRWD_CHANNEL = config("FRWD_CHANNEL", cast=int)
    LeoProjects = TelegramClient('leosupportx', apiid, apihash).start(bot_token=bottoken)
except:
    print("Environment vars are missing! Kindly recheck.")
    print("Bot is quiting...")
    exit()

@BotzHub.on(events.NewMessage(pattern="/start", func=lambda e: e.is_private))
async def _(event):
    ok = await BotzHub(GetFullUserRequest(event.sender_id))
    await event.reply(f"Hello {ok.user.first_name}👋 \nI'm a Leo View Counter Bot 🇱🇰\nSend me a message and I'll attach a view count to it 🙂,
                    buttons=[
                        [Button.url("Developer🧑‍💻", url="https://t.me/naviya2"),
                        Button.url("Rate us  ★", url="https://t.me/tlgrmcbot?start=leoviewcounterbot-review")]
                  
                        [Button.url("Updates Channel🗣", url="https://t.me/new_ehi"),
                        Button.url("Support Group👥", url="https://t.me/leosupportx")]
                    ])

@BotzHub.on(events.NewMessage(incoming=True, func=lambda e: e.is_private))
async def countit(event):
    if event.text.startswith('/'):
        return
    x = await event.forward_to(FRWD_CHANNEL)
    await x.forward_to(event.chat_id)

print("Leo View Counter Bot is Started")
print("Do visit @new_ehi..")
BotzHub.run_until_disconnected()
