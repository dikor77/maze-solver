# models/border.py

from enum import IntFlag, auto

class Border(IntFlag):
    EMPTY = 0
    TOP = auto()
    BOTTOM = auto()
    LEFT = auto()
    RIGHT = auto()

    @property
    def corner(self) -> bool:
        return self in (
            self.TOP | self.LEFT,
            self.TOP | self.RIGHT,
            self.BOTTOM | self.LEFT,
            self.BOTTOM | self.RIGHT,
        )

    @property
    def dead_end(self) -> bool:
        return self.bit_count() == 3

    @property
    def intersection(self) -> bool:
        return self.bit_count() < 2


def test():
    border = Border.TOP | Border.BOTTOM | Border.RIGHT
    pp(f'{border=}')
    pp(f'{border.name=}')
    pp(f'{border.value=}')
    pp(f'{Border.TOP in border=}')
    pp(f'{border is Border.TOP=}')
    pp(f'{border.corner=}')
    pp(f'{border.dead_end=}')
    pp(f'{border.intersection=}')


if __name__ == "__main__":
    from pprint import pp
    test()