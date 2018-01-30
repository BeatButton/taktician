# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: tak/proto/taktician.proto

import sys
_b=sys.version_info[0]<3 and (lambda x:x) or (lambda x:x.encode('latin1'))
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import symbol_database as _symbol_database
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)

_sym_db = _symbol_database.Default()




DESCRIPTOR = _descriptor.FileDescriptor(
  name='tak/proto/taktician.proto',
  package='tak.proto',
  syntax='proto3',
  serialized_pb=_b('\n\x19tak/proto/taktician.proto\x12\ttak.proto\"B\n\x0e\x41nalyzeRequest\x12\x10\n\x08position\x18\x01 \x01(\t\x12\r\n\x05\x64\x65pth\x18\x02 \x01(\x05\x12\x0f\n\x07precise\x18\x03 \x01(\x08\";\n\x0f\x41nalyzeResponse\x12\n\n\x02pv\x18\x01 \x03(\t\x12\r\n\x05value\x18\x02 \x01(\x03\x12\r\n\x05\x64\x65pth\x18\x03 \x01(\x05\"2\n\x13\x43\x61nonicalizeRequest\x12\x0c\n\x04size\x18\x01 \x01(\x05\x12\r\n\x05moves\x18\x02 \x03(\t\"%\n\x14\x43\x61nonicalizeResponse\x12\r\n\x05moves\x18\x01 \x03(\t2\xa2\x01\n\tTaktician\x12\x42\n\x07\x41nalyze\x12\x19.tak.proto.AnalyzeRequest\x1a\x1a.tak.proto.AnalyzeResponse\"\x00\x12Q\n\x0c\x43\x61nonicalize\x12\x1e.tak.proto.CanonicalizeRequest\x1a\x1f.tak.proto.CanonicalizeResponse\"\x00\x42\x04Z\x02pbb\x06proto3')
)




_ANALYZEREQUEST = _descriptor.Descriptor(
  name='AnalyzeRequest',
  full_name='tak.proto.AnalyzeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='position', full_name='tak.proto.AnalyzeRequest.position', index=0,
      number=1, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=_b("").decode('utf-8'),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth', full_name='tak.proto.AnalyzeRequest.depth', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='precise', full_name='tak.proto.AnalyzeRequest.precise', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=40,
  serialized_end=106,
)


_ANALYZERESPONSE = _descriptor.Descriptor(
  name='AnalyzeResponse',
  full_name='tak.proto.AnalyzeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='pv', full_name='tak.proto.AnalyzeResponse.pv', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='value', full_name='tak.proto.AnalyzeResponse.value', index=1,
      number=2, type=3, cpp_type=2, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='depth', full_name='tak.proto.AnalyzeResponse.depth', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=108,
  serialized_end=167,
)


_CANONICALIZEREQUEST = _descriptor.Descriptor(
  name='CanonicalizeRequest',
  full_name='tak.proto.CanonicalizeRequest',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='size', full_name='tak.proto.CanonicalizeRequest.size', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
    _descriptor.FieldDescriptor(
      name='moves', full_name='tak.proto.CanonicalizeRequest.moves', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=169,
  serialized_end=219,
)


_CANONICALIZERESPONSE = _descriptor.Descriptor(
  name='CanonicalizeResponse',
  full_name='tak.proto.CanonicalizeResponse',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='moves', full_name='tak.proto.CanonicalizeResponse.moves', index=0,
      number=1, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None, file=DESCRIPTOR),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  syntax='proto3',
  extension_ranges=[],
  oneofs=[
  ],
  serialized_start=221,
  serialized_end=258,
)

DESCRIPTOR.message_types_by_name['AnalyzeRequest'] = _ANALYZEREQUEST
DESCRIPTOR.message_types_by_name['AnalyzeResponse'] = _ANALYZERESPONSE
DESCRIPTOR.message_types_by_name['CanonicalizeRequest'] = _CANONICALIZEREQUEST
DESCRIPTOR.message_types_by_name['CanonicalizeResponse'] = _CANONICALIZERESPONSE
_sym_db.RegisterFileDescriptor(DESCRIPTOR)

AnalyzeRequest = _reflection.GeneratedProtocolMessageType('AnalyzeRequest', (_message.Message,), dict(
  DESCRIPTOR = _ANALYZEREQUEST,
  __module__ = 'tak.proto.taktician_pb2'
  # @@protoc_insertion_point(class_scope:tak.proto.AnalyzeRequest)
  ))
_sym_db.RegisterMessage(AnalyzeRequest)

AnalyzeResponse = _reflection.GeneratedProtocolMessageType('AnalyzeResponse', (_message.Message,), dict(
  DESCRIPTOR = _ANALYZERESPONSE,
  __module__ = 'tak.proto.taktician_pb2'
  # @@protoc_insertion_point(class_scope:tak.proto.AnalyzeResponse)
  ))
_sym_db.RegisterMessage(AnalyzeResponse)

CanonicalizeRequest = _reflection.GeneratedProtocolMessageType('CanonicalizeRequest', (_message.Message,), dict(
  DESCRIPTOR = _CANONICALIZEREQUEST,
  __module__ = 'tak.proto.taktician_pb2'
  # @@protoc_insertion_point(class_scope:tak.proto.CanonicalizeRequest)
  ))
_sym_db.RegisterMessage(CanonicalizeRequest)

CanonicalizeResponse = _reflection.GeneratedProtocolMessageType('CanonicalizeResponse', (_message.Message,), dict(
  DESCRIPTOR = _CANONICALIZERESPONSE,
  __module__ = 'tak.proto.taktician_pb2'
  # @@protoc_insertion_point(class_scope:tak.proto.CanonicalizeResponse)
  ))
_sym_db.RegisterMessage(CanonicalizeResponse)


DESCRIPTOR.has_options = True
DESCRIPTOR._options = _descriptor._ParseOptions(descriptor_pb2.FileOptions(), _b('Z\002pb'))

_TAKTICIAN = _descriptor.ServiceDescriptor(
  name='Taktician',
  full_name='tak.proto.Taktician',
  file=DESCRIPTOR,
  index=0,
  options=None,
  serialized_start=261,
  serialized_end=423,
  methods=[
  _descriptor.MethodDescriptor(
    name='Analyze',
    full_name='tak.proto.Taktician.Analyze',
    index=0,
    containing_service=None,
    input_type=_ANALYZEREQUEST,
    output_type=_ANALYZERESPONSE,
    options=None,
  ),
  _descriptor.MethodDescriptor(
    name='Canonicalize',
    full_name='tak.proto.Taktician.Canonicalize',
    index=1,
    containing_service=None,
    input_type=_CANONICALIZEREQUEST,
    output_type=_CANONICALIZERESPONSE,
    options=None,
  ),
])
_sym_db.RegisterServiceDescriptor(_TAKTICIAN)

DESCRIPTOR.services_by_name['Taktician'] = _TAKTICIAN

# @@protoc_insertion_point(module_scope)
