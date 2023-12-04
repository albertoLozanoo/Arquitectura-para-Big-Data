import pymongo
import time



# Establecer conexión con la base de datos
client = pymongo.MongoClient("mongodb://localhost:27017/")
db = client["ArquitecturaV2"]  # Base de datos ArquitecturaV2
books_col = db["Books"]  # Colección Books
authors_col = db["Authors"]  # Colección Authors

def buscar_obras_por_autor_y_fecha_publicacion(nombre_autor):
    # Iniciar el temporizador
    start_time = time.time()
    # Buscar el documento del autor por su nombre
    autor = authors_col.find_one({"Book-Author": nombre_autor})
    if autor:
        author_id = autor.get("Author-ID")

        # Consulta para obtener las publicaciones del autor después de 1990
        publicaciones_autor = books_col.find({
            "Author-ID": author_id,
            "Year-Of-Publication": {"$gt": 1990}
        })

        # Mostrar las publicaciones del autor después de 1990
        print(f"Publicaciones del autor {nombre_autor} después de 1990:")
        for publicacion in publicaciones_autor:
            print(publicacion)  # Aquí puedes realizar alguna acción con las publicaciones

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
        file.write(f"Tarea 2.1 - v2: {execution_time_truncated} segundos\n")

# Nombre del autor a buscar sus obras publicadas después de 1990
nombre_autor_a_buscar = "MARK P. O. MORFORD"  # Reemplaza con el nombre del autor deseado
buscar_obras_por_autor_y_fecha_publicacion(nombre_autor_a_buscar)

