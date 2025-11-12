from classes.GameObject import GameObject
from pgzero.actor import Actor

class Background(GameObject):
    """Background class for the game."""
    def __init__(self, image: str, hoverable = False, draggable = False, collidable = False):
        super().__init__(Actor(image), hoverable, draggable, collidable)

    def draw(self, screen):
        screen.clear()
        return self.target.draw()
    
