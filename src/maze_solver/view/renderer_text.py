# view/renderer.py
from maze_solver.models.maze import Maze
from maze_solver.models.border import Border


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



