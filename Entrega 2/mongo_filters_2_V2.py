import pymongo
import time

# Establecer conexión con la base de datos
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ArquitecturaV2"]  # Base de datos ArquitecturaV2
books_col = db["Books"]  # Colección Books
authors_col = db["Authors"]  # Colección Authors

def actualizar_nombre_autor_por_ISBN(ISBNs):
    start_time = time.time()  # Iniciar el temporizador al principio de la función
    for ISBN in ISBNs:
        libro = books_col.find_one({"ISBN": ISBN})
        if libro:
            author_id = libro.get("Author-ID")
            autor = authors_col.find_one({"Author-ID": author_id})
            if autor:
                nombre_autor = autor.get("Book-Author")
                autor["Book-Author"] = nombre_autor.upper()
                authors_col.replace_one({"Author-ID": author_id}, autor)
                print(f"Nombre del autor actualizado a mayúsculas para ISBN {ISBN}")
            else:
                print(f"No se encontró el autor correspondiente para el ISBN {ISBN}")
        else:
            print(f"No se encontró ningún libro con el ISBN {ISBN}")
    end_time = time.time()  # Finalizar el temporizador al final de la función
    execution_time = end_time - start_time  # Calcular el tiempo de ejecución
    print(f"Tiempo de ejecución: {execution_time} segundos")  # Imprimir el tiempo de ejecución

    # Truncar el tiempo de ejecución a 5 decimales
    execution_time_truncated = round(execution_time, 5)

    # Guardar el tiempo de ejecución truncado en un archivo
    with open("tiempos_ejecucion.txt", "a") as file:
        file.write(f"Tarea 1 - v2: {execution_time_truncated} segundos\n")

# Llamar a la función con una lista de ISBNs
ISBNs_a_actualizar = ["0195153448", "0002005018"]  # Lista de ISBNs a actualizar
actualizar_nombre_autor_por_ISBN(ISBNs_a_actualizar)


