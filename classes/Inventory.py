from classes.GameObject import GameObject
from utils.SparseSet import SparseSet

class Inventory:
    def __init__(self):
        self.items: SparseSet[GameObject] = SparseSet()
    
    def add_item(self, item: GameObject):
        self.items.add(item)

    def remove_item(self, item: GameObject):
        self.items.remove(item)
    
    def has_item(self, item: GameObject) -> bool:
        return item in self.items
    
    def use_item(self, item: GameObject):
        if self.has_item(item):
            if item.usable:
                item.use()
                self.remove_item(item)
            else:
                #TODO find a way to notify that item is not usable
                print("Item is not usable")