from configs._def_main_ import *

@gabi('ip')
async def start(client,msg):
        encontrar_usuario = collection.find_one({"_id": msg.from_user.id})
        
        if encontrar_usuario is None: return await msg.reply(text='<b>No estas registrado usa <code>/register</code></b>',quote=True)
        ips = msg.text[len('/ip '):]
        if not ips: return await msg.reply('<b> Error Ip Invalida o no existe</b>')
        req = requests.get(f'https://ipwho.is/{ips}')
        if '"success":false' in req.text:
            return await msg.reply('<b>Invalid IP address ❌</b>')
        else:
            rr = req.json()
            
            country=rr['country']
            country_code=rr['country_code']
            emoji=rr['flag']['emoji']
            lat=rr['latitude']
            lon=rr['longitude']
            city=rr['capital']
            domi=rr['connection']['domain']
            zip=rr['postal']
            name=msg.from_user.username
            
            ip = f'''<b>

•𝙄𝙋 ➪ <code>{ips}</code>
•𝙎𝙏𝘼𝙏𝙐𝙎 ➪ <code>True ✅</code>
•𝙋𝘼𝙄𝙎 ➪ <code>{country} {emoji}</code>      
•𝘾𝙄𝙐𝘿𝘼𝘿 ➪ <code>{city}</code>      
•𝘾𝙊𝙊𝙍𝘿𝙀𝙉𝘼𝘿𝘼𝙎 ➪ <code>{lat} - {lon}</code>         
•𝙀𝙈𝙋𝙍𝙀𝙎𝘼 𝘿𝙀 𝙄𝙉𝙏𝙀𝙍𝙉𝙀𝙏 ➪ <code>{domi}</code>      
•𝘾𝙊𝘿𝙄𝙂𝙊 𝙋𝙊𝙎𝙏𝘼𝙇 ➪ <code>{zip}</code>

•𝙐𝙎𝙀𝙍 ➪ {name} | {encontrar_usuario['plan']}
</b>'''

            await msg.reply(ip) 
            
           