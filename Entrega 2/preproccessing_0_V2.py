import pandas as pd

# Lee los primeros 10,000 registros del archivo CSV
df = pd.read_csv("/content/books_final.csv", nrows=1000)

# Crear un nuevo DataFrame con las columnas especificadas
nuevo_df = df[['Author-ID', 'Book-Author']]

# Eliminar la columna 'Author'
df.drop('Book-Author', axis=1, inplace=True)

# Eliminar filas duplicadas basadas en la columna 'Author-ID'
nuevo_df = nuevo_df.drop_duplicates(subset=['Author-ID'])

nuevo_df.to_csv('/content/authorsV2.csv', index=False)

df.to_csv('/content/booksV2.csv', index=False)