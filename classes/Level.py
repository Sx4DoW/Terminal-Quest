from classes.GameObject import GameObject
from classes.Room import Room
from utils.SparseSet import SparseSet
from random import Random

class Level(GameObject):
    def __init__(self):
        self.objects: SparseSet[GameObject] = SparseSet()
        self.rooms: list[Room] = []
        self.active_room: Room = None
        pass
    
    def draw(self, screen):
        for room in self.rooms:
            room.draw(screen)

    def update(self):
        for obj in self.objects:
            obj.update()

    def add_room(self, room: Room):
        self.rooms.append(room)

    def remove_object(self, obj: GameObject):
        self.objects.remove(obj)

    def start(self):
        self.active_room = self.rooms[0]
        # spawnPlayer()
        pass

    @staticmethod
    def generate_level(seed: int) -> 'Level':
        r: Random = Random(seed)
        n_rooms: int = r.randint(5, 14) # Generates between 7 and 16 rooms per level (one is the starting room and another one is the boss room)
        
        l: Level = Level()
        # Generates starting room
        l.add_room(Room.generate_starting_room(r.randint(0, 2**32 - 1))) 

        for i in range(n_rooms):
            # Generates random rooms
            l.add_room(Room.generate_random_room(r.randint(0, 2**32 - 1)))
            
        # Generates boss room
        l.add_room(Room.generate_boss_room(r.randint(0, 2**32 - 1)))
        return l