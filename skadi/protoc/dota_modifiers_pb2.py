# Generated by the protocol buffer compiler.  DO NOT EDIT!
# source: dota_modifiers.proto

from google.protobuf.internal import enum_type_wrapper
from google.protobuf import descriptor as _descriptor
from google.protobuf import message as _message
from google.protobuf import reflection as _reflection
from google.protobuf import descriptor_pb2
# @@protoc_insertion_point(imports)


import google.protobuf.descriptor_pb2
import networkbasetypes_pb2


DESCRIPTOR = _descriptor.FileDescriptor(
  name='dota_modifiers.proto',
  package='',
  serialized_pb='\n\x14\x64ota_modifiers.proto\x1a google/protobuf/descriptor.proto\x1a\x16networkbasetypes.proto\"\xe4\x04\n\x1b\x43\x44OTAModifierBuffTableEntry\x12N\n\nentry_type\x18\x01 \x02(\x0e\x32\x19.DOTA_MODIFIER_ENTRY_TYPE:\x1f\x44OTA_MODIFIER_ENTRY_TYPE_ACTIVE\x12\x0e\n\x06parent\x18\x02 \x02(\x05\x12\r\n\x05index\x18\x03 \x02(\x05\x12\x12\n\nserial_num\x18\x04 \x02(\x05\x12\x0c\n\x04name\x18\x05 \x01(\x05\x12\x15\n\rability_level\x18\x06 \x01(\x05\x12\x13\n\x0bstack_count\x18\x07 \x01(\x05\x12\x15\n\rcreation_time\x18\x08 \x01(\x02\x12\x14\n\x08\x64uration\x18\t \x01(\x02:\x02-1\x12\x0e\n\x06\x63\x61ster\x18\n \x01(\x05\x12\x0f\n\x07\x61\x62ility\x18\x0b \x01(\x05\x12\r\n\x05\x61rmor\x18\x0c \x01(\x05\x12\x11\n\tfade_time\x18\r \x01(\x02\x12\x0e\n\x06subtle\x18\x0e \x01(\x08\x12\x14\n\x0c\x63hannel_time\x18\x0f \x01(\x02\x12\x1c\n\x07v_start\x18\x10 \x01(\x0b\x32\x0b.CMsgVector\x12\x1a\n\x05v_end\x18\x11 \x01(\x0b\x32\x0b.CMsgVector\x12\x1a\n\x12portal_loop_appear\x18\x12 \x01(\t\x12\x1d\n\x15portal_loop_disappear\x18\x13 \x01(\t\x12\x18\n\x10hero_loop_appear\x18\x14 \x01(\t\x12\x1b\n\x13hero_loop_disappear\x18\x15 \x01(\t\x12\x16\n\x0emovement_speed\x18\x16 \x01(\x05\x12\x0c\n\x04\x61ura\x18\x17 \x01(\x08\x12\x10\n\x08\x61\x63tivity\x18\x18 \x01(\x05\x12\x0e\n\x06\x64\x61mage\x18\x19 \x01(\x05*e\n\x18\x44OTA_MODIFIER_ENTRY_TYPE\x12#\n\x1f\x44OTA_MODIFIER_ENTRY_TYPE_ACTIVE\x10\x01\x12$\n DOTA_MODIFIER_ENTRY_TYPE_REMOVED\x10\x02')

_DOTA_MODIFIER_ENTRY_TYPE = _descriptor.EnumDescriptor(
  name='DOTA_MODIFIER_ENTRY_TYPE',
  full_name='DOTA_MODIFIER_ENTRY_TYPE',
  filename=None,
  file=DESCRIPTOR,
  values=[
    _descriptor.EnumValueDescriptor(
      name='DOTA_MODIFIER_ENTRY_TYPE_ACTIVE', index=0, number=1,
      options=None,
      type=None),
    _descriptor.EnumValueDescriptor(
      name='DOTA_MODIFIER_ENTRY_TYPE_REMOVED', index=1, number=2,
      options=None,
      type=None),
  ],
  containing_type=None,
  options=None,
  serialized_start=697,
  serialized_end=798,
)

DOTA_MODIFIER_ENTRY_TYPE = enum_type_wrapper.EnumTypeWrapper(_DOTA_MODIFIER_ENTRY_TYPE)
DOTA_MODIFIER_ENTRY_TYPE_ACTIVE = 1
DOTA_MODIFIER_ENTRY_TYPE_REMOVED = 2



