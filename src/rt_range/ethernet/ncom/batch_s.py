from rt_range.ethernet.rt_types import Field, Long, UByte

BatchS = {  # TODO: Modes description
    0: [Field('time_since_gps', Long, unit='min'),
        Field('num_satellites', UByte),
        Field('position_mode', UByte),
        Field('velocity_mode', UByte),
        Field('orientation_mode', UByte)],
}
