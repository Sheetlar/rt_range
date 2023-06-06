def decode_enum(enum_dict: dict):
    def decode(value):
        if value not in enum_dict:
            return enum_dict[KeyError]
        return enum_dict[value]

    return decode


nav_status = {
    KeyError: 'Value_not_in_documentation',
    0: 'Invalid',
    1: 'Raw_IMU_measurements',
    2: 'Initializing',
    3: 'Locking',
    4: 'Locked',
    5: 'Reserved',
    6: 'Expired_firmware',
    7: 'Blocked_firmware',
}
channel_status = {
    KeyError: 'Reserved_for_future_use',
    0: 'Time_satellites_mode',
    1: 'Kalman_filter_innovations_1',
    2: 'Internal_info_primary_antenna',
    3: 'Position_accuracy',
    4: 'Velocity_accuracy',
    5: 'Orientation_accuracy',
    6: 'Gyro_bias',
    7: 'Accelerometer_bias',
    8: 'Gyro_scale_factor',
    9: 'Gyro_bias_accuracy',
    10: 'Accelerometer_accuracy',
    11: 'Gyro_scalr_factor_accuracy',
    12: 'Position_estimate_primary_antenna',
    13: 'Orientation_estimate_dual_antenna',
    14: 'Position_accuracy_primary_antenna',
    15: 'Orientation_accuracy_dual_antenna',
    16: 'INS_rotation',
    17: 'Internal_info_secondary_antenna',
    18: 'Internal_info_IMU',
    19: 'INS_SW_version',
    20: 'Differential_correction_info',
    21: 'Disk_space_log_size',
    22: 'Internal_info_processing_timing',
    23: 'Up_time_GNSS_rejections_PTP_status',
    24: 'Async_packet_event_input_falling_edge',
    25: 'Reserved',
    26: 'Displacement_lever_arm',
    27: 'Internal_info_dual_antenna_ambiguity',
    28: 'Internal_info_dual_antenna_ambiguity',
    29: 'Initial_settings_NAVconfig',
    30: 'OS_script_version_info',
    31: 'HW_config_info',
    32: 'Kalman_filter_innovation_2',
    33: 'Zero_velocity_lever_arm',
    34: 'Zero_velocity_lever_arm_accuracy',
    # TODO: Status descriptions
}
