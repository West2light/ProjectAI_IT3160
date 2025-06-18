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
 