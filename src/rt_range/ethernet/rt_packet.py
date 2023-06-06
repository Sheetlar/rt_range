import itertools
from copy import deepcopy

import numpy as np

from rt_range.ethernet.rt_types import Field, VariableBlock, Selector, Structure, ValueConvertFunc


class Packet:
    def __init__(self, fields: Structure):
        self._raw_structure = fields
        self._get_blocks_and_selectors()
        self._parse_fields()
        self._structure: dict[Selector, np.dtype] = {
            selector: np.dtype([(field.name, field.dtype) for field in structure])
            for selector, structure in self._fields.items()}
        self._decoder: dict[Selector, dict[str, ValueConvertFunc]] = {
            selector: {field.name: field.get_value for field in fields}
            for selector, fields in self._fields.items()}

    def _get_blocks_and_selectors(self):
        self._blocks = tuple(filter(
            lambda e: isinstance(e, VariableBlock),
            self._raw_structure),
        )
        self._selectors = tuple(block.selector for block in self._blocks)

    def _parse_fields(self):
        def wrap_name(field: Field, block: VariableBlock):
            field = deepcopy(field)
            if block.name is not None:
                field.name = f'{block.name}_{field.name}'
            return field

        def make_struct(selector: Selector):
            for struct_field in self._raw_structure:
                if isinstance(struct_field, Field):
                    yield struct_field
                else:
                    yield from (wrap_name(f, struct_field)
                                for f in struct_field.structure[selector[self._blocks.index(struct_field)]])

        self._fields: dict[Selector, tuple[Field, ...]] = {
            selector: tuple(make_struct(selector))
            for selector in itertools.product(*(block.structure for block in self._blocks))}
        self._append_default()

    def _append_default(self):
        self._fields[None] = tuple(field if isinstance(field, Field) else field.default
                                   for field in self._raw_structure)

    def _get_selector(self, buffer: bytes) -> Selector:
        return tuple(buffer[s] for s in self._selectors)

    def decode(self, buffer: bytes) -> tuple[np.array, Selector]:
        selector = self._get_selector(buffer)
        if selector not in self._structure:
            selector = None
        return np.frombuffer(buffer, dtype=self._structure[selector]), selector

    def get(self, obj: np.array, name: str, selector: Selector):
        return self._decoder[selector][name](obj[name][0])

    def translate(self, obj: np.array, selector: Selector) -> dict[str, ...]:
        return {field.name: self.get(obj, field.name, selector) for field in self._fields[selector]}

    def parse(self, buffer: bytes) -> dict[str, ...]:
        return self.translate(*self.decode(buffer))
