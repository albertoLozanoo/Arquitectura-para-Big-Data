import pymongo
import time

# Establecer conexión con la base de datos
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ArquitecturaV2"]  # Base de datos ArquitecturaV2
books_col = db["Books"]  # Colección Books
authors_col = db["Authors"]  # Colección Authors

def buscar_libros_por_autor_y_titulo(nombre_autor, inicio_titulo):
    # Iniciar el temporizador
    start_time = time.time()
    # Buscar el documento del autor por su nombre
    autor = authors_col.find_one({"Book-Author": nombre_autor})
    if autor:
        author_id = autor.get("Author-ID")

        # Consulta para obtener las publicaciones del autor con título que empiece por "The"
        libros_autor_titulo = books_col.find({
            "Author-ID": author_id,
            "Book-Title": {"$regex": f"^{inicio_titulo}", "$options": "i"}
        })

        # Mostrar las publicaciones del autor con títulos que comiencen con "The"
        print(f"Publicaciones del autor {nombre_autor} con títulos que comienzan con '{inicio_titulo}':")
        for libro in libros_autor_titulo:
            print(libro)  # Puedes realizar acciones con los libros encontrados
    else:
        print(f"No se encontró al autor {nombre_autor} en la base de datos.")

    # Calcular el tiempo de ejecución
    end_time = time.time()
    execution_time = end_time - start_time
    print(f"\nTiempo de ejecución: {execution_time} segundos")

    # Truncar el tiempo de ejecución a 5 decimales
    execution_time_truncated = round(execution_time, 5)

    # Guardar el tiempo de ejecución truncado en un archivo
    with open("tiempos_ejecucion.txt", "a") as file:
        file.write(f"Tarea 2.2 - v2: {execution_time_truncated} segundos\n")

# Nombre del autor y título inicial a buscar
nombre_autor_a_buscar = "Amy Tan"  # Reemplaza con el nombre del autor deseado
titulo_a_buscar = "The"  # Reemplaza con la palabra inicial del título deseado
buscar_libros_por_autor_y_titulo(nombre_autor_a_buscar, titulo_a_buscar)

