from constants import FOOD, EMPTY, WALL

# Directions: right, left, down, up
DDX = [[0, 1], [0, -1], [1, 0], [-1, 0]]


def Thief_check(maze_map, row: int, col: int, height: int, width: int) -> bool:
    """Check if the thief can move to this position"""
    return (
        0 < row < height
        and 0 < col < width
        and (maze_map[row][col] == FOOD or maze_map[row][col] == EMPTY)
    )


def Police_check(maze_map, row: int, col: int, height: int, width: int) -> bool:
    """Check if the police can move to this position"""
    return 0 < row < height and 0 < col < width and maze_map[row][col] != WALL
