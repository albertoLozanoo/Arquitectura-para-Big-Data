import pymongo
import time

# Iniciar el temporizador
start_time = time.time()

# Conectar a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Arquitectura"]
collection = db["Books"]

# ii. Filtrando que el título de su obra empiece por “The…..”
author_name = "Gina Bari Kolata"
title_starts_with = "The"
query_by_author_and_title = {
    "Book-Author": author_name,
    "Book-Title": { "$regex": f"^{title_starts_with}", "$options": "i" }
}

results_author_title = list(collection.find(query_by_author_and_title))
print(f"\nResultados para el autor {author_name} con título que comienza por '{title_starts_with}':")
for doc in results_author_title:
    print(doc)

# Calcular el tiempo de ejecución
end_time = time.time()
execution_time = end_time - start_time
print(f"\nTiempo de ejecución: {execution_time} segundos")

# Truncar el tiempo de ejecución a 5 decimales
execution_time_truncated = round(execution_time, 5)

# Guardar el tiempo de ejecución truncado en un archivo
with open("tiempos_ejecucion.txt", "a") as file:
    file.write(f"Tarea 2.2 - v1: {execution_time_truncated} segundos\n")