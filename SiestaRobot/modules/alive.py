import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from SiestaRobot.events import register
from SiestaRobot import telethn as tbot


PHOTO = "https://telegra.ph/file/ff2fa22dfa6ae838cc6cd.jpg"

@register(pattern=("/alive"))
async def awake(event):
  TEXT = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), this ʙᴜᴍ ʙᴜᴍ ʙᴏᴛ.** \n\n"
  TEXT += "💠 **I'm Working Management Groups!** \n\n"
  TEXT += f"💠 **Bot Maker : [Zen](https://t.me/zenzuzu2)** \n\n"
  TEXT += f"💠 **Library Version :** `{telever}` \n\n"
  TEXT += f"💠 **Telethon Version :** `{tlhver}` \n\n"
  TEXT += f"💠 **Pyrogram Version :** `{pyrover}` \n\n"
  TEXT += "**Thanks For Adding Me.. I Will Safety Your Groups ❤️**"
  BUTTON = [[Button.url("Help", "https://t.me/BumBumRobot?start=help"), Button.url("Support", "https://t.me/dbzea")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=TEXT,  buttons=BUTTON)
