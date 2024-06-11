# models/square.py

from dataclasses import dataclass

from maze_solver.models.border import Border
from maze_solver.models.role import Role

@dataclass(frozen=True)
class Square:
    index: int
    row: int
    column: int
    border: Border
    role: Role = Role.NONE



def test():
    cell = Square(1,1,1,Border.BOTTOM|Border.TOP,Role.ENTRANCE)
    pp(f'{cell=}')



if __name__ == "__main__":
    from pprint import pp
    test()