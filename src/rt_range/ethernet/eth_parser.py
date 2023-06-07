from enum import Enum

from rt_range.ethernet.ncom import NCOM
from rt_range.ethernet.rcom import RCOM_lane, RCOM_extended_range
from rt_range.ethernet.rt_packet import Packet


class PacketType(Enum):
    NCOM = 0xE700
    RCOM_lane = 0x5701
    RCOM_extended_range = 0x5702
    RCOM_wrapped_NCOM = 0x5703
    RCOM_trigger_time = 0x5704
    RCOM_polygon = 0x5705
    RCOM_multiple_sensor_point = 0x5706


class EthernetParser:
    _parsers: dict[PacketType, Packet] = {
        PacketType.NCOM: NCOM,
        PacketType.RCOM_lane: RCOM_lane,
        PacketType.RCOM_extended_range: RCOM_extended_range,
    }

    @classmethod
    def parse_rt_ethernet(cls, buffer: bytes, packet_type: PacketType | None = None):
        packet_parser = cls._get_parser(buffer, packet_type)
        return packet_parser.parse(buffer)

    @classmethod
    def _get_parser(cls, buffer: bytes, packet_type: PacketType | None):
        if packet_type is None:
            packet_type = cls._identify_packet_type(buffer)
        try:
            packet_parser = cls._parsers[packet_type]
        except KeyError:
            raise NotImplementedError(f'Parser for packet "{packet_type.name}" is not yet implemented')
        return packet_parser

    @staticmethod
    def _identify_packet_type(buffer: bytes) -> PacketType:
        paket_type = int.from_bytes(buffer[:2], byteorder='big')
        if paket_type & 0xFF00 == PacketType.NCOM:
            return PacketType.NCOM
        for k, v in vars(PacketType).items():
            if k.startswith('_'):
                continue
            if paket_type == v.value:
                return v
        raise ValueError('Unknown packet type')
