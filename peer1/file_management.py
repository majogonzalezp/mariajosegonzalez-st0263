import os
import requests

# Directorio desde el cual se servirán los archivos
DIRECTORIO_SERVIDOR = os.path.expanduser('./')

# Función para seleccionar archivos de manera interactiva
def elegir_archivos_interactivamente(archivos_disponibles):
    indices_seleccionados = []
    print("Listado de archivos disponibles:")
    for indice, archivo in enumerate(archivos_disponibles):
        print(f"{indice + 1}. {archivo}")

    print("Selecciona un archivo escribiendo su número y termina con 'finalizar'.")
    while True:
        eleccion = input("Elige un archivo (o 'finalizar' para concluir): ")
        if eleccion == 'finalizar':
            break
        else:
            try:
                indice_archivo = int(eleccion) - 1
                if 0 <= indice_archivo < len(archivos_disponibles):
                    indices_seleccionados.append(indice_archivo + 1)
                else:
                    print("Número de archivo no válido.")
            except ValueError:
                print("Introduce un número válido por favor.")
    
    return indices_seleccionados

# Función para listar archivos en un directorio
def listar_archivos_en_directorio(directorio):
    return [archivo for archivo in os.listdir(directorio) if os.path.isfile(os.path.join(directorio, archivo))]

# Función principal para seleccionar archivos
def seleccionar_archivos():
    archivos = listar_archivos_en_directorio(DIRECTORIO_SERVIDOR)
    indices_seleccionados = elegir_archivos_interactivamente(archivos)
    respuesta = requests.post('http://localhost:4000/elegir_archivos', json={"archivos": archivos, "indicesSeleccionados": indices_seleccionados})
    archivos_seleccionados = respuesta.json()['archivosElegidos']
    print("Archivos seleccionados:", archivos_seleccionados)
    return archivos_seleccionados


