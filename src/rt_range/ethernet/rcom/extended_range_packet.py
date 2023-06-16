import itertools

from rt_range.common import convert_10_pow_m2, convert_10_pow_m3, convert_10_pow_m7
from rt_range.ethernet.rt_packet import Packet
from rt_range.ethernet.rt_types import Field, VariableBlock, Byte, UByte, Short, UShort, Word, UWord, Long, ULong, Float
from rt_range.ethernet.status_definitions import decode_enum, rcom_ex_range_status_channel, ncom_position_velocity_orientation_mode


def multiple_sensor_points():
    return itertools.chain.from_iterable(
        (
            Field(f'resultant_range_from_sensor_point_{idx}_to_target', ULong, decode_value=convert_10_pow_m3, unit='m'),
            Field(f'percentage_target_visible_in_FoV_sensor_point_{idx}', UByte),
            Field(f'percentage_FoV_occupied_by_target_sensor_point_{idx}', UByte),
        )
        for idx in range(12)
    )


rcom_ex_range_status = {
    0: [
        Field('GPS_time', Long, unit='min'),
        Field('hunter_position_mode', UByte, decode_value=decode_enum(ncom_position_velocity_orientation_mode)),
        Field('target_position_mode', UByte, decode_value=decode_enum(ncom_position_velocity_orientation_mode)),
        Field('target_latency', UShort, decode_value=convert_10_pow_m3, unit='s'),
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
        Field('target_radio_characters_received', UShort),
        Field('target_radio_packets_received', UShort),
        Field('target_radio_characters_skipped', UShort),
        Field('reserved', UShort),
    ],
    3: [
        Field('target_WLAN_characters_received', UShort),
        Field('target_WLAN_packets_received', UShort),
        Field('target_WLAN_characters_skipped', UShort),
        Field('reserved', UShort),
    ],
    4: [
        Field('hunter_ethernet_characters_received', UShort),
        Field('hunter_ethernet_packets_received', UShort),
        Field('hunter_ethernet_characters_skipped', UShort),
        Field('reserved', UShort),
    ],
    5: [
        Field('hunter_output_latency', UShort, decode_value=convert_10_pow_m3, unit='s'),
        Field('range_longitudinal_offset', Short, decode_value=convert_10_pow_m3, unit='m'),
        Field('range_lateral_offset', Short, decode_value=convert_10_pow_m3, unit='m'),
        Field('reserved', UShort),
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
        Field('range_reference_plane_configuration', UByte),
        Field('target_feature_set_number', UByte),
        Field('number_feature_points_feature_set', UShort),
        Field('maximum_feature_points_per_feature_cell', UByte),
        Field('CPU_load', UByte, decode_value=lambda v: v * 0.4, unit='%'),
    ],
    8: [
        Field('fixed_point_latitude', Long, decode_value=convert_10_pow_m7, unit='deg'),
        Field('fixed_point_longitude', Long, decode_value=convert_10_pow_m7, unit='deg'),
    ],
    9: [
        Field('hunter_ip_byte_1', UByte),
        Field('hunter_ip_byte_2', UByte),
        Field('hunter_ip_byte_3', UByte),
        Field('hunter_ip_byte_4', UByte),
        Field('target_ip_byte_1', UByte),
        Field('target_ip_byte_2', UByte),
        Field('target_ip_byte_3', UByte),
        Field('target_ip_byte_4', UByte),
    ],
    10: [
        Field('fixed_point_altitude', Long, decode_value=convert_10_pow_m3, unit='m'),
        Field('fixed_point_heading', ULong, decode_value=convert_10_pow_m7, unit='deg'),
    ],
    11: [
        Field('local_coordinate_origin_latitude', Long, decode_value=convert_10_pow_m7, unit='deg'),
        Field('local_coordinate_origin_longitude', Long, decode_value=convert_10_pow_m7, unit='deg'),
    ],
    12: [
        Field('local_coordinate_origin_altitude', Long, decode_value=convert_10_pow_m3, unit='m'),
        Field('local_coordinate_origin_heading', ULong, decode_value=convert_10_pow_m7, unit='deg'),
    ],
    13: [
        Field('hunter_lever_arm_x', Word, decode_value=convert_10_pow_m3, unit='m'),
        Field('hunter_lever_arm_y', Word, decode_value=convert_10_pow_m3, unit='m'),
        Field('hunter_lever_arm_z', Short, decode_value=convert_10_pow_m3, unit='m'),
    ],
    14: [
        Field('target_lever_arm_x', Word, decode_value=convert_10_pow_m3, unit='m'),
        Field('target_lever_arm_y', Word, decode_value=convert_10_pow_m3, unit='m'),
        Field('target_lever_arm_z', Short, decode_value=convert_10_pow_m3, unit='m'),
    ],
    15: [
        Field('UDP_command_characters_received', UShort),
        Field('UDP_command_packets_received', UShort),
        Field('UDP_command_characters_skipped', UShort),
        Field('UDP_command_errors', UShort),
    ],
    16: [
        Field('range_longitudinal_accuracy', UShort, decode_value=convert_10_pow_m3, unit='m'),
        Field('range_lateral_accuracy', UShort, decode_value=convert_10_pow_m3, unit='m'),
        Field('range_vertical_accuracy', UShort, decode_value=convert_10_pow_m3, unit='m'),
        Field('range_magnitude_accuracy', UShort, decode_value=convert_10_pow_m3, unit='m'),
    ],
    17: [
        Field('target_vehicle_length', UShort, decode_value=convert_10_pow_m3, unit='m'),
        Field('target_vehicle_width', UShort, decode_value=convert_10_pow_m3, unit='m'),
        Field('target_polygon_number', UShort),
        Field('target_vehicle_height', UShort, decode_value=convert_10_pow_m3, unit='m'),
    ],
    18: [
        Field('acceleration_filter_cut_off_frequency', Float, unit='Hz'),
        Field('acceleration_filter_damping_ratio', Float),
    ],
    19: [
        Field('extrapolation_filter_cut_off_frequency', Float, unit='Hz'),
        Field('extrapolation_filter_damping_ratio', Float),
    ],
    20: [
        Field('feature_point_latitude', Long, decode_value=convert_10_pow_m7, unit='deg'),
        Field('feature_point_longitude', Long, decode_value=convert_10_pow_m7, unit='deg'),
    ],
    21: [
        Field('feature_point_altitude', Long, decode_value=convert_10_pow_m3, unit='m'),
        Field('feature_point_heading', ULong, decode_value=convert_10_pow_m7, unit='deg'),
    ],
    22: [
        Field('hunter_vehicle_length', UShort, decode_value=convert_10_pow_m3, unit='m'),
        Field('hunter_vehicle_width', UShort, decode_value=convert_10_pow_m3, unit='m'),
        Field('hunter_polygon_number', UShort),
        Field('hunter_vehicle_height', UShort, decode_value=convert_10_pow_m3, unit='m'),
    ],
}

