from configs._def_main_ import *

FOLDER = "DATABIN" 
DATA_FILE = "apibin.txt"

@pro('extras')
async def reextras(client, msg):   
    men = msg.message.reply_to_message.text
    inicio = time.time()
    geneoa= men.split()[1]
    
    with open(f"{FOLDER}/{DATA_FILE}", "r") as f:
        for line in f:
            if line.startswith(geneoa):
                card = line[0:9]
               
                binreq = requests.get(f'https://bins.antipublic.cc/bins/{geneoa}')
                brand = binreq.json()['brand']
                country_name = binreq.json()['country_name']
                country_flag = binreq.json()['country_flag']
                bank = binreq.json()['bank']
                level = binreq.json()['level']
                typea = binreq.json()['type']
            
                year1 = (random.randint(2024, 2029))
                year2 = (random.randint(2024, 2029))
                year3 = (random.randint(2024, 2029))
                year4 = (random.randint(2024, 2029))
                year5 = (random.randint(2024, 2029))
                year6 = (random.randint(2024, 2029))
                year7 = (random.randint(2024, 2029))
                year8 = (random.randint(2024, 2029))
                year9 = (random.randint(2024, 2029))
                
                
               
                mes1 = (random.choice(("01","02","03","04","05","06","07","09","09","10","11","12")))
                mes2 = (random.choice(("01","02","03","04","05","06","07","09","09","10","11","12")))
                mes3 = (random.choice(("01","02","03","04","05","06","07","09","09","10","11","12")))
                mes4 = (random.choice(("01","02","03","04","05","06","07","09","09","10","11","12")))
                mes5 = (random.choice(("01","02","03","04","05","06","07","09","09","10","11","12")))
                mes6 = (random.choice(("01","02","03","04","05","06","07","09","09","10","11","12")))
                mes7 = (random.choice(("01","02","03","04","05","06","07","09","09","10","11","12")))
                mes8 = (random.choice(("01","02","03","04","05","06","07","09","09","10","11","12")))
                mes9 = (random.choice(("01","02","03","04","05","06","07","09","09","10","11","12")))
                
        
                extra1 = (random.randrange(100,950,3))
                extra2 = (random.randrange(100,950,3))
                extra3 = (random.randrange(100,950,3))
                extra4 = (random.randrange(100,950,3))
                extra5 = (random.randrange(100,950,3))
                extra6 = (random.randrange(100,950,3))
                extra7 = (random.randrange(100,950,3))
                extra8 = (random.randrange(100,950,3))
                extra9 =  (random.randrange(100,950,3))
                
                que = line[0:9]


                fin = time.time()

                tiempo = fin - inicio
            
                encontrar_usuario = collection.find_one({"_id": msg.message.reply_to_message.from_user.id}) 
                x = get_bin_info(geneoa)
                regen = f"""
                
<code>{que}{extra1}xxxx|{mes1}|{year1}|rnd</code>
<code>{que}{extra2}xxxx|{mes2}|{year2}|rnd</code>
<code>{que}{extra3}xxxx|{mes3}|{year3}|rnd</code>
<code>{que}{extra4}xxxx|{mes4}|{year4}|rnd</code>
<code>{que}{extra5}xxxx|{mes5}|{year5}|rnd</code>
<code>{que}{extra6}xxxx|{mes6}|{year6}|rnd</code>
<code>{que}{extra7}xxxx|{mes7}|{year7}|rnd</code>
<code>{que}{extra8}xxxx|{mes8}|{year8}|rnd</code>
<code>{que}{extra9}xxxx|{mes9}|{year9}|rnd</code>

•𝙀𝙭𝙩𝙧𝙖 ➪ <code>{geneoa}</code>
•𝙋𝙖𝙞𝙨 ➪ <code>{x.get("country")} {x.get("flag")}</code>
•𝙄𝙣𝙛𝙤 ➪ <code>{x.get("vendor")} - {x.get("type")} - {x.get("level")}</code>
•𝘽𝙖𝙣𝙠 ➪ <code>{x.get("bank_name")}</code>

•𝘾𝙝𝙚𝙘𝙠𝙚𝙧 𝘽𝙮 ➪ <code>{msg.from_user.username}</code> | <b>{encontrar_usuario['plan']}</b>
"""
                    
                await msg.edit_message_text(regen,reply_markup=ExtraRegen)
                await msg.delete