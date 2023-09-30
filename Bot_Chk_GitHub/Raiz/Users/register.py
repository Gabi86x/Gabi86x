from configs._def_main_ import *


@gabi('register')
async def register(client,message):
    try:
        find = collection.find_one({"_id": message.from_user.id})
        if find is None:
                            
            mydict = {
            "_id": message.from_user.id,
            "id": message.from_user.id,
            "username": message.from_user.username,
            "plan": "Free User",
            "role": "User",
            "since": datetime.now(),
            "key" : 'None',        
            }
            
            collection.insert_one(mydict)    
            text = f'<b>Registro Exitoso!</b>✅'
            await message.reply(text)
        else:
            await message.reply('<b>Ya Estas Registrado!</b>✅')
    except Exception as e:
        print(e)










