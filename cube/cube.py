from cube.cube_constants import FaceDirections, RotationDirections
from cube.face import Face

class Cube:

    """
    Cube Wrapping:
    [U]
    [F][R][B][L]
    [D]
    """

    def __init__(self, size=3):
        self.size = size
        self.faces = {
            FaceDirections.UP: Face(FaceDirections.UP, size),
            FaceDirections.DOWN: Face(FaceDirections.DOWN, size),
            FaceDirections.LEFT: Face(FaceDirections.LEFT, size),
            FaceDirections.RIGHT: Face(FaceDirections.RIGHT, size),
            FaceDirections.FRONT: Face(FaceDirections.FRONT, size),
            FaceDirections.BACK: Face(FaceDirections.BACK, size),
        }

    def rotate(self, face, direction=RotationDirections.CLOCKWISE, index=0):
        if index == 0:
            self.faces[face].rotate(direction)

        if direction == RotationDirections.CLOCKWISE:
            self._rotate_strip(face, index)
        else:
            self._rotate_strip(5-face, self.size-1-index)

    def _rotate_strip(self, face, index):
        match face:
            case FaceDirections.UP:
                self._swap_lines(
                    self.faces[FaceDirections.FRONT], [[index, i] for i in range(self.size)], 
                    self.faces[FaceDirections.RIGHT], [[index, i] for i in range(self.size)], 
                    self.faces[FaceDirections.BACK], [[index, i] for i in range(self.size)], 
                    self.faces[FaceDirections.LEFT], [[index, i] for i in range(self.size)], 
                    )

            case FaceDirections.DOWN:
                self._swap_lines(
                    self.faces[FaceDirections.LEFT], [[self.size-1-index, i] for i in range(self.size)], 
                    self.faces[FaceDirections.BACK], [[self.size-1-index, i] for i in range(self.size)], 
                    self.faces[FaceDirections.RIGHT], [[self.size-1-index, i] for i in range(self.size)], 
                    self.faces[FaceDirections.FRONT], [[self.size-1-index, i] for i in range(self.size)], 
                    )
                    
            case FaceDirections.LEFT:
                self._swap_lines(
                    self.faces[FaceDirections.UP], [[i, index] for i in range(self.size)], 
                    self.faces[FaceDirections.BACK], [[self.size-1-i, self.size-1-index] for i in range(self.size)], 
                    self.faces[FaceDirections.DOWN], [[i, index] for i in range(self.size)], 
                    self.faces[FaceDirections.FRONT], [[i, index] for i in range(self.size)],
                    )

            case FaceDirections.RIGHT:
                self._swap_lines(
                    self.faces[FaceDirections.FRONT], [[self.size-1-i, self.size-1-index] for i in range(self.size)],
                    self.faces[FaceDirections.DOWN], [[self.size-1-i, self.size-1-index] for i in range(self.size)],
                    self.faces[FaceDirections.BACK], [[i, index] for i in range(self.size)],
                    self.faces[FaceDirections.UP], [[self.size-1-i, self.size-1-index] for i in range(self.size)],
                    )
                
            case FaceDirections.FRONT:
                self._swap_lines(
                    self.faces[FaceDirections.UP], [[self.size-1-index, self.size-1-i] for i in range(self.size)],
                    self.faces[FaceDirections.LEFT], [[i, self.size-1-index] for i in range(self.size)],
                    self.faces[FaceDirections.DOWN], [[index, i] for i in range(self.size)],      
                    self.faces[FaceDirections.RIGHT], [[self.size-1-i, index] for i in range(self.size)],
                    )
                
            case FaceDirections.BACK:
                self._swap_lines(
                    self.faces[FaceDirections.RIGHT], [[self.size-1-i, self.size-1-index] for i in range(self.size)],
                    self.faces[FaceDirections.DOWN], [[self.size-1-index, i] for i in range(self.size)],
                    self.faces[FaceDirections.LEFT], [[i, index] for i in range(self.size)],
                    self.faces[FaceDirections.UP], [[index, self.size-1-i] for i in range(self.size)],
                    )
    
 
    def _swap_lines(self, face1:Face, cordinates1, face2:Face, cordinates2, face3:Face, cordinates3, face4:Face, cordinates4):
        for i in range(self.size):
            temp = face1.tiles[cordinates1[i][0]][cordinates1[i][1]]
            face1.tiles[cordinates1[i][0]][cordinates1[i][1]] = face2.tiles[cordinates2[i][0]][cordinates2[i][1]]
            face2.tiles[cordinates2[i][0]][cordinates2[i][1]] = face3.tiles[cordinates3[i][0]][cordinates3[i][1]]
            face3.tiles[cordinates3[i][0]][cordinates3[i][1]] = face4.tiles[cordinates4[i][0]][cordinates4[i][1]]
            face4.tiles[cordinates4[i][0]][cordinates4[i][1]] = temp


