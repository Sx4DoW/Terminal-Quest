class Enemy:
    def __init__(self, healt: int, damage: int, attack_speed: float):
        self.healt: int = healt
        self.damage: int = damage
        self.attack_speed: float = attack_speed
    
    @staticmethod
    def random_enemy(seed: int) -> 'Enemy':
        from random import Random
        r = Random(seed)
        healt = r.randint(20, 100)
        damage = r.randint(5, 20)
        attack_speed = r.uniform(0.5, 2.0)
        return Enemy(healt, damage, attack_speed)
    
    @staticmethod
    def boss(seed: int) -> 'Enemy':
        from random import Random
        r = Random(seed)
        healt = r.randint(200, 500)
        damage = r.randint(30, 70)
        attack_speed = r.uniform(0.3, 1.0)
        return Enemy(healt, damage, attack_speed)