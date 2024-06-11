# models/role.py

from enum import IntEnum, auto

class Role(IntEnum):
    NONE = 0
    ENEMY = auto()
    ENTRANCE = auto()
    EXIT = auto()
    EXTERIOR = auto()
    REWARD = auto()
    WALL = auto()

def test():
    pp(f'{str(Role.ENEMY.name)[:4]=}')
    for key in Role:
        pp(f'{key=}')


if __name__ == "__main__":
    from pprint import pp
    test()