from cube.cube_constants import FaceDirections, RotationDirections
from cube.color import Color

class Face:
    face_colors = {
        FaceDirections.UP: (255, 255, 255),
        FaceDirections.DOWN: (255, 255, 0),
        FaceDirections.LEFT: (0, 255, 0),
        FaceDirections.RIGHT: (0, 0, 255),
        FaceDirections.FRONT: (255, 0, 0),
        FaceDirections.BACK: (255, 100, 0),
    }

    def __init__(self, direction, size=3):
        self.direction = direction
        self.size = size
        self.tiles = [[Color(*self.face_colors[direction]) for x in range(size)] for y in range(size)] #[y][x]

    def rotate(self, direction):
        match direction:
            case RotationDirections.CLOCKWISE:
                self._rotate_clockwise()
            case RotationDirections.COUNTER_CLOCKWISE:
                self._rotate_counter_clockwise()

    def _rotate_clockwise(self):
        for x in range((self.size+1)//2):
            for y in range((self.size)//2):
                temp = self.tiles[x][y]
                self.tiles[x][y] = self.tiles[self.size-1-y][x]
                self.tiles[self.size-1-y][x] = self.tiles[self.size-1-x][self.size-1-y]
                self.tiles[self.size-1-x][self.size-1-y] = self.tiles[y][self.size-1-x]
                self.tiles[y][self.size-1-x] = temp

    def _rotate_counter_clockwise(self):
        for x in range((self.size+1)//2):
            for y in range((self.size)//2):
                temp = self.tiles[x][y]
                self.tiles[x][y] = self.tiles[y][self.size-1-x]
                self.tiles[y][self.size-1-x] = self.tiles[self.size-1-x][self.size-1-y]
                self.tiles[self.size-1-x][self.size-1-y] = self.tiles[self.size-1-y][x]
                self.tiles[self.size-1-y][x] = temp
