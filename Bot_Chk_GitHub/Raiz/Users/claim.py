from configs._def_main_ import *



@gabi('claim')
async def claim(client,message):
	buscar_permisos = collection.find_one({"_id": message.from_user.id})
	if buscar_permisos is None: return await message.reply(text='<b>No estas registrado usa <code>/register</code></b>')

	ccs = message.text[len('/claim'):]
	espacios = ccs.split()
	if len(espacios)==0: return await message.reply('<b>/claim key</b>')
	key = espacios[0]

	encontrar_key = collection_dos.find_one({"key": key})
	if encontrar_key is None: return await message.reply(text='<b>Key invalida.</b>')
		
	days = encontrar_key['days']
	x = datetime.now() + timedelta(days=days)

	collection.update_one({"_id": message.from_user.id},{"$set": {"key": x}})
	collection.update_one({"_id": message.from_user.id},{"$set": {"plan": 'Premium'}})
	collection_dos.delete_one({"key": key})

	texto = f'''
𝙆𝙚𝙮 𝙍𝙚𝙘𝙡𝙖𝙢𝙖𝙙𝙖 𝘾𝙤𝙧𝙧𝙚𝙘𝙩𝙖𝙢𝙚𝙣𝙩𝙚✅
━━━━━━━━━━━━━━━━━━
•𝘿𝙞𝙖𝙨 𝙙𝙚 𝙥𝙧𝙚𝙢𝙞𝙪𝙢 ➪ <code>{days}</code>
•𝙋𝙡𝙖𝙣 ➪ <code>Premium</code>
•𝙁𝙚𝙘𝙝𝙖 𝙫𝙚𝙣𝙘𝙞𝙢𝙞𝙚𝙣𝙩𝙤 ➪ <code>{x.strftime("%d %B %X")}</code>
━━━━━━━━━━━━━━━━━━
•𝙊𝙬𝙣𝙚𝙧 ➪ <b><a href="tg://resolve?domain=Gabi_86x">𝑮𝒂𝒃𝒊</a></b>
'''

	await message.reply(texto)   