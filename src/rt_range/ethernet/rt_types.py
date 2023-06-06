from dataclasses import dataclass, InitVar
from typing import Callable, Any
from typing import TypeAlias

import numpy as np

ValueConvertFunc: TypeAlias = Callable[[Any], Any]


@dataclass
class RTType:
    """
    RT data type definition
    :param dtype: NumPy dtype for structure decoding
    :param get_value: Function for converting dtype into raw value
    """
    dtype: type | np.dtype
    get_value: ValueConvertFunc | None = None

    def __post_init__(self):
        if self.get_value is None:
            self.get_value = self._default_get_value

    @staticmethod
    def _default_get_value(value):
        return value


@dataclass
class Field:
    """
    RT data packet field
    :param name: Filed name
    :param rt_type: RT data type of the field
    :param decode_value: Function for raw value conversion to specified format
    :param unit: Unit of the field value
    """
    name: str
    rt_type: InitVar[RTType]
    decode_value: InitVar[Callable[[Any], Any]] = None
    unit: str = None

    def __post_init__(self, rt_type: RTType, decode_value: InitVar[ValueConvertFunc]):
        if decode_value is None:
            decode_value = self._default_decode_value
        self._decode_value = decode_value
        self._decode_dtype = rt_type.get_value
        self.dtype = rt_type.dtype

    @staticmethod
    def _default_decode_value(value):
        return value

    def get_value(self, value):
        return self._decode_value(self._decode_dtype(value))


@dataclass
class VariableBlock:
    selector: int
    structure: dict[int, list[Field]]
    size: InitVar[int]
    name: str | None = None

    def __post_init__(self, size: int):
        field_name = self.name if self.name is not None else f'field_{hex(id(self))}'
        self.default = Field(field_name, RTType(
            np.dtype([(f'b{i}', np.uint8) for i in range(size)]),
            get_value=lambda _: 'Parser_not_implemented',
        ))


Selector: TypeAlias = tuple[int, ...] | None
Structure: TypeAlias = list[Field | VariableBlock]

Byte = RTType(np.int8)
UByte = RTType(np.uint8)
Short = RTType(np.int16)
UShort = RTType(np.uint16)
Word = RTType(
    np.dtype([('b0', np.uint8), ('b1', np.uint8), ('b2', np.uint8)]),
    get_value=lambda v: x if (x := np.frombuffer(bytes(v) + b'\0', dtype=np.int32)[0]) < 0x800000 else -(~x & 0x00FFFFFF) - 1,
)
UWord = RTType(
    np.dtype([('b0', np.uint8), ('b1', np.uint8), ('b2', np.uint8)]),
    get_value=lambda v: np.frombuffer(bytes(v) + b'\0', dtype=np.int32)[0],
)
Long = RTType(np.int32)
ULong = RTType(np.uint32)
Int64 = RTType(np.int64)
UInt64 = RTType(np.uint64)
Float = RTType(np.float32)
Double = RTType(np.float64)
