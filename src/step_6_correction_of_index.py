from collections import defaultdict

# Ruta del archivo de entrada y salida
ruta_archivo = '/home/guest/PycharmProjects/ancestral_states_proteins/src/residues_modified.fasta'
ruta_archivo_corregido = 'NR99.93j7vG_residues_modified_corregido.fasta'

# Leer el contenido del archivo
with open(ruta_archivo, 'r', encoding='utf-8') as file:
    contenido = file.readlines()

# Diccionario para contar los nombres de secuencias
secuencia_count = defaultdict(int)

# Lista para almacenar el contenido corregido
contenido_corregido = []

# Procesar cada línea del archivo
for linea in contenido:
    if linea.startswith('>'):
        nombre_secuencia = linea.strip()
        secuencia_count[nombre_secuencia] += 1
        if secuencia_count[nombre_secuencia] > 1:
            # Añadir un sufijo único al nombre de la secuencia duplicada
            nombre_secuencia += f"_{secuencia_count[nombre_secuencia]}"
        contenido_corregido.append(nombre_secuencia + '\n')
    else:
        contenido_corregido.append(linea)

# Guardar el contenido corregido en un nuevo archivo
with open(ruta_archivo_corregido, 'w', encoding='utf-8') as file:
    file.writelines(contenido_corregido)
