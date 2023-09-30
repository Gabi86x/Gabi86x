from configs._def_main_ import *

@pro('regen')
async def regen(client, msg):   
    men = msg.message.reply_to_message.text
    inicio = time.time()
    geneoa= men.split()[1]
    
    geneo = re.findall(r'[0-9]+',geneoa)
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

    cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9,cc10 = cc_gen(cc,mes,ano,cvv)
    
    name=msg.from_user.username
    
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


    cc1,cc2,cc3,cc4,cc5,cc6,cc7,cc8,cc9,cc10, = cc_gen(cc,mes,ano,cvv)
    
    fin = time.time()
    
    x = get_bin_info(geneoa[0:6])
            
    tiempo_final = fin - inicio 
    encontrar_usuario = collection.find_one({"_id": msg.message.reply_to_message.from_user.id})

    gen = f"""

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
𝗧𝗶𝗺𝗲 ➪ <code>{tiempo_final:0.2}</code>
"""  

    await msg.edit_message_text(gen,reply_markup=regene)

