from configs._def_main_ import *

@gabi(['start','ini'])
async def start(_,msg):
        msg1=await msg.reply(f'𝗛𝗼𝗹𝗮! @{msg.from_user.username}')
        time.sleep(1.5)
        encontrar_usuario = collection.find_one({"_id": msg.from_user.id})
        
        if encontrar_usuario is None: return await msg1.edit(text='<b>No estas registrado usa <code>/register</code></b>')
        msg2=await msg1.edit('𝗡𝗼𝘀 𝗮𝗹𝗲𝗴𝗿𝗮 𝘁𝗲𝗻𝗲𝗿𝘁𝗲 𝗮𝗾𝘂𝗶')
        time.sleep(1.5)
        await msg2.edit(startx.format(adc=msg.from_user.id,ada=msg.from_user.first_name,abdc=msg.from_user.username))
    