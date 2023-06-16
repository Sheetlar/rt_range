from rt_range.ethernet.ncom.batch_s import BatchS
from rt_range.ethernet.ncom.ncom import BatchA, BatchB
from rt_range.ethernet.rt_packet import Packet
from rt_range.ethernet.rt_types import Field, UByte, UShort, VariableBlock
from rt_range.ethernet.status_definitions import decode_enum, ncom_nav_status, ncom_channel_status

RCOM_wrapped_NCOM = Packet([
    Field('sync', UByte),  # 0x57
    Field('packet_type', UByte),  # 0x03
    Field('length_of_data_section', UShort),
    Field('sender_ip_byte_1', UByte),
    Field('sender_ip_byte_2', UByte),
    Field('sender_ip_byte_3', UByte),
    Field('sender_ip_byte_4', UByte),
    Field('NCOM_provenance', UByte),
    Field('ncom_sync', UByte),  # 0xE7
    *BatchA,
    Field('nav_status', UByte, decode_value=decode_enum(ncom_nav_status)),
    Field('checksum_1', UByte),
    *BatchB,
    Field('checksum_2', UByte),
    Field('status_channel', UByte, decode_value=decode_enum(ncom_channel_status)),
    VariableBlock(selector=71, name='batch_s', size=8, structure=BatchS),
    Field('checksum_3', UByte),
    Field('checksum', UByte),
])