RCOM_extended_range = Packet([
    Field('sync', UByte),  # 0x57
    Field('packet_type', UByte),  # 0x02
    Field('length_of_data_section', UShort),
    Field('GPS_time_into_minute', UShort, decode_value=convert_10_pow_m3, unit='s'),
    Field('target_number', UByte),
    Field('total_number_of_targets', UByte),
    Field('lateral_range', Long, decode_value=convert_10_pow_m3, unit='m'),
    Field('longitudinal_range', Long, decode_value=convert_10_pow_m3, unit='m'),
    Field('lateral_range_rate', Short, decode_value=convert_10_pow_m2, unit='m/s'),
    Field('longitudinal_range_rate', Short, decode_value=convert_10_pow_m2, unit='m/s'),
    Field('hunter_measurement_point_position_x', Long, decode_value=convert_10_pow_m3, unit='m'),
    Field('hunter_measurement_point_position_y', Long, decode_value=convert_10_pow_m3, unit='m'),
    Field('target_measurement_point_position_x', Long, decode_value=convert_10_pow_m3, unit='m'),
    Field('target_measurement_point_position_y', Long, decode_value=convert_10_pow_m3, unit='m'),
    Field('hunter_heading_angle', UShort, decode_value=convert_10_pow_m2, unit='deg'),
    Field('target_heading_angle', UShort, decode_value=convert_10_pow_m2, unit='deg'),
    Field('range_status', UByte),
    Field('status_channel', UByte, decode_value=decode_enum(rcom_ex_range_status_channel)),
    VariableBlock(selector=41, name='status', size=8, structure=rcom_ex_range_status),
    Field('hunter_forward_velocity', Short, decode_value=convert_10_pow_m2, unit='m/s'),
    Field('hunter_lateral_velocity', Short, decode_value=convert_10_pow_m2, unit='m/s'),
    Field('lateral_range_acceleration', Short, decode_value=convert_10_pow_m2, unit='m/s^2'),
    Field('longitudinal_range_acceleration', Short, decode_value=convert_10_pow_m2, unit='m/s^2'),
    Field('nearest_target_polygon_vertex_to_hunter_point_left', UByte),
    Field('nearest_target_polygon_vertex_to_hunter_point_right', UByte),
    Field('target_visibility', UByte, unit='%'),
    Field('target_feature_point_type', UByte),
    Field('target_feature_point_index', UShort),
    Field('nearest_hunter_polygon_vertex_to_target_point_left', UByte),
    Field('nearest_hunter_polygon_vertex_to_target_point_right', UByte),
    Field('nearest_target_polygon_vertex_to_hunter_polygon_left', UByte),
    Field('nearest_target_polygon_vertex_to_hunter_polygon_right', UByte),
    Field('nearest_hunter_polygon_vertex_to_target_polygon_left', UByte),
    Field('nearest_hunter_polygon_vertex_to_target_polygon_right', UByte),
    Field('nearest_target_polygon_vertex_to_hunter_point_scale', UByte, decode_value=lambda v: v * 0.004),
    Field('nearest_hunter_polygon_vertex_to_target_point_scale', UByte, decode_value=lambda v: v * 0.004),
    Field('nearest_target_polygon_vertex_to_hunter_polygon_scale', UByte, decode_value=lambda v: v * 0.004),
    Field('nearest_hunter_polygon_vertex_to_target_polygon_scale', UByte, decode_value=lambda v: v * 0.004),
    Field('hunter_polygon_origin_position_x', Long),
    Field('hunter_polygon_origin_position_y', Long),
    Field('target_polygon_origin_position_x', Long),
    Field('target_polygon_origin_position_y', Long),
    Field('hunter_unit_position_x', Long),
    Field('hunter_unit_position_y', Long),
    Field('target_unit_position_x', Long),
    Field('target_unit_position_y', Long),
    Field('hunter_pitch_angle', Short, decode_value=convert_10_pow_m2, unit='deg'),
    Field('hunter_roll_angle', Short, decode_value=convert_10_pow_m2, unit='deg'),
    Field('target_pitch_angle', Short, decode_value=convert_10_pow_m2, unit='deg'),
    Field('target_roll_angle', Short, decode_value=convert_10_pow_m2, unit='deg'),
    *multiple_sensor_points(),
    Field('checksum', UByte),
])
