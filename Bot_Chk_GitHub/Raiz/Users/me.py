from configs._def_main_ import *

@gabi('me')
async def me(client,message):

    try:  
        if message.reply_to_message.from_user.id:
            encontrar_usuario = collection.find_one({"_id": message.reply_to_message.from_user.id})
    except: encontrar_usuario = collection.find_one({"_id": message.from_user.id})
        
   
    if encontrar_usuario is None: return await message.reply(text='<b>No estas registrado usa <code>/register</code></b>')
        
    id_usuario = encontrar_usuario["id"]
    user_name = encontrar_usuario["username"]
    plan = encontrar_usuario["plan"]
    role = encontrar_usuario["role"]
    fecha = encontrar_usuario["since"]
    key_ = encontrar_usuario["key"]
    if key_ != 'None':
        key_ = key_.strftime('%d %B %X')
    else:
        key_ = 'None'
    
    texto=f"""<b>
    
•𝘿𝙖𝙩𝙤𝙨 𝙙𝙚𝙡 𝙐𝙨𝙪𝙖𝙧𝙞𝙤:

•𝙐𝙨𝙪𝙖𝙧𝙞𝙤 ➪ <code>{user_name}</code>
•𝙄𝘿 ➪ <code>{id_usuario}</code>
•𝙨𝙩𝙖𝙩𝙪𝙨 ➪ <code>{role}</code>
•𝙋𝙡𝙖𝙣 ➪ <code>{plan}</code>
•𝙁𝙚𝙘𝙝𝙖 𝙙𝙚 𝙧𝙚𝙜𝙞𝙨𝙩𝙧𝙤 ➪ <code>{fecha}</code>
•𝙆𝙚𝙮 ➪ <code>{key_}</code>
➜ <b><a href="https://api.ipify.org/?format=html">Presiona aqui para consultar tu IP</a></b>      
━━━━━━━━━━━━━━
•𝙊𝙬𝙣𝙚𝙧 ➪ <b><a href="tg://resolve?domain=Gabi_86x">𝑮𝒂𝒃𝒊</a></b>                   
</b>"""

    await message.reply(texto)
        

    