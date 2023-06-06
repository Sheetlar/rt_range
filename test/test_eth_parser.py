from unittest import TestCase
from rt_range.ethernet.eth_parser import PacketType, EthernetParser


class MockPacketType:
    def __init__(self):
        self.name = self.__class__.__name__


class TestEthernetParser(TestCase):
    def test_identify_packet_type_valid(self):
        for name, packet_type in vars(PacketType).items():
            if name.startswith('_'):
                continue
            packet = packet_type.value.to_bytes(2) + b'\x11\x22'
            identified_type = EthernetParser._identify_packet_type(packet)
            self.assertEqual(identified_type, packet_type)

    def test_identify_packet_type_invalid(self):
        invalid_packet = b'\x11\x22\x33\x44'
        with self.assertRaises(ValueError):
            EthernetParser._identify_packet_type(invalid_packet)

    def test_get_parser_identify_valid(self):
        for packet_type, parser in EthernetParser._parsers.items():
            packet = packet_type.value.to_bytes(2) + b'\x11\x22'
            got_parser = EthernetParser._get_parser(packet, None)
            self.assertEqual(got_parser, parser)

    def test_get_parser_valid_type_passed(self):
        for packet_type, parser in EthernetParser._parsers.items():
            packet = b'\0\0\0\0'
            got_parser = EthernetParser._get_parser(packet, packet_type)
            self.assertEqual(got_parser, parser)

    def test_get_parser_identify_invalid(self):
        invalid_packet = b'\x11\x22\x33\x44'
        with self.assertRaises(ValueError):
            EthernetParser._get_parser(invalid_packet, None)

    def test_get_parser_invalid_type_passed(self):
        packet = b'\0\0\0\0'
        with self.assertRaises(NotImplementedError):
            EthernetParser._get_parser(packet, MockPacketType())  # noqa
