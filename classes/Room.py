from classes.Enemy import Enemy
from classes.GameObject import GameObject
from random import Random

class Room(GameObject):
    def __init__(self):
        self.adjacent_rooms: dict[str, Room] = {
            "SOUTH": None,
            "EAST": None,
            "WEST": None,
            "NORTH": None
        }

secret_room = Room()

# Each room has a probability to spawn
ROOM_TYPES: dict[str, float] = {"LOOT": 0.3, "COMBAT": 1.0, "START": 0.0, "BOSS": 0.0}

def generate_starting_room(seed: int) -> Room:

def generate_combat_room(seed: int) -> Room:

def generate_loot_room(seed: int) -> Room:

def generate_boss_room(seed: int) -> Room:
    r = Random(seed)
    room: Room = Room()
    boss: Enemy = generate_boss(r.randint(0, 2**32 - 1))
    room.add_enemies(boss)

    return room


def generate_random_room(seed: int) -> Room:
    r = Random(seed)
    chance: float = r.random()
    for room_type, room_chance in ROOM_TYPES.items():
        if chance < room_chance:
            if room_type == "LOOT":
                return generate_loot_room(r.randint(0, 2**32 - 1))
            elif room_type == "COMBAT":
                return generate_combat_room(r.randint(0, 2**32 - 1))
            else: 
                return secret_room