import pandas as pd

# Lee los primeros 10,000 registros del archivo CSV
df = pd.read_csv("data/books.csv", nrows=1000)

# Eliminar las columnas especificadas del DataFrame 'df'
columns = ['Publisher', 'Image-URL-S', 'Image-URL-M', 'Image-URL-L']
df.drop(columns=columns, axis=1, inplace=True)

# Crear un diccionario para asignar IDs a autores únicos
author_ids = {}
current_id = 1

for author in df['Book-Author'].unique():
    if author not in author_ids:
        author_ids[author] = current_id
        current_id += 1

df['Author-ID'] = df['Book-Author'].map(author_ids)

# Reordenar las columnas según el orden deseado
column_order = ['ISBN', 'Book-Title', 'Year-Of-Publication', 'Author-ID', 'Book-Author']
df = df.reindex(columns=column_order)

#Exportar csv
df.to_csv('/data/books_final2.csv', index=False)
