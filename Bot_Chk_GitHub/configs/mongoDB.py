from pymongo.mongo_client import MongoClient
from pymongo.server_api import ServerApi

# Instalar la libreria de mongo con el siguiente comando: pip install pymongo

uri = "TU_CLUSTER"
# Este bot para añadir a sus usuarios usa de la data base de mongoDB. luego de crear tu cuenta y crear tu CLUSTER
# Ingresa Aqui la URL del cluster

client = MongoClient(uri, server_api=ServerApi('1'))

database = client['users']
collection = database['usuarios']
collection_dos = database['keys']
collection_tres = database['group']
collection_cuatro = database['ban']

try:
    client.admin.command('ping')
    print("Conexion con MongoDB Exitosa!")
except Exception as e:
    print(e)

