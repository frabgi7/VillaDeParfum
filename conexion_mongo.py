from pymongo import MongoClient

# Conectar al servidor local
client = MongoClient("mongodb://localhost:27017/")

# 1. Imprimir todas las bases de datos que existen en tu MongoDB
print("Bases de datos disponibles:", client.list_database_names())

# 2. Conectar a la base de datos (prueba con el nombre exacto que veas arriba)
db = client["VillaDeParfum"]  # O "villa_de_parfum"

# 3. Imprimir las colecciones que hay dentro de esa base de datos
print("Colecciones en la base de datos:", db.list_collection_names())

# 4. Contar cuántos documentos hay en clientes
print(
    "Cantidad de documentos en clientes:", db["Clientes"].count_documents({})
)