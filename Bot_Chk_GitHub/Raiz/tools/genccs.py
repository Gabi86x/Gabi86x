from configs._def_main_ import *

@Client.on_message(filters.command('gen', prefixes=["/",".",",","-","$","%","!",";","?"], case_sensitive=False) & filters.text)
async def gen(_,msg):
    
            encontrar_usuario = collection.find_one({"_id": msg.from_user.id})
            inicio = time.time()
            bin_prohibido = ['1','2','7','8','9']

            if encontrar_usuario is None: return await msg.reply(text='<b>No estas registrado usa <code>/register</code></b>',quote=True)
        
            ccbin = msg.text[len('/gen '):]
            if not ccbin: return await msg.reply('<b><code>/gen 434769</code></b>',quote=True)
            if len(str(ccbin)) < 6: return await msg.reply('<b>El bin es menor a 6 digitos</b>',quote=True)

            geneo = re.findall(r'[0-9]+',msg.text)
            if not geneo: return await msg.reply('<b> Error de generador.</b>',quote=True)
        
        
            name=msg.from_user.username
    
            if len(geneo) == 1:
                cc = geneo[0]
                mes = 'x'
                ano = 'x'
                cvv = 'x'
            elif len(geneo) ==2:
                cc = geneo[0]
                mes = geneo[1]
                ano = 'x'
                cvv = 'x'
            elif len(geneo) ==3:
                cc = geneo[0]
                mes = geneo[1]
                ano = geneo[2]
                cvv = 'x'
            elif len(geneo) ==4:
                cc = geneo[0]
                mes = geneo[1]
                ano = geneo[2]
                cvv = geneo[3]
            else:
                cc = geneo[0]
                mes = geneo[1]
                ano = geneo[2]
                cvv = geneo[3]

            cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9,cc10, = cc_gen(cc,mes,ano,cvv)
            
            extra = str(cc) + 'xxxxxxxxxxxxxxxxxxxxxxx'
            if mes == 'x':
             mes_2 = 'rnd'
            else:
                mes_2 = mes
            if ano == 'x':
             ano_2 = 'rnd'
            else:
                ano_2 = ano
            if cvv == 'x':
             cvv_2 = 'rnd'
            else:
                cvv_2 = cvv
                

            if cc[0] in bin_prohibido: return await msg.reply('<b>Invalid Bin ⚠️</b>',quote=True)  
                
            
            fin = time.time()
            
            tiempo_final = fin  - inicio
            x = get_bin_info(ccbin[0:6])
    
            text = f"""

𝘾𝙖𝙧𝙙 𝙂𝙚𝙣𝙚𝙧𝙖𝙩𝙤𝙧 
𝙂𝙚𝙣 𝘽𝙮  ➪ @{name} | <b>{encontrar_usuario['plan']}</b>

<code>{cc1}</code>
<code>{cc2}</code>  
<code>{cc3}</code>
<code>{cc4}</code> 
<code>{cc5}</code>
<code>{cc6}</code>
<code>{cc7}</code>
<code>{cc8}</code>
<code>{cc9}</code>
<code>{cc10}</code>

𝗗𝗲𝘁𝗮𝗹𝗹𝗲𝘀: 
𝗜𝗻𝗽𝘂𝘁 ➪  <code>{extra[0:16]}|{mes_2}|{ano_2}|{cvv_2}</code>
𝗕𝗶𝗻 𝗜𝗻𝗳𝗼 ➪ <code>{x.get("vendor")} - {x.get("type")} - {x.get("level")}</code>
𝗖𝗼𝘂𝗻𝘁𝗿𝘆 ➪ <code>{x.get("country")} {x.get("flag")}</code>
𝗕𝗮𝗻𝗸 ➪ <code>{x.get("bank_name")}</code>
"""  

            Client.send_message(_,chat_id=msg.chat.id,text=text,reply_to_message_id=msg.id,reply_markup=regene)

  
