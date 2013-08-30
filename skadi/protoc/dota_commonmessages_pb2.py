# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dota_commonmessages.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import google.protobuf.descriptor_pb2
import networkbasetypes_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dota_commonmessages.proto',
  package='',
  serialized_pb='\n\x19\x64ota_commonmessages.proto\x1a google/protobuf/descriptor.proto\x1a\x16networkbasetypes.proto\"`\n\x15\x43\x44OTAMsg_LocationPing\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\x0e\n\x06target\x18\x03 \x01(\x05\x12\x13\n\x0b\x64irect_ping\x18\x04 \x01(\x08\x12\x0c\n\x04type\x18\x05 \x01(\x05\":\n\x12\x43\x44OTAMsg_ItemAlert\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\x0e\n\x06itemid\x18\x03 \x01(\x05\"9\n\x10\x43\x44OTAMsg_MapLine\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\x0f\n\x07initial\x18\x03 \x01(\x08\"S\n\x12\x43\x44OTAMsg_WorldLine\x12\t\n\x01x\x18\x01 \x01(\x05\x12\t\n\x01y\x18\x02 \x01(\x05\x12\t\n\x01z\x18\x03 \x01(\x05\x12\x0f\n\x07initial\x18\x04 \x01(\x08\x12\x0b\n\x03\x65nd\x18\x05 \x01(\x08\"~\n\x16\x43\x44OTAMsg_SendStatPopup\x12\x39\n\x05style\x18\x01 \x01(\x0e\x32\x14.EDOTAStatPopupTypes:\x14k_EDOTA_SPT_Textline\x12\x14\n\x0cstat_strings\x18\x02 \x03(\t\x12\x13\n\x0bstat_images\x18\x03 \x03(\x05*\xb7\x02\n\x15\x45\x44OTAChatWheelMessage\x12\x11\n\rk_EDOTA_CW_Ok\x10\x00\x12\x13\n\x0fk_EDOTA_CW_Care\x10\x01\x12\x16\n\x12k_EDOTA_CW_GetBack\x10\x02\x12\x18\n\x14k_EDOTA_CW_NeedWards\x10\x03\x12\x13\n\x0fk_EDOTA_CW_Stun\x10\x04\x12\x13\n\x0fk_EDOTA_CW_Help\x10\x05\x12\x13\n\x0fk_EDOTA_CW_Push\x10\x06\x12\x16\n\x12k_EDOTA_CW_GoodJob\x10\x07\x12\x16\n\x12k_EDOTA_CW_Missing\x10\x08\x12\x1a\n\x16k_EDOTA_CW_Missing_Top\x10\t\x12\x1a\n\x16k_EDOTA_CW_Missing_Mid\x10\n\x12\x1d\n\x19k_EDOTA_CW_Missing_Bottom\x10\x0b*\\\n\x13\x45\x44OTAStatPopupTypes\x12\x18\n\x14k_EDOTA_SPT_Textline\x10\x00\x12\x15\n\x11k_EDOTA_SPT_Basic\x10\x01\x12\x14\n\x10k_EDOTA_SPT_Poll\x10\x02')

_EDOTACHATWHEELMESSAGE = _descriptor.EnumDescriptor(
  name='EDOTAChatWheelMessage',
  full_name='EDOTAChatWheelMessage',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='k_EDOTA_CW_Ok', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTA_CW_Care', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTA_CW_GetBack', index=2, number=2,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTA_CW_NeedWards', index=3, number=3,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTA_CW_Stun', index=4, number=4,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTA_CW_Help', index=5, number=5,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTA_CW_Push', index=6, number=6,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTA_CW_GoodJob', index=7, number=7,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTA_CW_Missing', index=8, number=8,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTA_CW_Missing_Top', index=9, number=9,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTA_CW_Missing_Mid', index=10, number=10,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTA_CW_Missing_Bottom', index=11, number=11,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=518,
  serialized_end=829,
)

EDOTAChatWheelMessage = enum_type_wrapper.EnumTypeWrapper(_EDOTACHATWHEELMESSAGE)
_EDOTASTATPOPUPTYPES = _descriptor.EnumDescriptor(
  name='EDOTAStatPopupTypes',
  full_name='EDOTAStatPopupTypes',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='k_EDOTA_SPT_Textline', index=0, number=0,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTA_SPT_Basic', index=1, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='k_EDOTA_SPT_Poll', index=2, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=831,
  serialized_end=923,
)

EDOTAStatPopupTypes = enum_type_wrapper.EnumTypeWrapper(_EDOTASTATPOPUPTYPES)
k_EDOTA_CW_Ok = 0
k_EDOTA_CW_Care = 1
k_EDOTA_CW_GetBack = 2
k_EDOTA_CW_NeedWards = 3
k_EDOTA_CW_Stun = 4
k_EDOTA_CW_Help = 5
k_EDOTA_CW_Push = 6
k_EDOTA_CW_GoodJob = 7
k_EDOTA_CW_Missing = 8
k_EDOTA_CW_Missing_Top = 9
k_EDOTA_CW_Missing_Mid = 10
k_EDOTA_CW_Missing_Bottom = 11
k_EDOTA_SPT_Textline = 0
k_EDOTA_SPT_Basic = 1
k_EDOTA_SPT_Poll = 2



