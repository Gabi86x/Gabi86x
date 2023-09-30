from configs._def_main_ import *

@pro('SilverBullet')
async def silver(client, msg):
    await msg.edit_message_text(Sistema_hits,reply_markup=atrasboton)