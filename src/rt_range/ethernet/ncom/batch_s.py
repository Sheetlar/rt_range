from rt_range.common import convert_10_pow_m1, convert_10_pow_m2, convert_10_pow_m4, convert_10_pow_m6, validity_bit0
from rt_range.ethernet.rt_types import Field, Byte, UByte, Short, UShort, Long, ULong
from rt_range.ethernet.status_definitions import decode_enum, ncom_position_velocity_orientation_mode, ncom_blended_processing_methods, ncom_ptp_status


def validity_bit0_pow_m1(value: int):
    return convert_10_pow_m1(validity_bit0(value))


async_packet = [
    Field('trigger_minute', Long, unit='min'),
    Field('trigger_millisecond', UShort, unit='ms'),
    Field('trigger_microsecond', Byte, decode_value=lambda v: v * 4 * 10e-6, unit='us'),
    Field('trigger_count', UByte),
]


BatchS = {  # TODO: Block definitions for other status_channel values
    0: [
        Field('time_since_gps', Long, unit='min'),
        Field('num_satellites', UByte),
        Field('position_mode', UByte, decode_value=decode_enum(ncom_position_velocity_orientation_mode)),
        Field('velocity_mode', UByte, decode_value=decode_enum(ncom_position_velocity_orientation_mode)),
        Field('orientation_mode', UByte, decode_value=decode_enum(ncom_position_velocity_orientation_mode)),
    ],
    1: [
        Field('position_x_innovation', UByte, decode_value=validity_bit0_pow_m1),
        Field('position_y_innovation', UByte, decode_value=validity_bit0_pow_m1),
        Field('position_z_innovation', UByte, decode_value=validity_bit0_pow_m1),
        Field('velocity_x_innovation', UByte, decode_value=validity_bit0_pow_m1),
        Field('velocity_y_innovation', UByte, decode_value=validity_bit0_pow_m1),
        Field('velocity_z_innovation', UByte, decode_value=validity_bit0_pow_m1),
        Field('orientation_pitch_innovation', UByte, decode_value=validity_bit0_pow_m1),
        Field('orientation_heading_innovation', UByte, decode_value=validity_bit0_pow_m1),
    ],
    2: [
        Field('primary_GNSS_characters_received', UShort),
        Field('primary_GNSS_packets_received', UShort),
        Field('primary_GNSS_characters_skipped', UShort),
        Field('primary_GNSS_packets_skipped', UShort),
    ],
    3: [
        Field('north_position_accuracy', UShort, unit='mm'),
        Field('east_position_accuracy', UShort, unit='mm'),
        Field('down_position_accuracy', UShort, unit='mm'),
        Field('age', UByte),
        Field('ABD_robot_UMAC_interface_status', UByte),
    ],
    4: [
        Field('north_velocity_accuracy', UShort, unit='mm/s'),
        Field('east_velocity_accuracy', UShort, unit='mm/s'),
        Field('down_velocity_accuracy', UShort, unit='mm/s'),
        Field('age', UByte),
        Field('processing_method', UByte, decode_value=decode_enum(ncom_blended_processing_methods)),
    ],
    5: [
        Field('heading_accuracy', UShort, unit='mm'),
        Field('pitch_accuracy', UShort, unit='mm'),
        Field('roll_accuracy', UShort, unit='mm'),
        Field('age', UByte),
        Field('reserved', UByte),
    ],
    6: [
        Field('gyro_bias_x', Short, decode_value=convert_10_pow_m4, unit='rad/s'),
        Field('gyro_bias_y', Short, decode_value=convert_10_pow_m4, unit='rad/s'),
        Field('gyro_bias_z', Short, decode_value=convert_10_pow_m4, unit='rad/s'),
        Field('age', UByte),
        Field('L1_L2_GPS_measurements_decoded_primary_receiver', UByte),
    ],
    7: [
        Field('accelerometer_bias_x', Short, decode_value=convert_10_pow_m1, unit='mm/s^2'),
        Field('accelerometer_bias_y', Short, decode_value=convert_10_pow_m1, unit='mm/s^2'),
        Field('accelerometer_bias_z', Short, decode_value=convert_10_pow_m1, unit='mm/s^2'),
        Field('age', UByte),
        Field('L1_L2_GPS_measurements_decoded_secondary_receiver', UByte),
    ],
    8: [
        Field('gyro_scale_factor_x', Short, decode_value=convert_10_pow_m4, unit='%'),
        Field('gyro_scale_factor_y', Short, decode_value=convert_10_pow_m4, unit='%'),
        Field('gyro_scale_factor_z', Short, decode_value=convert_10_pow_m4, unit='%'),
        Field('age', UByte),
        Field('L1_L2_GPS_measurements_decoded_external_receiver', UByte),
    ],
    9: [
        Field('accuracy_gyro_bias_x', Short, decode_value=convert_10_pow_m6, unit='rad/s'),
        Field('accuracy_gyro_bias_y', Short, decode_value=convert_10_pow_m6, unit='rad/s'),
        Field('accuracy_gyro_bias_z', Short, decode_value=convert_10_pow_m6, unit='rad/s'),
        Field('age', UByte),
        Field('L1_L2_GLONASS_measurements_decoded_primary_receiver', UByte),
    ],
    10: [
        Field('accuracy_accelerometer_bias_x', Short, decode_value=convert_10_pow_m2, unit='mm/s^2'),
        Field('accuracy_accelerometer_bias_y', Short, decode_value=convert_10_pow_m2, unit='mm/s^2'),
        Field('accuracy_accelerometer_bias_z', Short, decode_value=convert_10_pow_m2, unit='mm/s^2'),
        Field('age', UByte),
        Field('L1_L2_GLONASS_measurements_decoded_secondary_receiver', UByte),
    ],
    11: [
        Field('accuracy_gyro_scale_factor_x', Short, decode_value=convert_10_pow_m4, unit='%'),
        Field('accuracy_gyro_scale_factor_y', Short, decode_value=convert_10_pow_m4, unit='%'),
        Field('accuracy_gyro_scale_factor_z', Short, decode_value=convert_10_pow_m4, unit='%'),
        Field('age', UByte),
        Field('L1_L2_GLONASS_measurements_decoded_external_receiver', UByte),
    ],
    12: [
        Field('distance_to_primary_GNSS_x', Short, unit='mm'),
        Field('distance_to_primary_GNSS_y', Short, unit='mm'),
        Field('distance_to_primary_GNSS_z', Short, unit='mm'),
        Field('age', UByte),
        Field('reserved', UByte),
    ],
    13: [
        Field('heading_GNSS_antennas', Short, decode_value=convert_10_pow_m4, unit='rad'),
        Field('pitch_GNSS_antennas', Short, decode_value=convert_10_pow_m4, unit='rad'),
        Field('distance_GNSS_antennas', Short, unit='mm'),
        Field('age', UByte),
        Field('number_GPS_satellites_in_heading_module', UByte),
    ],
    14: [
        Field('accuracy_distance_to_primary_GNSS_x', Short, decode_value=convert_10_pow_m1, unit='mm'),
        Field('accuracy_distance_to_primary_GNSS_y', Short, decode_value=convert_10_pow_m1, unit='mm'),
        Field('accuracy_distance_to_primary_GNSS_z', Short, decode_value=convert_10_pow_m1, unit='mm'),
        Field('age', UByte),
        Field('number_satellites_in_position_solution', UByte),
    ],
    15: [
        Field('accuracy_heading_GNSS_antennas', Short, decode_value=convert_10_pow_m4, unit='rad'),
        Field('accuracy_pitch_GNSS_antennas', Short, decode_value=convert_10_pow_m4, unit='rad'),
        Field('accuracy_distance_GNSS_antennas', Short, unit='mm'),
        Field('age', UByte),
        Field('number_GLONASS_satellites_in_heading_module', UByte),
    ],
    16: [
        Field('vehicle_heading_INS', Short, decode_value=convert_10_pow_m4, unit='rad'),
        Field('vehicle_pitch_INS', Short, decode_value=convert_10_pow_m4, unit='rad'),
        Field('vehicle_roll_INS', Short, decode_value=convert_10_pow_m4, unit='rad'),
        Field('validity', UByte),
        Field('UTC_time_offset', UByte, decode_value=validity_bit0, unit='s'),
    ],
    17: [
        Field('secondary_GNSS_characters_received', UShort),
        Field('secondary_GNSS_packets_received', UShort),
        Field('secondary_GNSS_characters_skipped', UShort),
        Field('secondary_GNSS_packets_skipped', UShort),
    ],
    18: [
        Field('IMU_characters_received', ULong),
        Field('IMU_packets_received', UShort),
        Field('IMU_characters_skipped', UShort),
    ],
    19: [
        Field('ID_byte_0', Byte),
        Field('ID_byte_1', Byte),
        Field('ID_byte_2', Byte),
        Field('ID_byte_3', Byte),
        Field('ID_byte_4', Byte),
        Field('ID_byte_5', Byte),
        Field('ID_byte_6', Byte),
        Field('ID_byte_7', Byte),
    ],
    20: [
        Field('differential_corrections_age', Short),
        Field('station_ID_byte_0', Byte),
        Field('station_ID_byte_1', Byte),
        Field('station_ID_byte_2', Byte),
        Field('station_ID_byte_3', Byte),
        Field('reserved', UByte),
    ],
    21: [
        Field('disk_space_remaining', Long, unit='kB'),
        Field('current_data_file_size', Long, unit='kB'),
    ],
    22: [
        Field('time_mismatch_counter', UShort),
        Field('IMU_time_difference', UByte, unit='ms'),
        Field('IMU_time_margin', UByte, unit='ms'),
        Field('IMU_loop_time', UShort, unit='ms'),
        Field('output_loop_time', UShort, unit='ms'),
    ],
    23: [
        Field('blended_navigation_lag_time', UShort, unit='ms'),
        Field('INS_running_time', UShort),  # TODO: Unit depends on value
        Field('number_consecutive_GPS_position_updates_rejected', UByte),
        Field('number_consecutive_GPS_velocity_updates_rejected', UByte),
        Field('number_consecutive_GPS_orientation_updates_rejected', UByte),
        Field('PTP_status', UByte, decode_value=decode_enum(ncom_ptp_status))
    ],
    24: async_packet,
    # 25: Reserved,
    26: [
        Field('output_displacement_lever_arm_x', Short, unit='mm'),
        Field('output_displacement_lever_arm_y', Short, unit='mm'),
        Field('output_displacement_lever_arm_z', Short, unit='mm'),
        Field('validity', UByte),
        Field('Reserved', UByte),
    ],
}
