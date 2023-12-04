import pymongo
import pandas as pd
import time

# Iniciar el temporizador
start_time = time.time()

# Lee el archivo CSV
df = pd.read_csv("data/books_final.csv")

# Obtén los primeros 1000 registros del DataFrame para insertarlos en MongoDB
df_subset = df.head(1000)

# Conectar a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Reemplaza con tu URL de conexión si es diferente
db = client["Arquitectura"]  # Nombre de la base de datos
collection = db["Books"]  # Nombre de la colección

# Convierte el DataFrame a una lista de diccionarios para facilitar la inserción en MongoDB
data_to_insert = df_subset.to_dict(orient='records')

# Inserta los datos en la colección de MongoDB
collection.insert_many(data_to_insert)

print("Datos insertados en MongoDB")

# Calcular el tiempo de ejecución
end_time = time.time()
execution_time = end_time - start_time
print(f"\nTiempo de ejecución: {execution_time} segundos")

# Truncar el tiempo de ejecución a 5 decimales
execution_time_truncated = round(execution_time, 5)

# Guardar el tiempo de ejecución truncado en un archivo
with open("tiempos_ejecucion.txt", "a") as file:
    file.write(f"Insert - v1: {execution_time_truncated} segundos\n")