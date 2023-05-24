from unittest import TestCase

from rt_range.ethernet.rt_packet import Packet
from rt_range.ethernet.rt_types import Field, VariableBlock
from rt_range.ethernet.rt_types import UByte


class FakePacket(Packet):
    def __init__(self):  # noqa
        pass


class TestPacket(TestCase):
    def test_get_blocks_and_selectors(self):
        test_packet = FakePacket()
        test_packet._raw_structure = (
            Field('test_field_0', UByte),
            Field('test_field_1', UByte),
            VariableBlock(selector=0, structure={}),
            VariableBlock(selector=1, structure={}),
            Field('test_field_2', UByte),
        )
        test_packet._get_blocks_and_selectors()
        self.assertEqual(test_packet._blocks, (
            test_packet._raw_structure[2],
            test_packet._raw_structure[3],
        ))
        self.assertEqual(test_packet._selectors, (0, 1))  # noqa

    def test_parse_fields(self):
        test_packet = FakePacket()
        test_packet._raw_structure = (
            Field('test_field_0', UByte),
            VariableBlock(selector=0, structure={
                0: [Field('inner_test_field_0_0_0', UByte),
                    Field('inner_test_field_0_0_1', UByte)],
                1: [Field('inner_test_field_0_1_0', UByte),
                    Field('inner_test_field_0_1_1', UByte)],
            }),
            Field('test_field_1', UByte),
            VariableBlock(selector=0, name='test_block', structure={
                0: [Field('inner_test_field_1_0_0', UByte),
                    Field('inner_test_field_1_0_1', UByte)],
                1: [Field('inner_test_field_1_1_0', UByte),
                    Field('inner_test_field_1_1_1', UByte)],
            }),
        )
        expected_fields = {
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
            VariableBlock(selector=0, structure={
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
            {'test_field': 0, 'inner_test_field_0': 0x57},
            {'test_field': 1, 'inner_test_field_1': 0xe7},
        )
        for buffer, expected_result in zip(test_buffers, expected_results):
            self.assertEqual(self.test_packet.parse(buffer), expected_result)
