from classes.GameObject import GameObject
from pgzero.actor import Actor

class Player(GameObject):
    def __init__(self):
        super().__init__(Actor("player"))
        self.health = 100
        self.inventory = Inventory()
    
    def draw(self, screen) -> None:
        self.target.draw(screen)
    
    def update(self) -> None:
        #TODO
        pass