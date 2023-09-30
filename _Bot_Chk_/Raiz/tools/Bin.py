from configs._def_main_ import *

@gabi('bin')
async def start(client,msg):
        encontrar_usuario = collection.find_one({"_id": msg.from_user.id})
        inicio = time.time()

        if encontrar_usuario is None: return await msg.reply(text='<b>No estas registrado usa <code>/register</code></b>',quote=True)
        ccbin = msg.text[len('/bin '):]
        if not ccbin: return await msg.reply('<code>/bin 551507</code>')
        
        if len(str(ccbin)) < 6: return await msg.reply('<b>❌ Invalid BIN.</b>')


        binif=ccbin
                               
        name = msg.from_user.username
        
        fin = time.time()
            
        tiempo = fin - inicio
        x = get_bin_info(ccbin[0:6])
            
        msg1 = f'''<b>
•𝘽𝙄𝙉 ➪ <code>{binif}</code>
•𝙏𝙔𝙋𝙀 ➪ <code>{x.get("vendor")} - {x.get("type")} - {x.get("level")}</code>
•𝘾𝙊𝙐𝙉𝙏𝙍𝙔 ➪ <code>{x.get("country")} {x.get("flag")}</code>
•𝘽𝘼𝙉𝙆 ➪ <code>{x.get("bank_name")}</code>

•𝘾𝙝𝙚𝙘𝙠𝙚𝙧 𝘽𝙮 ➪ @{name} | {encontrar_usuario['plan']}
</b>'''
            
        await msg.reply(msg1)
    