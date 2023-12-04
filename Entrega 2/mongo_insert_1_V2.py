import pymongo
import pandas as pd
import time

# Iniciar el temporizador
start_time = time.time()


# Lee los archivos CSV de libros y autores
df_books = pd.read_csv("data/booksV2.csv")
df_authors = pd.read_csv("data/authorsV2.csv")

# Obtén los primeros 1000 registros de cada DataFrame para insertar en MongoDB
df_books_subset = df_books.head(1000)
df_authors_subset = df_authors.head(1000)

# Conectar a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")  # Reemplaza con tu URL de conexión si es diferente
db = client["ArquitecturaV2"]  # Nombre de la base de datos

# Colección de libros
collection_books = db["Books"]  # Colección para libros
collection_authors = db["Authors"]  # Colección para autores

# Convertir los DataFrames a listas de diccionarios para facilitar la inserción en MongoDB
data_books_to_insert = df_books_subset.to_dict(orient='records')
data_authors_to_insert = df_authors_subset.to_dict(orient='records')

# Insertar los datos en las colecciones de MongoDB
collection_books.insert_many(data_books_to_insert)
collection_authors.insert_many(data_authors_to_insert)

print("Datos de libros y autores insertados en MongoDB")

# Calcular el tiempo de ejecución
end_time = time.time()
execution_time = end_time - start_time
print(f"\nTiempo de ejecución: {execution_time} segundos")

# Truncar el tiempo de ejecución a 5 decimales
execution_time_truncated = round(execution_time, 5)

# Guardar el tiempo de ejecución truncado en un archivo
with open("tiempos_ejecucion.txt", "a") as file:
    file.write(f"Insert - v2: {execution_time_truncated} segundos\n")