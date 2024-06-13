# view/renderer.py
from maze_solver.models.maze import Maze
from maze_solver.models.border import Border
from maze_solver.models.square import Square

from dataclasses import dataclass 
from functools import cached_property

def Print_maze(maze: Maze)->None:
    
    for y in range(maze.height):
        line_top=''
        line_mid=''
        line_bot=''
        for x in range(maze.width):
            idx = y * maze.width + x
            border=maze[idx].border
            r=str(maze[idx].role.name)[:3]
            r= "YYY" if r == "EXT" else r
            r= "XXX" if r == "WAL" else r
            r= "   " if r == "NON" else r
            if border is Border.LEFT | Border.TOP | Border.RIGHT | Border.BOTTOM:
                line_top+=f'┌─────┐'
                line_mid+=f'│ {r} │'
                line_bot+=f'└─────┘'
            if border is Border.BOTTOM | Border.LEFT | Border.TOP:
                line_top+=f'┌──────'
                line_mid+=f'│ {r}  '
                line_bot+=f'└──────'
            if border is Border.LEFT | Border.TOP | Border.RIGHT:
                line_top+=f'┌─────┐'
                line_mid+=f'│ {r} │'
                line_bot+=f'│     │'
            if border is Border.TOP | Border.RIGHT | Border.BOTTOM:
                line_top+=f'──────┐'
                line_mid+=f'  {r} │'
                line_bot+=f'──────┘'
            if border is Border.RIGHT | Border.BOTTOM | Border.LEFT:
                line_top+=f'│     │'
                line_mid+=f'│ {r} │'
                line_bot+=f'└─────┘'
            if border is Border.LEFT | Border.TOP:
                line_top+=f'┌──────'
                line_mid+=f'│ {r}  '
                line_bot+=f'│      '
            if border is Border.TOP | Border.RIGHT:
                line_top+=f'──────┐'
                line_mid+=f'  {r} │'
                line_bot+=f'      │'
            if border is Border.BOTTOM | Border.LEFT:
                line_top+=f'│      '
                line_mid+=f'│ {r}  '
                line_bot+=f'└──────'
            if border is Border.RIGHT | Border.BOTTOM:
                line_top+=f'      │'
                line_mid+=f'  {r} │'
                line_bot+=f'──────┘'
            if border is Border.LEFT | Border.RIGHT:
                line_top+=f'│     │'
                line_mid+=f'│ {r} │'
                line_bot+=f'│     │'
            if border is Border.TOP | Border.BOTTOM:
                line_top+=f'───────'
                line_mid+=f'  {r}  '
                line_bot+=f'───────'
            if border is Border.TOP:
                line_top+=f'───────'
                line_mid+=f'  {r}  '
                line_bot+=f'       '
            if(border is Border.BOTTOM):
                line_top+=f'       '
                line_mid+=f'  {r}  '
                line_bot+=f'───────'
            if(border is Border.LEFT):
                line_top+=f'│      '
                line_mid+=f'│ {r}  '
                line_bot+=f'│      '
            if(border is Border.RIGHT):
                line_top+=f'      │'
                line_mid+=f'  {r} │'
                line_bot+=f'      │'

        print(line_top)
        print(line_mid)
        print(line_bot)


#====================================================================
#                             Test
#====================================================================
def test():
    from maze_solver.models.role import Role

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


    Print_maze(maze)




if __name__ == "__main__":
    test()
