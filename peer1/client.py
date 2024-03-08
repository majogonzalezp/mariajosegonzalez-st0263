import grpc
import peer_pb2
import peer_pb2_grpc

# Función para enviar una lista de archivos a un nodo objetivo en la red P2P
def transmitirArchivosSeleccionados(listaArchivos, destino):
    conexion = grpc.insecure_channel(destino)
    controlador = peer_pb2_grpc.ServerHandlerStub(conexion)
    respuesta = controlador.procesar_archivos_peer(peer_pb2.listFilesSended(file=listaArchivos))
    print(f"Respuesta del servidor: {respuesta.status_code}")


