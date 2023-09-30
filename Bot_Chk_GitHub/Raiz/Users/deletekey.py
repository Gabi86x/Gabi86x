from configs._def_main_ import *

@gabi('unvip')
async def claim(client,message):
	buscar_permisos = collection.find_one({"_id": message.from_user.id})
	if buscar_permisos is None: return await message.reply(text='<b>No estas registrado usa <code>/register</code></b>',quote=True)

	ccs = message.text[len('/unvip'):]
	espacios = ccs.split()
	if len(espacios)==0: return await message.reply('<b>/unvip - key</b>')
	key = espacios[0]

	encontrar_key = collection_dos.find_one({"key": key})
	if encontrar_key is None: return await message.reply(text='<b>Key no existe</b>')
		
	collection_dos.delete_one({"key": key})

	texto = f'''<b>
La Key ha sido eliminada.
</b>'''

	await message.reply(texto)      
