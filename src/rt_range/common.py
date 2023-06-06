from typing import Iterable


def flatten(iterable: Iterable):
    for item in iterable:
        if isinstance(item, Iterable) and not isinstance(item, (str, bytes)):
            yield from flatten(item)
        else:
            yield item
