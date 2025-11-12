from classes.GameObject import GameObject
from classes.Player import Player
from classes.Level import Level
from utils.SparseSet import SparseSet

class Game(GameObject):
    def __init__(self, n_levels: int = 3):
        from GameState import GameState        
        self.objects: SparseSet = SparseSet()
        self.levels: list[Level] = []
        for _ in range(n_levels):
            level = Level.generate_level(GameState.seed)
            self.levels.append(level)
        self.active_level: Level = self.levels[0]
        self.spawnPlayer()

    def draw(self, screen):
        screen.clear()
        #print("Drawing game")
        self.active_level.draw(screen)
        for obj in self.objects:
            #print(f"Drawing object {obj}")
            obj.draw(screen)

    def update(self, pos, button=None):
        self.active_level.update(pos, button)
        for obj in self.objects:
            obj.update(pos, button)

    def spawnPlayer(self):
        #TODO
        self.player = Player()
        self.objects.add(self.player)