from uuid import uuid4
from swap_meet.item import Item


class Clothing(Item):
    def __init__(self, id=None, fabric="Unknown"):
        super().__init__(id)
        self.fabric = fabric

    def get_category(self):
        return "Clothing"
    
    def __str__(self):
        return (f"{super().__str__()} "
                f"It is made from {self.fabric} fabric.")