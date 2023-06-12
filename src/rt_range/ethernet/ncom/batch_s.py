from rt_range.ethernet.rt_types import Field, Long, UByte, UShort
from rt_range.ethernet.status_definitions import decode_enum, ncom_position_velocity_orientation_mode, ncom_blended_processing_methods

BatchS = {  # TODO: Block definitions for other status_channel values
    0: [Field('time_since_gps', Long, unit='min'),
        Field('num_satellites', UByte),
        Field('position_mode', UByte, decode_value=decode_enum(ncom_position_velocity_orientation_mode)),
        Field('velocity_mode', UByte, decode_value=decode_enum(ncom_position_velocity_orientation_mode)),
        Field('orientation_mode', UByte, decode_value=decode_enum(ncom_position_velocity_orientation_mode))],
    3: [Field('north_position_accuracy', UShort, unit='mm'),
        Field('east_position_accuracy', UShort, unit='mm'),
        Field('down_position_accuracy', UShort, unit='mm'),
        Field('age', UByte),
        Field('ABD_robot_UMAC_interface_status', UByte)],
    4: [Field('north_velocity_accuracy', UShort, unit='mm/s'),
        Field('east_velocity_accuracy', UShort, unit='mm/s'),
        Field('down_velocity_accuracy', UShort, unit='mm/s'),
        Field('age', UByte),
        Field('processing_method', UByte, decode_value=decode_enum(ncom_blended_processing_methods))],
    5: [Field('heading_accuracy', UShort, unit='mm'),
        Field('pitch_accuracy', UShort, unit='mm'),
        Field('roll_accuracy', UShort, unit='mm'),
        Field('age', UByte),
        Field('reserved', UByte)],
}
