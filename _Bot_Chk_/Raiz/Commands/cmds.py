from configs._def_main_ import *

@gabi(['cmd','cmds','comandos','ayuda'])
async def cmd(client,msg):
        encontrar_usuario = collection.find_one({"_id": msg.from_user.id})
        
        if encontrar_usuario is None: return await msg.reply('<b>No estas registrado usa <code>/register</code></b>')
        await msg.reply(cmds,reply_markup=botoncmd)
    
