class Cube:
    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    FRONT = 4
    BACK = 5

    def __init__(self, size=3):
        self.faces = [
            Face(self.UP, size),
            Face(self.DOWN, size),
            Face(self.LEFT, size),
            Face(self.RIGHT, size),
            Face(self.FRONT, size),
            Face(self.BACK, size),
        ]

class Color:
    def __init__(self, color):
        self.color = color

class Face:
    face_colors = {
        Cube.UP: (255, 255, 255),
        Cube.DOWN: (255, 255, 0),
        Cube.LEFT: (0, 255, 0),
        Cube.RIGHT: (0, 0, 255),
        Cube.FRONT: (255, 0, 0),
        Cube.BACK: (255, 100, 0),
    }

    def __init__(self, direction, size=3):
        self.faces = [[Color(self.face_colors[direction]) for x in range(size)] for y in range(size)]