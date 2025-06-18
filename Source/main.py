import sys
import pygame
import random

from Algorithms.SearchAlgorithms import SearchAlgorithms
from Object.Food import Food
from Object.Player import Player
from Object.Wall import Wall
from constants import *
from Object.Menu import Menu, Button


class GameState:
    def __init__(self):
        self.height = 0
        self.width = 0
        self.score = 0
        self.thief_animation_state = 0
        self.maze_map = []
        self.wall_objects = []
        self.road_objects = []
        self.food_objects = []
        self.police_objects = []
        self.food_positions = []
        self.police_positions = []
        self.visit_counter = []
        self.thief_player = None
        self.current_level = 1
        self.map_file_path = ""
        self.game_end_done = False
        
    def reset(self):
        self.height = 0
        self.width = 0
        self.score = 0
        self.thief_animation_state = 0
        self.maze_map = []
        self.wall_objects = []
        self.road_objects = []
        self.food_objects = []
        self.police_objects = []
        self.food_positions = []
        self.police_positions = []


class GameManager:
    def __init__(self):
        pygame.init()
        pygame.font.init()
        
        self.state = GameState()
        self.screen = pygame.display.set_mode((WIDTH, HEIGHT))
        pygame.display.set_caption('Thief')
        self.clock = pygame.time.Clock()
        self.game_font = pygame.font.SysFont('Comic Sans MS', 30)
        self.large_font = pygame.font.SysFont('Comic Sans MS', 100)
    def load_map_from_file(self, map_name):
        f = open(map_name, "r")
        x = f.readline().split()
        
        self.state.maze_map = []
        self.state.height, self.state.width = int(x[0]), int(x[1])
        
        for _ in range(self.state.height):
            line = f.readline().split()
            map_row = []
            for j in range(self.state.width):
                map_row.append(int(line[j]))
            self.state.maze_map.append(map_row)

        x = f.readline().split()
        MARGIN["TOP"] = max(0, (HEIGHT - self.state.height * SIZE_WALL) // 2)
        MARGIN["LEFT"] = max(0, (WIDTH - self.state.width * SIZE_WALL) // 2)
        self.state.thief_player = Player(int(x[0]), int(x[1]), IMAGE_THIEF[0])
        f.close()
        
    def process_map_object(self, row, col):
        if self.state.maze_map[row][col] == WALL:
            self.state.wall_objects.append(Wall(row, col, BLUE))

        if self.state.maze_map[row][col] == FOOD:
            self.state.food_objects.append(Food(row, col, BLOCK_SIZE, BLOCK_SIZE, YELLOW))
            self.state.food_positions.append([row, col])

        if self.state.maze_map[row][col] == POLICE:
            police_img = IMAGE_POLICE[len(self.state.police_objects) % len(IMAGE_POLICE)]
            self.state.police_objects.append(Player(row, col, police_img))
            self.state.police_positions.append([row, col])
            
    def initialize_game_data(self):
        self.state.reset()
        
        self.load_map_from_file(map_name=self.state.map_file_path)
        self.state.visit_counter = [[0 for _ in range(self.state.width)] for _ in range(self.state.height)]

        for row in range(self.state.height):
            for col in range(self.state.width):
                self.process_map_object(row, col)
                
    def draw_game_objects(self):
        for wall in self.state.wall_objects:
            wall.draw(self.screen)
        for road in self.state.road_objects:
            road.draw(self.screen)
        for food in self.state.food_objects:
            food.draw(self.screen)
        for police in self.state.police_objects:
            police.draw(self.screen)

        self.state.thief_player.draw(self.screen)

        text_surface = self.game_font.render(f'Score: {self.state.score}', False, RED)
        self.screen.blit(text_surface, (0, 0))
        