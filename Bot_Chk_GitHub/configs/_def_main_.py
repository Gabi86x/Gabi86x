from pyrogram import Client,filters
from Inc.Plantillas import *
from pyrogram import *
from Inc.botones import *
import os,requests,re
from configs.ccs import *
from datetime import datetime, timedelta
import requests
import time
import random
from configs.bin_data import * 
from configs.mongoDB import *
from telethon import utils

def gabi(bit):
    nix = Client.on_message(filters.command(bit, prefixes=["/",".",",","-","$","%","!",";","?"], case_sensitive=False) & filters.text)
    return nix

def pro(bor):
    nox = Client.on_callback_query(filters.regex(bor))
    return nox

def cls():
    os.system('cls' if os.name == 'nt' else 'clear')
    print('BOT ON')
    
    
apid = 'TU_API_ID'
apihasd = 'TU_API_HASH'
token = 'TU_TOKEN_BOT'

def conta(call):
    if call == 'apid':
        return apid
    elif call == 'hasd':
        return apihasd
    else:
        return token 


usertime = {}
timetake = 50
def atspam(func):
    async def wrapper(client, message):
        user_id = message.from_user.id
        if 5416957433 in usertime and time.time() - usertime[user_id] < timetake:
            await func(client, message)
            usertime[user_id] = time.time()
            return
        elif user_id in usertime and time.time() - usertime[user_id] < timetake:
            wait_time = int(timetake - (time.time() - usertime[user_id]))
            await message.reply(f"<b>[ANTISPAM]</b>")
            return
        else:
            await func(client, message)
            usertime[user_id] = time.time()

    return wrapper