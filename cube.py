class Cube:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    FRONT = 4
    BACK = 5

    def __init__(self):
        self.faces = {
            self.UP: Face(self.UP),
            self.DOWN: Face(self.DOWN),
            self.LEFT: Face(self.LEFT),
            self.RIGHT: Face(self.RIGHT),
            self.FRONT: Face(self.FRONT),
            self.BACK: Face(self.BACK),
        }

class Face:
    def __init__(self, direction):
        pass

class Color:
    def __init__(self, color):
        pass