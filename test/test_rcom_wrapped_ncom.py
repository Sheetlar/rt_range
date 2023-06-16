from unittest import TestCase

from rt_range.ethernet.eth_parser import EthernetParser, PacketType
from rt_range.ethernet.rcom import RCOM_wrapped_NCOM
from rt_range.ethernet.rt_packet import Packet


class TestNCOM(TestCase):
    def test_init(self):
        self.assertIsInstance(RCOM_wrapped_NCOM, Packet)

    def test_parse(self):
        sample_packet = b'\x57\x03\x00\x00\xc3\x00\x00\x01\x00' \
                        b'\xe7\x00\x00\x50\xc3\x00\xd0\x07\x00\xca\x80\xfe\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                        b'\x04\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00\x00' \
                        b'\xa8\x7a\x00\x98\x6c\x00\x01\x00\x00\xd2\x04\x00\x7b\x00\x00\x41\x01\x00\x00\x00' \
                        b'\x00\x00\x00\x00\x0f\x06\x06\x06\x00\x00'
        expected_values = (
            0x57, 3, 0, 195, 0, 0, 1, 0,
            0xe7, 0, 5.0, 0.2, -9.8102, 0, 0, 0,
            'Locked', 0, 0.0, 0.0, 0.0,
            3.14, 2.78, 0.0001, 0.001234, 0.000123, 0.000321, 0, 'Time_satellites_mode',
            0, 15, 'RTK_Integer', 'RTK_Integer', 'RTK_Integer', 0, 0,
        )
        parsed_data = EthernetParser.parse_rt_ethernet(sample_packet, PacketType.RCOM_wrapped_NCOM)
        for expected_value, parsed_value in zip(expected_values, parsed_data.values()):
            self.assertEqual(expected_value, parsed_value)
