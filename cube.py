class Cube:

    """
    Cube Wrapping:
    [U]
    [F][R][B][L]
    [D]
    """

    UP = 0
    DOWN = 1
    LEFT = 2
    RIGHT = 3
    FRONT = 4
    BACK = 5

    CLOCKWISE = 0
    COUNTER_CLOCKWISE = 1

    def __init__(self, size=3):
        self.faces = {
            self.UP: Face(self.UP, size),
            self.DOWN: Face(self.DOWN, size),
            self.LEFT: Face(self.LEFT, size),
            self.RIGHT: Face(self.RIGHT, size),
            self.FRONT: Face(self.FRONT, size),
            self.BACK: Face(self.BACK, size),
        }

    def rotate(self, face, direction=CLOCKWISE, index=0):
        pass

    def _rotate_strip(self, face, direction, index):
        pass


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
        self.direction = direction
        self.size = size
        self.faces = [[Color(self.face_colors[direction]) for x in range(size)] for y in range(size)]

    def rotate(self, direction):
        match direction:
            case Cube.CLOCKWISE:
                self._rotate_clockwise()
            case Cube.COUNTER_CLOCKWISE:
                self._rotate_counter_clockwise()

    def _rotate_clockwise(self):
        for x in range((self.size+1)/2):
            for y in range((self.size)/2):
                temp = self.faces[x][y]
                self.faces[x][y] = self.faces[self.size-1-y][x]
                self.faces[self.size-1-y][x] = self.faces[self.size-1-x][self.size-1-y]
                self.faces[self.size-1-x][self.size-1-y] = self.faces[y][self.size-1-x]
                self.faces[y][self.size-1-x] = temp

    def _rotate_counter_clockwise(self):
        for x in range((self.size+1)/2):
            for y in range((self.size)/2):
                temp = self.faces[x][y]
                self.faces[x][y] = self.faces[y][self.size-1-x]
                self.faces[y][self.size-1-x] = self.faces[self.size-1-x][self.size-1-y]
                self.faces[self.size-1-x][self.size-1-y] = self.faces[self.size-1-y][x]
                self.faces[self.size-1-y][x] = temp