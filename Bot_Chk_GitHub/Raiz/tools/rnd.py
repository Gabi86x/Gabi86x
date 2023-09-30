from configs._def_main_ import *

@gabi('fake')
async def fake(client,message):
            encontrar_usuario = collection.find_one({"_id": message.from_user.id})
        

            if encontrar_usuario is None: return await message.reply(text='<b>No estas registrado usa <code>/register</code></b>',quote=True)
            pais = message.text[len('/fake '):]
            if not pais:
               await message.reply("<code>/fake us</code>")
               return 
            
            api = requests.get(f'https://randomuser.me/api/1.2/?nat={pais}')
            data = api.json()['results'][0]

            first_name = data['name']['first']
            last_name = data['name']['last']
            street = data['location']['street']
            city = data['location']['city']
            state = data['location']['state']
            postcode = data['location']['postcode']
            country = data['nat']
            ssn = data['id']['value']
            dob = data['dob']['date']
            gender = data['gender']
            email = data['email']
            phone = data['phone']
            cell = data['cell']
            username = data['login']['username']
            password = data['login']['password']
            foto = data['picture']['large']
            
         
            texto = f"""<b> 
⭞ FAKE ADDRESS GENERATOR
⤷ FIRST NAME: <code>{first_name}</code>
⤷ LAST NAME: <code>{last_name}</code>
⤷ ADDRESS: <code>{street}</code>
⤷ CITY: <code>{city}</code>
⤷ STATE: <code>{state}</code>
⤷ ZIP: <code>{postcode}</code>
⤷ COUNTRY: <code>{country}</code>
⤷ SSN: <code>{ssn}</code>
⤷ DOB: <code>{dob}</code>
⤷ GENDER: <code>{gender}</code>
⤷ EMAIL: <code>{email}</code>
⤷ PHONE: <code>{phone}</code>
⤷ USERNAME: <code>{username}</code>
⤷ PASSWORD: <code>{password}</code>

</b>"""

            await client.send_video(message.chat.id, foto, texto)

