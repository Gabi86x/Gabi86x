from configs._def_main_ import *

@gabi(['id','myid','mid','idk','idchat','chatid'])
async def myid(client,msg):
    await msg.reply(f'''━━━━━━━━━━━━━ 
•𝙐𝙎𝙀𝙍 𝙄𝘿 ➪ <code>{msg.from_user.id}</code>
•𝘾𝙃𝘼𝙏 𝙄𝘿 ➪ <code>{msg.chat.id}</code>               
</b>''')