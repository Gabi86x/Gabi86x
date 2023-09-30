from configs._def_main_ import *

@gabi('zip')
async def start(client,msg):
        encontrar_usuario = collection.find_one({"_id": msg.from_user.id})
        
        if encontrar_usuario is None: return await msg.reply(text='<b>No estas registrado usa <code>/register</code></b>',quote=True)
        codep = msg.text[len('/zip '):]
        if not codep: return await msg.reply('<code>/zip 10010</code>')
        zip_api = requests.get(f'https://zip.getziptastic.com/v2/US/{codep}')

        if 'Not Found' in zip_api.text:
            return await msg.reply('<b> codigo postal erroneo. ❌</b>')
        else:
            
            pais=zip_api.json()['country']
            cap=zip_api.json()['postal_code']
            ciudad= zip_api.json()['city']
            estado=zip_api.json()['state_short']
            name=msg.from_user.username
            
            zip = f"""

𝙕𝙞𝙥 ➪ <code>{cap}</code>
𝘾𝙤𝙪𝙣𝙩𝙧𝙮 ➪ <code>{pais}</code>          
𝘾𝙞𝙪𝙙𝙖𝙙 ➪ <code>{ciudad}</code>           
𝙀𝙨𝙩𝙖𝙙𝙤 ➪ <code>{estado}</code>     

𝙕𝙞𝙥 𝘽𝙮 ➪ @{name} | <b>{encontrar_usuario['plan']}</b>

</b>"""

            await msg.reply(zip)    
    