from unittest import TestCase

from rt_range.ethernet.rt_packet import Packet
from rt_range.ethernet.rt_types import Field, VariableBlock
from rt_range.ethernet.rt_types import UByte


class MockPacket(Packet):
    def __init__(self):  # noqa
        pass


class TestPacket(TestCase):
    def test_get_blocks_and_selectors(self):
        test_packet = MockPacket()
        test_packet._raw_structure = (
            Field('test_field_0', UByte),
            Field('test_field_1', UByte),
            VariableBlock(selector=0, size=0, structure={}),
            VariableBlock(selector=1, size=0, structure={}),
            Field('test_field_2', UByte),
        )
        test_packet._get_blocks_and_selectors()
        self.assertEqual(test_packet._blocks, (
            test_packet._raw_structure[2],
            test_packet._raw_structure[3],
        ))
        self.assertEqual(test_packet._selectors, (0, 1))

    def test_parse_fields(self):
        test_packet = MockPacket()
        test_packet._raw_structure = (
            Field('test_field_0', UByte),
            VariableBlock(selector=0, size=2, structure={
                0: [Field('inner_test_field_0_0_0', UByte),
                    Field('inner_test_field_0_0_1', UByte)],
                1: [Field('inner_test_field_0_1_0', UByte),
                    Field('inner_test_field_0_1_1', UByte)],
            }),
            Field('test_field_1', UByte),
            VariableBlock(selector=0, size=2, name='test_block', structure={
                0: [Field('inner_test_field_1_0_0', UByte),
                    Field('inner_test_field_1_0_1', UByte)],
                1: [Field('inner_test_field_1_1_0', UByte),
                    Field('inner_test_field_1_1_1', UByte)],
            }),
        )
        expected_fields = {
            None: (
                Field('test_field_0', UByte),
                test_packet._raw_structure[1].default,
                Field('test_field_1', UByte),
                test_packet._raw_structure[3].default,
            ),
            (0, 0): (
                Field('test_field_0', UByte),
                Field('inner_test_field_0_0_0', UByte),
                Field('inner_test_field_0_0_1', UByte),
                Field('test_field_1', UByte),
                Field('test_block_inner_test_field_1_0_0', UByte),
                Field('test_block_inner_test_field_1_0_1', UByte),
            ),
            (0, 1): (
                Field('test_field_0', UByte),
                Field('inner_test_field_0_0_0', UByte),
                Field('inner_test_field_0_0_1', UByte),
                Field('test_field_1', UByte),
                Field('test_block_inner_test_field_1_1_0', UByte),
                Field('test_block_inner_test_field_1_1_1', UByte),
            ),
            (1, 0): (
                Field('test_field_0', UByte),
                Field('inner_test_field_0_1_0', UByte),
                Field('inner_test_field_0_1_1', UByte),
                Field('test_field_1', UByte),
                Field('test_block_inner_test_field_1_0_0', UByte),
                Field('test_block_inner_test_field_1_0_1', UByte),
            ),
            (1, 1): (
                Field('test_field_0', UByte),
                Field('inner_test_field_0_1_0', UByte),
                Field('inner_test_field_0_1_1', UByte),
                Field('test_field_1', UByte),
                Field('test_block_inner_test_field_1_1_0', UByte),
                Field('test_block_inner_test_field_1_1_1', UByte),
            ),
        }
        test_packet._get_blocks_and_selectors()
        test_packet._parse_fields()
        self.maxDiff = None
        self.assertDictEqual(test_packet._fields, expected_fields)

    def test_init(self):
        instance = Packet([Field('test_field', UByte)])
        self.assertIsInstance(instance, Packet)

    def setUp(self) -> None:
        self.test_packet = Packet([
            Field('test_field', UByte),
            VariableBlock(selector=0, name='inner_field', size=1, structure={
                0: [Field('inner_test_field_0', UByte)],
                1: [Field('inner_test_field_1', UByte)],
            }),
        ])

    def test_parse(self):
        test_buffers = (
            b'\0\x57',
            b'\1\xe7',
        )
        expected_results = (
            {'test_field': 0, 'inner_field_inner_test_field_0': 0x57},
            {'test_field': 1, 'inner_field_inner_test_field_1': 0xe7},
        )
        for buffer, expected_result in zip(test_buffers, expected_results):
            self.assertEqual(self.test_packet.parse(buffer), expected_result)

    def test_default_field(self):
        test_buffer = b'\3\x69'
        expected_result = {'test_field': 3, 'inner_field': 'Parser_not_implemented'}
        self.assertEqual(self.test_packet.parse(test_buffer), expected_result)
