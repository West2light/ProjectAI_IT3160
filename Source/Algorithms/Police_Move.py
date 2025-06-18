from queue import PriorityQueue
from Extension.extension import Manhattan, DDX, Police_check


class AStarPoliceAgent:
    def __init__(self):
        self.maze_map = None
        self.height = 0
        self.width = 0
        self.cells_visited = None
        self.path_tracker = None
        self.path_cost = None
        
    def initialize(self, maze_map, height, width):
        self.maze_map = maze_map
        self.height = height
        self.width = width
        self.cells_visited = [[False for _ in range(width)] for _ in range(height)]
        self.path_tracker = {}
        self.path_cost = {}
        
    def heuristic(self, current_row, current_col, target_row, target_col):
        return Manhattan(current_row, current_col, target_row, target_col)
        
    def get_valid_adjacent_positions(self, row, col):
        valid_positions = []
        
        for [direction_row, direction_col] in DDX:
            next_row, next_col = row + direction_row, col + direction_col
            if Police_check(self.maze_map, next_row, next_col, self.height, self.width) and not self.cells_visited[next_row][next_col]:
                valid_positions.append((next_row, next_col))
                
        return valid_positions
        
    def reconstruct_path(self, start_position, target_position):
        path = []
        current_position = target_position
        
        while current_position in self.path_tracker:
            path.append([current_position[0], current_position[1]])
            current_position = self.path_tracker[current_position]
            
        path.append([current_position[0], current_position[1]])
        
        path.reverse()
        
        return path[1] if len(path) > 1 else [start_position[0], start_position[1]]
        
    def run_astar(self, start_row, start_col, target_row, target_col):

        self.cells_visited = [[False for _ in range(self.width)] for _ in range(self.height)]
        self.path_tracker = {}
        self.path_cost = {}
        
        start_position = (start_row, start_col)
        target_position = (target_row, target_col)
        
        self.path_cost[start_position] = 0
        priority_queue = PriorityQueue()
        priority_queue.put((self.heuristic(start_row, start_col, target_row, target_col), start_position))
        
        while not priority_queue.empty():

            current_position = priority_queue.get()[1]
            current_row, current_col = current_position
            
            self.cells_visited[current_row][current_col] = True
            
            if current_position == target_position:
                return self.reconstruct_path(start_position, target_position)
                
            for next_position in self.get_valid_adjacent_positions(current_row, current_col):
                next_row, next_col = next_position
                
                new_cost = self.path_cost[current_position] + 1
                
                if next_position not in self.path_cost or new_cost < self.path_cost[next_position]:

                    self.path_cost[next_position] = new_cost

                    f_score = new_cost + self.heuristic(next_row, next_col, target_row, target_col)
                    
                    priority_queue.put((f_score, next_position))
                    self.path_tracker[next_position] = current_position

        return [start_row, start_col]


def move_police_using_astar(maze_map, start_row, start_col, end_row, end_col, height, width):
    agent = AStarPoliceAgent()
    agent.initialize(maze_map, height, width)
    return agent.run_astar(start_row, start_col, end_row, end_col)