from sprite import Sprite

class Sprite1(Sprite):
    def __init__(self, gameEngine, costume):
        super().__init__(gameEngine, costume)

    def paint(self):
        self.stamp(0, 100)
