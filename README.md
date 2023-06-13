# OxTS RT-Range data parsing utility

This simple parser is capable of parsing RT-Range Ethernet packets (NCOM and RCOM).

**REQUIRES PYTHON 3.10 OR NEWER**

## Installation

Use [pip](https://pip.pypa.io/en/stable/) to install

```bash
pip install rt-range
```

## Usage

### Basic parsing

```python
from rt_range.ethernet import EthernetParser

rt_packet: bytes = ...  # RT-Range Ethernet packet

# Parsing with automatic packet type identification
parsed: dict[str, ...] = EthernetParser.parse_rt_ethernet(rt_packet)
```

The packet type will be determined automatically.
Raises `ValueError` if the bytestring is not a valid RT-Range packet.
Raises `NotImplementedError` if the parser for detected type is not implemented.

### Specifying packet type

```python
from rt_range.ethernet import EthernetParser, PacketType

ncom_data: list[bytes] = ...  # RT-Range Ethernet packets list

# Parsing with specified type
parsed: list[dict[str, ...]] = [
    EthernetParser.parse_rt_ethernet(packet, PacketType.NCOM)
    for packet in ncom_data
]
```

This forces the parser to use the specified packet type
regardless of the packet contents. Use this only if you are sure about the packet content
asit may lead to parsing errors or unexpected values in the parsing result.

Raises `NotImplementedError` if the parser for detected type is not implemented.

### Using Pandas

```python
import pandas as pd
from rt_range.ethernet import EthernetParser, PacketType

range_data: list[bytes] = ...  # RT-Range Ethernet packets list

# Parsing and converting to DataFrame
parsed = pd.DataFrame([
    EthernetParser.parse_rt_ethernet(packet, PacketType.RCOM_extended_range)
    for packet in range_data
])
```

The returned list of dictionaries can be easily converted to the Pandas Dataframe
for further processing.

## Short documentation

### Class `EthernetParser`

- Package: `rt_range.ethernet.eth_parser`
- Import: `from rt_range.ethernet import EthernetParser`
- Purpose: RT-Range NCOM and RCOM packets parsing
- Members:
  - Class method `is_implemented(cls, packet_type: PacketType)`

    Returns `True` if the parser for the specified packet type is implemented,
    `False` otherwise
  - Class method `parse_rt_ethernet(cls, buffer: bytes, packet_type: PacketType | None = None)`

    Parse bytes buffer to `dict[str, ...]`

### Enum `PacketType`

- Package: `rt_range.ethernet.eth_parser`
- Import: `from rt_range.ethernet import PacketType`
- Purpose: RT-Range packets types definitions
- Members:
  - NCOM
  - RCOM_lane
  - RCOM_extended_range
  - RCOM_wrapped_NCOM
  - RCOM_trigger_time
  - RCOM_polygon
  - RCOM_multiple_sensor_point
  - Unknown

### Enum `SyncByte`

- Package: `rt_range.ethernet.eth_parser`
- Import: `from rt_range.ethernet import SyncByte`
- Purpose: Sync Byte definitions for distinguishing NCOM and RCOM
- Members:
  - NCOM
  - RCOM

### Class `Packet`

- Package: `rt_range.ethernet.rt_packet`
- Import: `from rt_range.ethernet.rt_packet import Packet`
- Purpose: RT-Range parseable Packet
- Members:
  - Method `decode(self, buffer: bytes) -> tuple[np.array, Selector]`

    Decodes bytes buffer with `np.dtype` to `np.array`
  - Method `get(self, obj: np.array, name: str, selector: Selector)`

    Decodes raw value using rules defined in packet structure
  - Method `translate(self, obj: np.array, selector: Selector) -> dict[str, ...]`

    Translates `np.array` into a dictionary
  - Method `parse(self, buffer: bytes) -> dict[str, ...]`

    Wrapper for decoding and translation
