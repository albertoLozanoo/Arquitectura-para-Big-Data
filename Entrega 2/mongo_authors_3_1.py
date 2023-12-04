import pymongo
import time

# Iniciar el temporizador
start_time = time.time()

# Conectar a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Arquitectura"]
collection = db["Books"]


# i. Filtrando por el año de publicación mayor de 2020
author_name = "Gina Bari Kolata"
publication_year = 1990
query_by_author_and_year = {
    "Book-Author": author_name,
    "Year-Of-Publication": { "$gt": publication_year }
}

results_author_year = list(collection.find(query_by_author_and_year))
print(f"Resultados para el autor {author_name} con año de publicación mayor a {publication_year}:")
for doc in results_author_year:
    print(doc)

# Calcular el tiempo de ejecución
end_time = time.time()
execution_time = end_time - start_time
print(f"\nTiempo de ejecución: {execution_time} segundos")

# Truncar el tiempo de ejecución a 5 decimales
execution_time_truncated = round(execution_time, 5)

# Guardar el tiempo de ejecución truncado en un archivo
with open("tiempos_ejecucion.txt", "a") as file:
    file.write(f"Tarea 2.1 - v1: {execution_time_truncated} segundos\n")