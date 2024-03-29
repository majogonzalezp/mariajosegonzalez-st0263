# Generated by the gRPC Python protocol compiler plugin. DO NOT EDIT!
"""Client and server classes corresponding to protobuf-defined services."""
import grpc

import peer_pb2 as peer__pb2


class ServerHandlerStub(object):
    """Missing associated documentation comment in .proto file."""

    def __init__(self, channel):
        """Constructor.

        Args:
            channel: A grpc.Channel.
        """
        self.procesar_archivos_peer = channel.unary_unary(
                '/ServerHandler/procesar_archivos_peer',
                request_serializer=peer__pb2.listFilesSended.SerializeToString,
                response_deserializer=peer__pb2.confirmation.FromString,
                )


class ServerHandlerServicer(object):
    """Missing associated documentation comment in .proto file."""

    def procesar_archivos_peer(self, request, context):
        """Missing associated documentation comment in .proto file."""
        context.set_code(grpc.StatusCode.UNIMPLEMENTED)
        context.set_details('Method not implemented!')
        raise NotImplementedError('Method not implemented!')


def add_ServerHandlerServicer_to_server(servicer, server):
    rpc_method_handlers = {
            'procesar_archivos_peer': grpc.unary_unary_rpc_method_handler(
                    servicer.procesar_archivos_peer,
                    request_deserializer=peer__pb2.listFilesSended.FromString,
                    response_serializer=peer__pb2.confirmation.SerializeToString,
            ),
    }
    generic_handler = grpc.method_handlers_generic_handler(
            'ServerHandler', rpc_method_handlers)
    server.add_generic_rpc_handlers((generic_handler,))


 # This class is part of an EXPERIMENTAL API.
class ServerHandler(object):
    """Missing associated documentation comment in .proto file."""

    @staticmethod
    def procesar_archivos_peer(request,
            target,
            options=(),
            channel_credentials=None,
            call_credentials=None,
            insecure=False,
            compression=None,
            wait_for_ready=None,
            timeout=None,
            metadata=None):
        return grpc.experimental.unary_unary(request, target, '/ServerHandler/procesar_archivos_peer',
            peer__pb2.listFilesSended.SerializeToString,
            peer__pb2.confirmation.FromString,
            options, channel_credentials,
            insecure, call_credentials, compression, wait_for_ready, timeout, metadata)
