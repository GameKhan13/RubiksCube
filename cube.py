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
        self.size = size
        self.faces = {
            self.UP: Face(self.UP, size),
            self.DOWN: Face(self.DOWN, size),
            self.LEFT: Face(self.LEFT, size),
            self.RIGHT: Face(self.RIGHT, size),
            self.FRONT: Face(self.FRONT, size),
            self.BACK: Face(self.BACK, size),
        }

    def rotate(self, face, direction=CLOCKWISE, index=0):
        if index == 0:
            self.faces[face].rotate(direction)
        self._rotate_strip(face, direction, index)

    def _rotate_strip(self, face, direction, index):
        match face:
            case self.UP:
                self._swap_lines(
                    self.faces[self.FRONT][index], 
                    self.faces[self.RIGHT][index], 
                    self.faces[self.BACK][index], 
                    self.faces[self.LEFT][index], 
                    direction)

            case self.DOWN:
                self._swap_lines(
                    self.faces[self.FRONT][self.size-1-index], 
                    self.faces[self.RIGHT][self.size-1-index], 
                    self.faces[self.BACK][self.size-1-index], 
                    self.faces[self.LEFT][self.size-1-index], 
                    1-direction)#swap d
                
            case self.LEFT:
                pass
            case self.RIGHT:
                pass
            case self.FRONT:
                pass
            case self.BACK:
                pass
    
    """
    Clockwise is a rotate left style operation
    """
    def _swap_lines(self, line1, line2, line3, line4, direction):
        if direction == 0:   
            self._swap_lines_clockwise(line1, line2, line3, line4)
        else:
            self._swap_lines_counter_clockwise(line1, line2, line3, line4)

    def _swap_lines_clockwise(self, line1, line2, line3, line4):
        for i in range(self.size):
            temp = line1[i]
            line1[i] = line2[i]
            line2[i] = line3[i]
            line3[i] = line4[i]
            line4[i] = temp

    def _swap_lines_counter_clockwise(self, line1, line2, line3, line4):
        for i in range(self.size):
            temp = line1[i]
            line1[i] = line4[i]
            line4[i] = line3[i]
            line3[i] = line2[i]
            line2[i] = temp
            
            
            


class Color:
    def __init__(self, red, green, blue):
        self.color = (red, green, blue)
        
    @property
    def red(self):
        return self.color[0]
    
    @property
    def green(self):
        return self.color[1]
    
    @property
    def blue(self):
        return self.color[2]

    def __mul__(self, other:float):
        return Color(other*self.red, other*self.green, other*self.blue)

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
        self.tiles = [[Color(self.face_colors[direction]) for x in range(size)] for y in range(size)] #[y][x]

    def rotate(self, direction):
        match direction:
            case Cube.CLOCKWISE:
                self._rotate_clockwise()
            case Cube.COUNTER_CLOCKWISE:
                self._rotate_counter_clockwise()

    def _rotate_clockwise(self):
        for x in range((self.size+1)/2):
            for y in range((self.size)/2):
                temp = self.tiles[x][y]
                self.tiles[x][y] = self.tiles[self.size-1-y][x]
                self.tiles[self.size-1-y][x] = self.tiles[self.size-1-x][self.size-1-y]
                self.tiles[self.size-1-x][self.size-1-y] = self.tiles[y][self.size-1-x]
                self.tiles[y][self.size-1-x] = temp

    def _rotate_counter_clockwise(self):
        for x in range((self.size+1)/2):
            for y in range((self.size)/2):
                temp = self.tiles[x][y]
                self.tiles[x][y] = self.tiles[y][self.size-1-x]
                self.tiles[y][self.size-1-x] = self.tiles[self.size-1-x][self.size-1-y]
                self.tiles[self.size-1-x][self.size-1-y] = self.tiles[self.size-1-y][x]
                self.tiles[self.size-1-y][x] = temp

if __name__ == "__main__":
    print((Color(100, 100, 100)*2).color)