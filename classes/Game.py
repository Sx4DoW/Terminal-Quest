from classes.GameObject import GameObject
from classes.Player import Player
from classes.Level import Level
from utils.SparseSet import SparseSet
from GameState import GameState

class Game:
    def __init__(self, n_levels: int = 3):
        self.objects: SparseSet[GameObject] = SparseSet()
        self.levels: list[Level] = []
        for _ in range(n_levels):
            level = Level.generate_level(GameState.seed)
            self.levels.append(level)
        self.active_level: Level = self.levels[0]
        self.spawnPlayer()

    def draw(self, screen):
        self.active_level.draw(screen)
        for obj in self.objects:
            obj.draw(screen)

    def update(self):
        self.active_level.update()
        for obj in self.objects:
            obj.update()

    def spawnPlayer(self):
        #TODO
        player = Player()
        self.objects.add(player)

game = Game()