_CDOTAMODIFIERBUFFTABLEENTRY = _descriptor.Descriptor(
  name='CDOTAModifierBuffTableEntry',
  full_name='CDOTAModifierBuffTableEntry',
  filename=None,
  file=DESCRIPTOR,
  containing_type=None,
  fields=[
    _descriptor.FieldDescriptor(
      name='entry_type', full_name='CDOTAModifierBuffTableEntry.entry_type', index=0,
      number=1, type=14, cpp_type=8, label=2,
      has_default_value=True, default_value=1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='parent', full_name='CDOTAModifierBuffTableEntry.parent', index=1,
      number=2, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='index', full_name='CDOTAModifierBuffTableEntry.index', index=2,
      number=3, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='serial_num', full_name='CDOTAModifierBuffTableEntry.serial_num', index=3,
      number=4, type=5, cpp_type=1, label=2,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='name', full_name='CDOTAModifierBuffTableEntry.name', index=4,
      number=5, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ability_level', full_name='CDOTAModifierBuffTableEntry.ability_level', index=5,
      number=6, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='stack_count', full_name='CDOTAModifierBuffTableEntry.stack_count', index=6,
      number=7, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='creation_time', full_name='CDOTAModifierBuffTableEntry.creation_time', index=7,
      number=8, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='duration', full_name='CDOTAModifierBuffTableEntry.duration', index=8,
      number=9, type=2, cpp_type=6, label=1,
      has_default_value=True, default_value=-1,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='caster', full_name='CDOTAModifierBuffTableEntry.caster', index=9,
      number=10, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='ability', full_name='CDOTAModifierBuffTableEntry.ability', index=10,
      number=11, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='armor', full_name='CDOTAModifierBuffTableEntry.armor', index=11,
      number=12, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='fade_time', full_name='CDOTAModifierBuffTableEntry.fade_time', index=12,
      number=13, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='subtle', full_name='CDOTAModifierBuffTableEntry.subtle', index=13,
      number=14, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='channel_time', full_name='CDOTAModifierBuffTableEntry.channel_time', index=14,
      number=15, type=2, cpp_type=6, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v_start', full_name='CDOTAModifierBuffTableEntry.v_start', index=15,
      number=16, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='v_end', full_name='CDOTAModifierBuffTableEntry.v_end', index=16,
      number=17, type=11, cpp_type=10, label=1,
      has_default_value=False, default_value=None,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='portal_loop_appear', full_name='CDOTAModifierBuffTableEntry.portal_loop_appear', index=17,
      number=18, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='portal_loop_disappear', full_name='CDOTAModifierBuffTableEntry.portal_loop_disappear', index=18,
      number=19, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_loop_appear', full_name='CDOTAModifierBuffTableEntry.hero_loop_appear', index=19,
      number=20, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='hero_loop_disappear', full_name='CDOTAModifierBuffTableEntry.hero_loop_disappear', index=20,
      number=21, type=9, cpp_type=9, label=1,
      has_default_value=False, default_value=unicode("", "utf-8"),
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='movement_speed', full_name='CDOTAModifierBuffTableEntry.movement_speed', index=21,
      number=22, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='aura', full_name='CDOTAModifierBuffTableEntry.aura', index=22,
      number=23, type=8, cpp_type=7, label=1,
      has_default_value=False, default_value=False,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='activity', full_name='CDOTAModifierBuffTableEntry.activity', index=23,
      number=24, type=5, cpp_type=1, label=1,
      has_default_value=False, default_value=0,
      message_type=None, enum_type=None, containing_type=None,
      is_extension=False, extension_scope=None,
      options=None),
    _descriptor.FieldDescriptor(
      name='damage', full_name='CDOTAModifierBuffTableEntry.damage', index=24,
      number=25, type=5, cpp_type=1, label=1,
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
  serialized_start=83,
  serialized_end=695,
)

_CDOTAMODIFIERBUFFTABLEENTRY.fields_by_name['entry_type'].enum_type = _DOTA_MODIFIER_ENTRY_TYPE
_CDOTAMODIFIERBUFFTABLEENTRY.fields_by_name['v_start'].message_type = networkbasetypes_pb2._CMSGVECTOR
_CDOTAMODIFIERBUFFTABLEENTRY.fields_by_name['v_end'].message_type = networkbasetypes_pb2._CMSGVECTOR
DESCRIPTOR.message_types_by_name['CDOTAModifierBuffTableEntry'] = _CDOTAMODIFIERBUFFTABLEENTRY

class CDOTAModifierBuffTableEntry(_message.Message):
  __metaclass__ = _reflection.GeneratedProtocolMessageType
  DESCRIPTOR = _CDOTAMODIFIERBUFFTABLEENTRY

  # @@protoc_insertion_point(class_scope:CDOTAModifierBuffTableEntry)


# @@protoc_insertion_point(module_scope)
