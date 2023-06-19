from typing import Iterable


def convert_10_pow_m1(value: int):
    return value / 10


def convert_10_pow_m2(value: int):
    return value / 100


def convert_10_pow_m3(value: int):
    return value / 1000


def convert_10_pow_m4(value: int):
    return value / 10000


def convert_10_pow_m5(value: int):
    return value / 100000


def convert_10_pow_m6(value: int):
    return value / 1000000


def convert_10_pow_m7(value: int):
    return value / 10000000


def validity_bit0(value: int):
    return value & 0x7f


def flatten(iterable: Iterable):
    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item
