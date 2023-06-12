from rt_range.common import convert_10_pow_m2, convert_10_pow_m3, convert_10_pow_m4
from rt_range.ethernet.rt_packet import Packet
from rt_range.ethernet.rt_types import Field, VariableBlock, Byte, UByte, Short, UShort, Word, UWord, Long, ULong
from rt_range.ethernet.status_definitions import decode_enum, rcom_lane_status_channel


def lever_arm_struct(point_name: str):
    return [
        Field(f'point_{point_name}_lever-arm_x', Word, decode_value=convert_10_pow_m3, unit='m'),
        Field(f'point_{point_name}_lever-arm_y', Word, decode_value=convert_10_pow_m3, unit='m'),
        Field(f'point_{point_name}_lever-arm_z', Short, decode_value=convert_10_pow_m3, unit='m'),
    ]


rcom_lane_status = {
    0: [
        Field('GPS_time', Long, unit='min'),
        Field('reserved', ULong),
    ],
    1: [
        Field('ID_byte_0', Byte),
        Field('ID_byte_1', Byte),
        Field('ID_byte_2', Byte),
        Field('ID_byte_3', Byte),
        Field('ID_byte_4', Byte),
        Field('ID_byte_5', Byte),
        Field('ID_byte_6', Byte),
        Field('ID_byte_7', Byte),
    ],
    2: [
        Field('map_number', UByte),
        Field('reserved_1', UWord),
        Field('reserved_2', ULong),
    ],
    6: [
        Field('major_OS_version', UByte),
        Field('minor_OS_version', UByte),
        Field('OS_revision_version', UByte),
        Field('script_version', UWord),
        Field('reserved', UShort),
    ],
    7: [
        Field('UTC_offset', Short, unit='s'),
        Field('reserved_1', UShort),
        Field('reserved_2', UWord),
        Field('CPU_load', UByte, decode_value=lambda v: v * 0.4, unit='%'),
    ],
    8: lever_arm_struct('A'),
    9: lever_arm_struct('B'),
    10: lever_arm_struct('C'),
    15: [
        Field('UDP_command_characters_received', UShort),
        Field('UDP_command_packets_received', UShort),
        Field('UDP_command_characters_skipped', UShort),
        Field('UDP_command_errors', UShort),
    ],
}

RCOM_lane = Packet([
    Field('sync', UByte),  # 0x57
    Field('packet_type', UByte),  # 0x01
    Field('length_of_data_section', UShort),
    Field('GPS_time_into_minute', UShort, decode_value=convert_10_pow_m3, unit='s'),
    Field('line_number_to_left_of_A', UByte),
    Field('line_number_to_right_of_A', UByte),
    Field('distance_along_line_1', Long, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_to_left_of_A', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_velocity_to_left_of_A', Short, decode_value=convert_10_pow_m2, unit='m/s'),
    Field('lateral_acceleration_to_left_of_A', Short, decode_value=convert_10_pow_m2, unit='m/s^2'),
    Field('lateral_distance_to_right_of_A', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_velocity_to_right_of_A', Short, decode_value=convert_10_pow_m2, unit='m/s'),
    Field('lateral_acceleration_to_right_of_A', Short, decode_value=convert_10_pow_m2, unit='m/s^2'),
    Field('lateral_distance_from_point_A_to_line_1', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_A_to_line_2', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_A_to_line_3', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_A_to_line_4', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_A_to_line_5', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_A_to_line_6', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_A_to_line_7', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_A_to_line_8', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_B_to_line_on_left_of_A', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_C_to_line_on_right_of_A', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('line_on_left_of_point_B', UByte),
    Field('line_on_right_of_point_B', UByte),
    Field('line_on_left_of_point_C', UByte),
    Field('line_on_right_of_point_C', UByte),
    Field('reserved', UByte),
    Field('status_channel', UByte, decode_value=decode_enum(rcom_lane_status_channel)),
    VariableBlock(selector=49, name='status', size=8, structure=rcom_lane_status),
    Field('lateral_velocity_from_point_A_to_line_1', Short, decode_value=convert_10_pow_m2, unit='m/s'),
    Field('lateral_velocity_from_point_A_to_line_2', Short, decode_value=convert_10_pow_m2, unit='m/s'),
    Field('lateral_velocity_from_point_A_to_line_3', Short, decode_value=convert_10_pow_m2, unit='m/s'),
    Field('lateral_velocity_from_point_A_to_line_4', Short, decode_value=convert_10_pow_m2, unit='m/s'),
    Field('lateral_velocity_from_point_A_to_line_5', Short, decode_value=convert_10_pow_m2, unit='m/s'),
    Field('lateral_velocity_from_point_A_to_line_6', Short, decode_value=convert_10_pow_m2, unit='m/s'),
    Field('lateral_velocity_from_point_A_to_line_7', Short, decode_value=convert_10_pow_m2, unit='m/s'),
    Field('lateral_velocity_from_point_A_to_line_8', Short, decode_value=convert_10_pow_m2, unit='m/s'),
    Field('lateral_distance_from_point_B_to_line_1', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_B_to_line_2', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_B_to_line_3', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_B_to_line_4', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_B_to_line_5', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_B_to_line_6', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_B_to_line_7', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_B_to_line_8', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_C_to_line_1', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_C_to_line_2', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_C_to_line_3', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_C_to_line_4', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_C_to_line_5', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_C_to_line_6', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_C_to_line_7', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_distance_from_point_C_to_line_8', Short, decode_value=convert_10_pow_m3, unit='m'),
    Field('curvature_of_line_1', Short, decode_value=convert_10_pow_m4, unit='1/m'),
    Field('curvature_of_line_2', Short, decode_value=convert_10_pow_m4, unit='1/m'),
    Field('curvature_of_line_3', Short, decode_value=convert_10_pow_m4, unit='1/m'),
    Field('curvature_of_line_4', Short, decode_value=convert_10_pow_m4, unit='1/m'),
    Field('curvature_of_line_5', Short, decode_value=convert_10_pow_m4, unit='1/m'),
    Field('curvature_of_line_6', Short, decode_value=convert_10_pow_m4, unit='1/m'),
    Field('curvature_of_line_7', Short, decode_value=convert_10_pow_m4, unit='1/m'),
    Field('curvature_of_line_8', Short, decode_value=convert_10_pow_m4, unit='1/m'),
    Field('curvature_of_point_A', Short, decode_value=convert_10_pow_m4, unit='1/m'),
    Field('curvature_of_point_B', Short, decode_value=convert_10_pow_m4, unit='1/m'),
    Field('curvature_of_point_C', Short, decode_value=convert_10_pow_m4, unit='1/m'),
    Field('heading_with_respect_to_line_on_left_of_A', Short, decode_value=convert_10_pow_m2, unit='deg'),
    Field('heading_with_respect_to_line_on_right_of_A', Short, decode_value=convert_10_pow_m2, unit='deg'),
    Field('checksum', UByte),
])