import pymongo
import time

# Iniciar el temporizador
start_time = time.time()

# Conectar a MongoDB
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ArquitecturaV2"]  # Base de datos ArquitecturaV2
books_col = db["Books"]
authors_col = db["Authors"]

isbn = "0375759778"
query_by_isbn = {"ISBN": isbn}

result_by_isbn = books_col.find_one(query_by_isbn)
if result_by_isbn:
    author_id = result_by_isbn.get("Author-ID")
    
    # Buscar el nombre del autor en base al Author-ID en la colección Authors
    author_query = {"Author-ID": author_id}
    author_result = authors_col.find_one(author_query)

    if author_result:
        author_name = author_result.get("Book-Author")
        print(f"Resultado para el ISBN {isbn}:")
        print(result_by_isbn)
        print(f"Nombre del autor: {author_name}")
    else:
        print(f"No se encontró el autor para el Author-ID {author_id} en la colección Authors.")
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
    file.write(f"Tarea 3 - v2: {execution_time_truncated} segundos\n")