import grpc
from concurrent import futures
import peer_pb2
import peer_pb2_grpc

# Clase que maneja las solicitudes del servidor
class ServerHandler(peer_pb2_grpc.ServerHandlerServicer):
    def procesar_archivos_peer(self, solicitud, contexto):
        print(f"Recibidos archivos de otro peer: {solicitud.file}")
        return peer_pb2.confirmation(status_code="Archivos recibidos")

# Función para iniciar el servidor en un puerto específico
def iniciar_servidor(puerto):
    servidor = grpc.server(futures.ThreadPoolExecutor(max_workers=10))
    peer_pb2_grpc.add_ServerHandlerServicer_to_server(ServerHandler(), servidor)
    servidor.add_insecure_port(f'[::]:{puerto}')
    servidor.start()
    return servidor

