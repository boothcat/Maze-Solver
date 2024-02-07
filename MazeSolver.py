# Catherine Booth
# Description:  Function solve_maze returns the path represented as a list of tuples
#               containing indices from given source to given destination to solve the
#               maze.

from collections import defaultdict
from collections import deque


def solve_maze(Board, Source, Destination):
    """Given a 2D maze puzzle, a source, and destination, function returns
    the solution path of the maze as a list of tuples containing indices and a string of
    directions to move from source to destination. Return [] for unsolvable maze."""

    rows = len(Board)
    columns = len(Board[0])

    # 2D matrices to keep track of visited indices, parents
    visited = [[False for m in range(columns)] for n in range(rows)]
    parents = [[None for m in range(columns)] for n in range(rows)]

    # Dictionary to keep track of the direction and coordinate moved from one position to another
    moves = defaultdict(dict)

    # Add source to the queue and mark as visited
    a, b = Source
    queue = deque()
    queue.append(Source)
    visited[a][b] = True

    while len(queue) > 0:
        # Get node to visit from the queue
        current_vertex = queue.popleft()
        a, b = current_vertex

        # If node is destination, return path
        if current_vertex == Destination:
            return path_finder(parents, Destination, Source, moves)

        # Find neighbors
        find_neighbors(current_vertex, Board, rows, columns, moves)

        # Add unvisited neighbors to the queue, update parent matrix
        for neighbor, direction in moves[current_vertex].items():
            i, j = neighbor
            if visited[i][j] is False:
                parents[i][j] = current_vertex
                queue.append((i, j))
                visited[i][j] = True

            # Check if destination has been reached
            if neighbor == Destination:
                return path_finder(parents, Source, Destination, moves)


def find_neighbors(vertex, Board, rows, columns, moves):
    """Helper function finds all valid neighbors and keeps track of the direction
    to move to that neighbor."""
    i, j = vertex
    left = j-1
    right = j+1
    down = i+1
    up = i-1

    # Check for valid left, right, up, down neighbors
    if 0 <= left < columns and Board[i][left] == '-':
        moves[i, j][i, left] = 'L'

    if 0 <= right < columns and Board[i][right] == '-':
        moves[i, j][(i, right)] = 'R'

    if 0 <= down < rows and Board[down][j] == '-':
        moves[i, j][down, j] = 'D'

    if 0 <= up < rows and Board[up][j] == '-':
        moves[i, j][up, j] = 'U'


def path_finder(parents, Source, Destination, moves, path=None, moves_string=None):
    """Helper function returns a list of the solution indices from source to destination
    and the string of directions to move from source to destination."""
    if moves_string is None:
        moves_string = ""
    if path is None:
        path = []

    # Add node to the path and stop recursion once source is reached.
    path.append(Destination)
    if Destination == Source:
        return path[::-1], moves_string[::-1]

    # Look up next node and add direction taken
    x, y = Destination
    parent_node = parents[x][y]
    moves_string += moves[parent_node][Destination]

    # Recursive call to generate path
    return path_finder(parents, Source, parent_node, moves, path, moves_string)


if __name__ == '__main__':

    maze1 = [
        ['-', '-', '-', '-', '-'],
        ['-', '#', '-', '#', '#'],
        ['-', '#', '-', '-', '-'],
        ['#', '-', '-', '#', '-'],
    ]
    print("Maze 1")
    for row in maze1:
        print(row)
    print("The path from starting point (0,0) to destination point (2,3) is: ")
    print(solve_maze(maze1, (0, 0), (2, 3)), '\n')
    print("The path from starting point (2,4) to destination point (2,0) is: ")
    print(solve_maze(maze1, (2, 4), (2, 0)), '\n')

    maze2 = [
        ['-', '-', '#', '-', '-'],
        ['-', '-', '-', '#', '-'],
        ['-', '#', '-', '-', '#'],
        ['-', '-', '-', '#', '-'],
        ['-', '-', '-', '#', '#'],
    ]
    print("Maze 2")
    for row in maze2:
        print(row)

    print("The path from starting point (0,0) to destination point (4,3) is:")
    print(solve_maze(maze2, (0, 0), (4, 3)), '\n')
    print("The path from starting point (0,0) to destination point (3,2) is:")
    print(solve_maze(maze2, (0, 0), (3, 2)), '\n')
