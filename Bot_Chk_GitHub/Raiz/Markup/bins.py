from configs._def_main_ import *

@pro('bins')
async def gates(client, msg):
    await msg.edit_message_text(bins,reply_markup=atrasboton)