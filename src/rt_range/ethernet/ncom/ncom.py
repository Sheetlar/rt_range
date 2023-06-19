from rt_range.common import convert_10_pow_m3, convert_10_pow_m4, convert_10_pow_m5, convert_10_pow_m6
from rt_range.ethernet.ncom.batch_s import BatchS
from rt_range.ethernet.rt_packet import Packet
from rt_range.ethernet.rt_types import Field, UByte, UShort, Word, Float, Double, VariableBlock
from rt_range.ethernet.status_definitions import decode_enum, ncom_nav_status, ncom_channel_status


BatchA = [
    Field('time', UShort, decode_value=convert_10_pow_m3, unit='s'),
    Field('acceleration_x', Word, decode_value=convert_10_pow_m4, unit='m/s^2'),
    Field('acceleration_y', Word, decode_value=convert_10_pow_m4, unit='m/s^2'),
    Field('acceleration_z', Word, decode_value=convert_10_pow_m4, unit='m/s^2'),
    Field('angular_rate_x', Word, decode_value=convert_10_pow_m5, unit='rad/s'),
    Field('angular_rate_y', Word, decode_value=convert_10_pow_m5, unit='rad/s'),
    Field('angular_rate_z', Word, decode_value=convert_10_pow_m5, unit='rad/s'),
]
BatchB = [
    Field('latitude', Double, unit='rad'),
    Field('longitude', Double, unit='rad'),
    Field('altitude', Float, unit='m'),
    Field('north_velocity', Word, decode_value=convert_10_pow_m4, unit='m/s'),
    Field('east_velocity', Word, decode_value=convert_10_pow_m4, unit='m/s'),
    Field('down_velocity', Word, decode_value=convert_10_pow_m4, unit='m/s'),
    Field('heading', Word, decode_value=convert_10_pow_m6, unit='rad'),
    Field('pitch', Word, decode_value=convert_10_pow_m6, unit='rad'),
    Field('roll', Word, decode_value=convert_10_pow_m6, unit='rad'),
]

NCOM = Packet([
    Field('sync', UByte),  # 0xE7
    *BatchA,
    Field('nav_status', UByte, decode_value=decode_enum(ncom_nav_status)),
    Field('checksum_1', UByte),
    *BatchB,
    Field('checksum_2', UByte),
    Field('status_channel', UByte, decode_value=decode_enum(ncom_channel_status)),
    VariableBlock(selector=62, name='batch_s', size=8, structure=BatchS),
    Field('checksum_3', UByte),
])
