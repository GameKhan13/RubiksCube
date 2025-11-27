class Cube:

    """
    Cube Wrapping:
    [U]
    [F][R][B][L]
    [D]
    """

    UP = 0
    FRONT = 1
    RIGHT = 2
    LEFT = 3
    BACK = 4
    DOWN = 5

    CLOCKWISE = 1
    COUNTER_CLOCKWISE = 0

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

        if direction == self.CLOCKWISE:
            self._rotate_strip(face, index)
        else:
            self._rotate_strip(5-face, self.size-1-index)

    def _rotate_strip(self, face, index):
        match face:
            case self.UP:
                self._swap_lines(
                    self.faces[self.FRONT], [[index, i] for i in range(self.size)], 
                    self.faces[self.RIGHT], [[index, i] for i in range(self.size)], 
                    self.faces[self.BACK], [[index, i] for i in range(self.size)], 
                    self.faces[self.LEFT], [[index, i] for i in range(self.size)], 
                    )

            case self.DOWN:
                self._swap_lines(
                    self.faces[self.LEFT], [[self.size-1-index, i] for i in range(self.size)], 
                    self.faces[self.BACK], [[self.size-1-index, i] for i in range(self.size)], 
                    self.faces[self.RIGHT], [[self.size-1-index, i] for i in range(self.size)], 
                    self.faces[self.FRONT], [[self.size-1-index, i] for i in range(self.size)], 
                    )
                    
            case self.LEFT:
                self._swap_lines(
                    self.faces[self.UP], [[i, index] for i in range(self.size)], 
                    self.faces[self.BACK], [[self.size-1-i, self.size-1-index] for i in range(self.size)], 
                    self.faces[self.DOWN], [[i, index] for i in range(self.size)], 
                    self.faces[self.FRONT], [[i, index] for i in range(self.size)],
                    )

            case self.RIGHT:
                self._swap_lines(
                    self.faces[self.FRONT], [[self.size-1-i, self.size-1-index] for i in range(self.size)],
                    self.faces[self.DOWN], [[self.size-1-i, self.size-1-index] for i in range(self.size)],
                    self.faces[self.BACK], [[i, index] for i in range(self.size)],
                    self.faces[self.UP], [[self.size-1-i, self.size-1-index] for i in range(self.size)],
                    )
                
            case self.FRONT:
                self._swap_lines(
                    self.faces[self.UP], [[self.size-1-index, self.size-1-i] for i in range(self.size)],
                    self.faces[self.LEFT], [[i, self.size-1-index] for i in range(self.size)],
                    self.faces[self.DOWN], [[index, i] for i in range(self.size)],      
                    self.faces[self.RIGHT], [[self.size-1-i, index] for i in range(self.size)],
                    )
                
            case self.BACK:
                self._swap_lines(
                    self.faces[self.RIGHT], [[self.size-1-i, self.size-1-index] for i in range(self.size)],
                    self.faces[self.DOWN], [[self.size-1-index, i] for i in range(self.size)],
                    self.faces[self.LEFT], [[i, index] for i in range(self.size)],
                    self.faces[self.UP], [[index, self.size-1-i] for i in range(self.size)],
                    )
    
 
    def _swap_lines(self, face1:Face, cordinates1, face2:Face, cordinates2, face3:Face, cordinates3, face4:Face, cordinates4):
        for i in range(self.size):
            temp = face1.tiles[cordinates1[i][0]][cordinates1[i][1]]
            face1.tiles[cordinates1[i][0]][cordinates1[i][1]] = face2.tiles[cordinates2[i][0]][cordinates2[i][1]]
            face2.tiles[cordinates2[i][0]][cordinates2[i][1]] = face3.tiles[cordinates3[i][0]][cordinates3[i][1]]
            face3.tiles[cordinates3[i][0]][cordinates3[i][1]] = face4.tiles[cordinates4[i][0]][cordinates4[i][1]]
            face4.tiles[cordinates4[i][0]][cordinates4[i][1]] = temp


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
        self.tiles = [[Color(*self.face_colors[direction]) for x in range(size)] for y in range(size)] #[y][x]

    def rotate(self, direction):
        match direction:
            case Cube.CLOCKWISE:
                self._rotate_clockwise()
            case Cube.COUNTER_CLOCKWISE:
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