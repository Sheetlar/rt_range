from unittest import TestCase

from rt_range.ethernet.eth_parser import PacketType, EthernetParser
from rt_range.ethernet.rcom import RCOM_lane
from rt_range.ethernet.rt_packet import Packet


class TestRCOMLane(TestCase):
    def test_init(self):
        self.assertIsInstance(RCOM_lane, Packet)

    def test_parse(self):
        sample_packet = b'\x57\x01\x00\x00\x00\x00\x01\x02\x40\x9c\x00\x00\x2e\xfb\x7b\x00\xbf\xfe\xd0\x07\x0c\x00\x66\x00' \
                        b'\xe8\x03\xd0\x07\xb8\x0b\xa0\x0f\x88\x13\x70\x17\x58\x1b\x40\x1f\x57\x04\xae\x08\x01\x02\x03\x04\x00' \
                        b'\x08\x32\xfb\xff\x34\x08\x00\x0c\xfe' \
                        b'\xe8\x03\xd0\x07\xb8\x0b\xa0\x0f\x88\x13\x70\x17\x58\x1b\x40\x1f\xe8\x03\xd0\x07\xb8\x0b\xa0\x0f\x88\x13\x70\x17\x58\x1b\x40\x1f' \
                        b'\xe8\x03\xd0\x07\xb8\x0b\xa0\x0f\x88\x13\x70\x17\x58\x1b\x40\x1f\xe8\x03\xd0\x07\xb8\x0b\xa0\x0f\x88\x13\x70\x17\x58\x1b\x40\x1f' \
                        b'\xe8\x03\xd0\x07\xb8\x0b\x3a\x01\x16\x01\x00'
        expected_values = (
            0x57, 1, 0, 0.0, 1, 2, 40.0, -1.234, 1.23, -3.21, 2.0, 0.12, 1.02,
            1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 1.111, 2.222, 1, 2, 3, 4, 0,
            'Point_A_lever-arm', -1.23, 2.1, -0.5,
            10.0, 20.0, 30.0, 40.0, 50.0, 60.0, 70.0, 80.0, 1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0,
            1.0, 2.0, 3.0, 4.0, 5.0, 6.0, 7.0, 8.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8,
            0.1, 0.2, 0.3, 3.14, 2.78, 0,
        )
        parsed_data = EthernetParser.parse_rt_ethernet(sample_packet, PacketType.RCOM_lane)
        for expected_value, parsed_value in zip(expected_values, parsed_data.values()):
            self.assertEqual(expected_value, parsed_value)
