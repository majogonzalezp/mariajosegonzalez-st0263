import time
from server import iniciar_servidor
from client import transmitirArchivosSeleccionados
from file_management import seleccionar_archivos

PUERTO_SERVIDOR = 8000
PUERTO_DESTINO = 9000

def ejecutar_main():
    servidor = iniciar_servidor(PUERTO_SERVIDOR)
    print(f"Servidor activo en puerto {PUERTO_SERVIDOR}")

    # Funcionalidad del cliente
    time.sleep(2)
    archivos_usuario = seleccionar_archivos()
    try:
        time.sleep(10)
        transmitirArchivosSeleccionados(archivos_usuario, f'localhost:{PUERTO_DESTINO}')
        time.sleep(10)
    except KeyboardInterrupt:
        print("Interrupción por usuario, servidor detenido")


if __name__ == '__main__':
    ejecutar_main()


