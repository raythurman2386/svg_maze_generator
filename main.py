from df_maze import Maze

# Maze dimensions (ncols, nrows)
nx, ny = 20, 15
# Maze entry position
ix, iy = 10, 0

maze = Maze(nx, ny, ix, iy)
maze.make_maze()

print(maze)
maze.write_svg('maze.svg')
