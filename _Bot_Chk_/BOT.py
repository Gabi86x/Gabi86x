from configs._def_main_ import *
# The bot configuration is imported here.


app = Client("Name_Bot",  # In the "Name_bot" area replace with the name of your bot.
        api_id = conta('apid'),
            api_hash = conta('hasd'),
                bot_token = conta('token'),
                    plugins=dict(root="Raiz"))

@app.on_callback_query()
async def callpri(app, callback_query):
    # Here it is noted that if someone uses someone else's menu they will get the Callback error message
    if callback_query.message.reply_to_message is not None and callback_query.message.reply_to_message.from_user.id != callback_query.from_user.id:
        await callback_query.answer("Please use your own menu❗️")
        return
    else:
        await callback_query.continue_propagation()

if app:
    cls(),app.run()
    
    
   