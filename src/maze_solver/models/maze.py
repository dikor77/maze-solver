# models/maze.py

from dataclasses import dataclass
from functools import cached_property
from typing import Iterator
from pathlib import Path

from maze_solver.models.role import Role
from maze_solver.models.square import Square
from maze_solver.models.border import Border
from maze_solver.persistence.serializer import (
    dump_squares,
    load_squares,
)

@dataclass(frozen=True)
class Maze:
    squares: tuple[Square, ...]

    @classmethod
    def load(cls, path: Path) -> "Maze":
        return Maze(tuple(load_squares(path)))
    
    def dump(self, path: Path) -> None:
        dump_squares(self.width, self.height, self.squares, path)

    def __post_init__(self) -> None:
        validate_indices(self)
        validate_rows_columns(self)
        validate_entrance(self)
        validate_exit(self)

    def __iter__(self) -> Iterator[Square]:
        return iter(self.squares)

    def __getitem__(self, index: int) -> Square:
        return self.squares[index]
    
    @cached_property
    def width(self):
        return max(square.column for square in self) + 1

    @cached_property
    def height(self):
        return max(square.row for square in self) + 1
    
    @cached_property
    def entrance(self) -> Square:
        return next(sq for sq in self if sq.role is Role.ENTRANCE)

    @cached_property
    def exit(self) -> Square:
        return next(sq for sq in self if sq.role is Role.EXIT)
    
#====================================================================
#                  maze validation function
#====================================================================
def validate_indices(maze: Maze) -> None:
    assert [square.index for square in maze] == list(range(len(maze.squares))), "Wrong square.index"

def validate_rows_columns(maze: Maze) -> None:
    for y in range(maze.height):
        for x in range(maze.width):
            square = maze[y * maze.width + x]
            assert square.row == y, "Wrong square.row"
            assert square.column == x, "Wrong square.column"

def validate_entrance(maze: Maze) -> None:
    assert 1 == sum(1 for square in maze if square.role is Role.ENTRANCE), "Must be exactly one entrance"

def validate_exit(maze: Maze) -> None:
    assert 1 == sum(1 for square in maze if square.role is Role.EXIT), "Must be exactly one exit"


#====================================================================
#                             Test
#====================================================================
def test():
    from maze_solver.view.renderer_text import Print_maze
    from maze_solver.view.renderer_text import MazeTextContainer

    maze = Maze(
        squares=(
            Square(0, 0, 0, Border.TOP | Border.LEFT),
            Square(1, 0, 1, Border.TOP | Border.RIGHT),
            Square(2, 0, 2, Border.LEFT | Border.RIGHT, role=Role.EXIT),
            Square(3, 0, 3, Border.TOP | Border.LEFT | Border.RIGHT),
            Square(4, 1, 0, Border.BOTTOM | Border.LEFT | Border.RIGHT),
            Square(5, 1, 1, Border.LEFT | Border.RIGHT),
            Square(6, 1, 2, Border.BOTTOM | Border.LEFT),
            Square(7, 1, 3, Border.RIGHT),
            Square(8, 2, 0, Border.TOP | Border.LEFT, role=Role.ENTRANCE),
            Square(9, 2, 1, Border.BOTTOM),
            Square(10, 2, 2, Border.TOP | Border.BOTTOM),
            Square(11, 2, 3, Border.BOTTOM | Border.RIGHT),
        )
    )

    maze_text = MazeTextContainer(maze)


    maze_text.Print()




if __name__ == "__main__":
    test()