import pymongo
import time

# Conectar a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Arquitectura"]
collection = db["Books"]

# Iniciar el temporizador
start_time = time.time()

# Buscar los dos registros específicos que deseas modificar
before_update_query = { "ISBN": { "$in": ["0195153448", "0002005018"] } }
before_update_results = list(collection.find(before_update_query))

# Imprimir el estado antes de la modificación
print("Estado antes de la modificación:")
for doc in before_update_results:
    print("Antes:", doc)

# Actualizar los registros y convertir 'Book-Author' a mayúsculas
update_query = { "ISBN": { "$in": ["0195153448", "0195153448"] } }
update = [
    {
        "$set": {
            "Book-Author": { "$toUpper": "$Book-Author" }
        }
    }
]
collection.update_many(update_query, update)

# Buscar los registros actualizados
after_update_results = list(collection.find(before_update_query))

# Imprimir el estado después de la modificación
print("\nEstado después de la modificación:")
for doc in after_update_results:
    print("Después:", doc)

# Calcular el tiempo de ejecución
end_time = time.time()
execution_time = end_time - start_time
print(f"\nTiempo de ejecución: {execution_time} segundos")

# Truncar el tiempo de ejecución a 5 decimales
execution_time_truncated = round(execution_time, 5)

# Guardar el tiempo de ejecución truncado en un archivo
with open("tiempos_ejecucion.txt", "a") as file:
    file.write(f"Tarea 1 - v1: {execution_time_truncated} segundos\n")
