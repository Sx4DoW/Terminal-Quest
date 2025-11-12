from classes.Enemy import Enemy
from classes.GameObject import GameObject
from utils.SparseSet import SparseSet
from pgzero.actor import Actor
from random import Random

class Room(GameObject):
    # Each room has a probability to spawn
    ROOM_TYPES: dict[str, float] = {"LOOT": 0.3, "COMBAT": 1.0, "START": 0.0, "BOSS": 0.0, "SECRET": 0.0}

    def __init__(self):
        super().__init__(Actor(f"room"))
        self.adjacent_rooms: dict[str, Room] = {
            "SOUTH": None,
            "EAST": None,
            "WEST": None,
            "NORTH": None
        }
        self.objects: SparseSet[GameObject] = SparseSet()

    def draw(self, screen):
        #print("Drawing room with objects:")
        for obj in self.objects:
            #print(f" - {obj}")
            obj.draw(screen)
    
    def update(self):
        for obj in self.objects:
            obj.update()

    def add_object(self, obj: GameObject):
        self.objects.add(obj)

    @staticmethod
    def generate_starting_room(seed: int) -> 'Room':
        r = Random(seed)
        room: Room = Room()
        return room
    @staticmethod
    def generate_combat_room(seed: int) -> 'Room':
        #TODO
        r = Random(seed)
        room: Room = Room()
        n_enemies: int = r.randint(1, 4)
        for _ in range(n_enemies):
            enemy: Enemy = Enemy.random_enemy(r.randint(0, 2**32 - 1))
            room.add_object(enemy)
        return room
    @staticmethod
    def generate_loot_room(seed: int) -> 'Room':
        #TODO
        r = Random(seed)
        room: Room = Room()
        return room
    @staticmethod
    def generate_boss_room(seed: int) -> 'Room':
        r = Random(seed)
        room: Room = Room()
        boss: Enemy = Enemy.boss(r.randint(0, 2**32 - 1))
        room.add_object(boss)

        return room
    @staticmethod
    def generate_random_room(seed: int) -> 'Room':
        r = Random(seed)
        chance: float = r.random()
        for room_type, room_chance in Room.ROOM_TYPES.items():
            if chance < room_chance:
                if room_type == "LOOT":
                    return Room.generate_loot_room(r.randint(0, 2**32 - 1))
                elif room_type == "COMBAT":
                    return Room.generate_combat_room(r.randint(0, 2**32 - 1))
                else: 
                    return secret_room
            


secret_room = Room()  # A predefined secret room instance
