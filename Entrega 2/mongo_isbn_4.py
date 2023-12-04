import pymongo
import time

# Iniciar el temporizador
start_time = time.time()

# Conectar a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["Arquitectura"]
collection = db["Books"]

isbn = "0375759778"
query_by_isbn = { "ISBN": isbn }

result_by_isbn = collection.find_one(query_by_isbn)
if result_by_isbn:
    print(f"Resultado para el ISBN {isbn}:")
    print(result_by_isbn)
else:
    print(f"No se encontraron resultados para el ISBN {isbn}.")

# Calcular el tiempo de ejecución
end_time = time.time()
execution_time = end_time - start_time
print(f"\nTiempo de ejecución: {execution_time} segundos")

# Truncar el tiempo de ejecución a 5 decimales
execution_time_truncated = round(execution_time, 5)

# Guardar el tiempo de ejecución truncado en un archivo
with open("tiempos_ejecucion.txt", "a") as file:
    file.write(f"Tarea 3 - v1: {execution_time_truncated} segundos\n")

