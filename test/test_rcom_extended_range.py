from unittest import TestCase

from rt_range.ethernet.eth_parser import PacketType, EthernetParser
from rt_range.ethernet.rcom import RCOM_extended_range
from rt_range.ethernet.rt_packet import Packet


class TestRCOMExtendedRange(TestCase):
    def test_init(self):
        self.assertIsInstance(RCOM_extended_range, Packet)

    def test_parse(self):
        sample_packet = b'\x57\x02\x00\x00\x00\x00\x01\x01\x10\x27\x00\x00\x20\x4e\x00\x00\x64\x00\xc8\x00' \
                        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x3a\x01\x16\x01\x00' \
                        b'\x11\x56\x13\x58\x07\x00\x00\xdc\x05' \
                        b'\x64\x00\xc8\x00\x64\x00\xc8\x00\x00\x00\x64\x00\x00\x00\x00\x00\x00\x00\x00\x00\x64\xc8\x64\xc8' \
                        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                        b'\x0a\x00\x14\x00\x0a\x00\x14\x00' \
                        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                        b'\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00'
        expected_values = (
            0x57, 2, 0, 0.0, 1, 1, 10.0, 20.0, 1.0, 2.0,
            0.0, 0.0, 0.0, 0.0, 3.14, 2.78, 0,
            'Target_vehicle_geometry', 4.95, 1.88, 0, 1.5,
            1.0, 2.0, 1.0, 2.0, 0, 0, 100, 0, 0, 0, 0, 0, 0, 0, 0, 0.4, 0.8, 0.4, 0.8,
            0, 0, 0, 0, 0, 0, 0, 0,
            0.1, 0.2, 0.1, 0.2,
            0.0, 0, 0, 0.0, 0, 0, 0.0, 0, 0, 0.0, 0, 0, 0.0, 0, 0, 0.0, 0, 0,
            0.0, 0, 0, 0.0, 0, 0, 0.0, 0, 0, 0.0, 0, 0, 0.0, 0, 0, 0.0, 0, 0, 0,
        )
        parsed_data = EthernetParser.parse_rt_ethernet(sample_packet, PacketType.RCOM_extended_range)
        for expected_value, parsed_value in zip(expected_values, parsed_data.values()):
            self.assertEqual(expected_value, parsed_value)