_CDOTAMSG_LOCATIONPING = _descriptor.Descriptor(
  name='CDOTAMsg_LocationPing',
  full_name='CDOTAMsg_LocationPing',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='CDOTAMsg_LocationPing.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='CDOTAMsg_LocationPing.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='target', full_name='CDOTAMsg_LocationPing.target', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='direct_ping', full_name='CDOTAMsg_LocationPing.direct_ping', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='type', full_name='CDOTAMsg_LocationPing.type', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=87,
  serialized_end=183,
)


_CDOTAMSG_ITEMALERT = _descriptor.Descriptor(
  name='CDOTAMsg_ItemAlert',
  full_name='CDOTAMsg_ItemAlert',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='CDOTAMsg_ItemAlert.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='CDOTAMsg_ItemAlert.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='itemid', full_name='CDOTAMsg_ItemAlert.itemid', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=185,
  serialized_end=243,
)


_CDOTAMSG_MAPLINE = _descriptor.Descriptor(
  name='CDOTAMsg_MapLine',
  full_name='CDOTAMsg_MapLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='CDOTAMsg_MapLine.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='CDOTAMsg_MapLine.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initial', full_name='CDOTAMsg_MapLine.initial', index=2,
      number=3, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=245,
  serialized_end=302,
)


_CDOTAMSG_WORLDLINE = _descriptor.Descriptor(
  name='CDOTAMsg_WorldLine',
  full_name='CDOTAMsg_WorldLine',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='x', full_name='CDOTAMsg_WorldLine.x', index=0,
      number=1, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='y', full_name='CDOTAMsg_WorldLine.y', index=1,
      number=2, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='z', full_name='CDOTAMsg_WorldLine.z', index=2,
      number=3, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='initial', full_name='CDOTAMsg_WorldLine.initial', index=3,
      number=4, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='end', full_name='CDOTAMsg_WorldLine.end', index=4,
      number=5, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=304,
  serialized_end=387,
)


_CDOTAMSG_SENDSTATPOPUP = _descriptor.Descriptor(
  name='CDOTAMsg_SendStatPopup',
  full_name='CDOTAMsg_SendStatPopup',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='style', full_name='CDOTAMsg_SendStatPopup.style', index=0,
      number=1, type=14, cpp_type=8, label=1,
      has_default_value=True, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stat_strings', full_name='CDOTAMsg_SendStatPopup.stat_strings', index=1,
      number=2, type=9, cpp_type=9, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stat_images', full_name='CDOTAMsg_SendStatPopup.stat_images', index=2,
      number=3, type=5, cpp_type=1, label=3,
      has_default_value=False, default_value=[],
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
  ],
  extensions=[
  ],
  nested_types=[],
  enum_types=[
  ],
  options=None,
  is_extendable=False,
  extension_ranges=[],
  serialized_start=389,
  serialized_end=515,
)

_CDOTAMSG_SENDSTATPOPUP.fields_by_name['style'].enum_type = _EDOTASTATPOPUPTYPES
DESCRIPTOR.message_types_by_name['CDOTAMsg_LocationPing'] = _CDOTAMSG_LOCATIONPING
DESCRIPTOR.message_types_by_name['CDOTAMsg_ItemAlert'] = _CDOTAMSG_ITEMALERT
DESCRIPTOR.message_types_by_name['CDOTAMsg_MapLine'] = _CDOTAMSG_MAPLINE
DESCRIPTOR.message_types_by_name['CDOTAMsg_WorldLine'] = _CDOTAMSG_WORLDLINE
DESCRIPTOR.message_types_by_name['CDOTAMsg_SendStatPopup'] = _CDOTAMSG_SENDSTATPOPUP

class CDOTAMsg_LocationPing(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDOTAMSG_LOCATIONPING

  # @@protoc_insertion_point(class_scope:CDOTAMsg_LocationPing)

class CDOTAMsg_ItemAlert(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDOTAMSG_ITEMALERT

  # @@protoc_insertion_point(class_scope:CDOTAMsg_ItemAlert)

class CDOTAMsg_MapLine(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDOTAMSG_MAPLINE

  # @@protoc_insertion_point(class_scope:CDOTAMsg_MapLine)

class CDOTAMsg_WorldLine(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDOTAMSG_WORLDLINE

  # @@protoc_insertion_point(class_scope:CDOTAMsg_WorldLine)

class CDOTAMsg_SendStatPopup(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDOTAMSG_SENDSTATPOPUP

  # @@protoc_insertion_point(class_scope:CDOTAMsg_SendStatPopup)


# @@protoc_insertion_point(module_scope)
