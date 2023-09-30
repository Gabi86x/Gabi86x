from configs._def_main_ import *
                                    
@gabi('vip')
async def vip(client,message):
	buscar_permisos = collection.find_one({"_id": message.from_user.id})
	if buscar_permisos is None: return await message.reply(text='<b>No estas registrado usa <code>/register</code></b>')
		
	if buscar_permisos["role"] == "Owner" or buscar_permisos["role"] == "Co-Owner": pass	
	else: return await message.reply(text='<b>❌Lo siento pero no eres administrador para poder usar este comando❌</b>')
		
	ccs = message.text[len('/vip'):]
	espacios = ccs.split()
	if len(espacios)==0: return await message.reply('<b>/vip dias</b>')
		
	days = espacios[0]

	key = f'Key-{str(random.randint(1000, 9999))}-IZUKU-{str(random.randint(1000, 9999))}-{str(random.randint(1000, 9999))}/{days}'
	my_dict = {
	"key" : key,
	"days" : int(days)
	}
	collection_dos.insert_one(my_dict)
	texto = f'''
𝙆𝙚𝙮 𝙂𝙚𝙣𝙚𝙧𝙖𝙙𝙖 𝙀𝙭𝙞𝙩𝙤𝙨𝙖𝙢𝙚𝙣𝙩𝙚 ✅
━━━━━━━━━━━━━━
•𝙆𝙚𝙮 ➪ <code>{key}</code>
•𝘿𝙞𝙖𝙨 𝙙𝙚 𝙥𝙧𝙚𝙢𝙞𝙪𝙢 ➪ <code>{days}</code>
•𝙋𝙡𝙖𝙣 ➪ <code>Premium</code>
━━━━━━━━━━━━━━
•𝙋𝙖𝙧𝙖 𝙧𝙚𝙘𝙡𝙖𝙢𝙖𝙧 𝙪𝙨𝙖 <code>/reclaim {key}</code>
'''
	await message.reply(texto)