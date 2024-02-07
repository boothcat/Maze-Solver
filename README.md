# Maze-Solver
## Setting up the Maze
Function maze_solver uses a breadth first search graph traversal algorithm to solve a 2D maze represented by a mxn (m rows, n columns) matrix. Each matrix index is either empty (represented by a '-') or a barrier (represented by a '#'). Only the left, right, up, and down directions are valid moves when solving the maze.  The goal is to solve the maze from the source to destination point in the fewest moves. An example maze is shown below.

![image](https://github.com/boothcat/Maze-Solver/assets/97126252/9e31a12c-007a-4ed3-b206-22166c6a4266)

In python, this maze is represented as a list of lists. Uppermost left coordinate is (0,0) and bottommost right coordinate is (M,N).
![image](https://github.com/boothcat/Maze-Solver/assets/97126252/8e104c70-f014-4b7f-8da4-423e973dfa9d)

## Function maze_solver
* Function maze_solver - takes a source coordinate (represented as a tuple), a destination coordinate (represented as a tuple), and a maze as parameters. 
    * If a path is possible, the function returns the solution as a list with two elements:
        * The first element in the solution is a list of coordinates representing the path from source to destination.
        * The second element in the solution is a string of characters representing the directions to take from source to destination. (U = up, D = Down, L = Left, R = Right).

## Example Solutions
At the end of code file, are example mazes showing maze_solver's solutions.
![image](https://github.com/boothcat/Maze-Solver/assets/97126252/27d0df24-22b5-4b97-9faa-68be668b977a)

If no paths are available, maze_solver returns None.  If multiple paths are available, maze_solver selects the path with fewest moves. 
![image](https://github.com/boothcat/Maze-Solver/assets/97126252/e872714d-7c66-42db-9633-f6989998daee)

## Algorithm Description
To solve the maze, the maze cells can be treated as a graph with ‘-‘ positions representing vertices.   Starting with the given source coordinate, we perform a breadth first search using a queue data structure.   The breadth first search provides the shortest path from source to destination.  Starting with the source, we determine all valid non-obstacle neighbors (up, down, left, right) and keep track of the direction moved to that neighbor with a moves dictionary.  Example: moves[0,0] = {(0,1): R, (1,0):D}.  This example shows the valid neighbors of coordinate (0,0) and the directions travelled to reach those neighbors.  We use a 2D parent array with the same dimensions as the puzzle initialized to None to keep track of the parent vertex of each visited vertex.  Similarly, a 2D Boolean visited array initialized to False keeps track of all visited vertices.  Whenever an unvisited neighbor vertex is added to the breadth first search queue, the neighbor’s parent is set to the current vertex so we can look it up later to construct the path.  When either the destination is reached or all vertices are visited, the search concludes.  Starting with the destination, a helper function path_finder recursively looks up the parent vertex and direction moved until the source is reached.  This generates the list of indices and string of directions used to solve the puzzle.       

## Time Complexity Analysis
Building the mxn 2D array to keep track of parent and visited vertices takes O(mn).  The find_neighbors helper function has a time complexity of O(1) since it is only assigning and looking up values.  The breadth first search has a time complexity of O(V+E), V = vertices, E = edges. Since the maze is an mxn grid, this means that there are at most mn vertices and 2mn-m-n edges.  This gives a time complexity of O(mn+2mn-m-n) which reduces to O(mn).  The path_finder helper functions at worst make mn recursive calls to look up the parent of each vertex in the path.  This gives an overall time complexity of O(mn). 




