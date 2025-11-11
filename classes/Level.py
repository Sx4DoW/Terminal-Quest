from classes.GameObject import GameObject
from classes.Room import Room, generate_random_room
from utils.SparseSet import SparseSet
from random import Random

class Level(GameObject):
    def __init__(self):
        self.objects: SparseSet[GameObject] = SparseSet()
        self.rooms: SparseSet[Room] = SparseSet()
        pass
    
    def add_room(self, room: Room):
        self.rooms.add(room)
        self.objects.add(room)

    def update(self):
        for obj in self.objects:
            obj.update()

    def remove_object(self, obj: GameObject):
        self.objects.remove(obj)
    def start(self):
        # spawnPlayer()
        pass


def generate_level(seed: int) -> Level:
    r: Random = Random(seed)
    n_rooms: int = r.randint(5, 14) #generates between 7 and 16 rooms per level (one is the starting room and another one is the boss room)
    for i in range(n_rooms):
        generate_random_room(r.randint(0, 2**32 - 1))
    l: Level = Level()
    return l