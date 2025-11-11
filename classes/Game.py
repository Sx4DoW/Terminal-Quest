from classes.GameObject import GameObject
from classes.Player import Player
from classes.Level import Level, generate_level
from utils.SparseSet import SparseSet
from GameState import GameState

class Game:
    def __init__(self, n_levels: int = 3):
        self.objects: SparseSet[GameObject] = SparseSet()
        self.levels: SparseSet[Level] = SparseSet()
        for _ in range(3):
            level = generate_level(GameState.seed)
            self.levels.add(level)
            self.objects.add(level)
        self.generate_level()
        self.spawnPlayer()


    def update(self):
        for obj in self.objects:
            obj.update()

    def spawnPlayer(self):
        player = Player()
