# Generated by the protocol buffer compiler.  DO NOT EDIT!

from google.protobuf import descriptor
from rpcz import service
from rpcz import service_reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import run_recognition_pb2
import graspable_object_pb2


_OBJECTRECOGNITIONSERVICE = descriptor.ServiceDescriptor(
  name='ObjectRecognitionService',
  full_name='graspit_rpcz.ObjectRecognitionService',
  file=run_recognition_pb2.DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=160,
  serialized_end=274,
  methods=[
  descriptor.MethodDescriptor(
    name='run',
    full_name='graspit_rpcz.ObjectRecognitionService.run',
    index=0,
    containing_service=None,
    input_type=run_recognition_pb2._OBJECTRECOGNITIONREQUEST,
    output_type=run_recognition_pb2._OBJECTRECOGNITIONRESPONSE,
    options=None,
  ),
])

class ObjectRecognitionService(service.Service):
  __metaclass__ = service_reflection.GeneratedServiceType
  DESCRIPTOR = _OBJECTRECOGNITIONSERVICE
class ObjectRecognitionService_Stub(ObjectRecognitionService):
  __metaclass__ = service_reflection.GeneratedServiceStubType
  DESCRIPTOR = _OBJECTRECOGNITIONSERVICE
