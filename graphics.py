from pygame import Surface, Vector3, Vector2, draw
from cube import Cube, Face
from math import inf
DIRECTION_DICT = {
   Cube.UP : Vector3(-90, 0, 0),
   Cube.DOWN : Vector3(90, 0, 0),
   Cube.LEFT : Vector3(0, -270, 0),
   Cube.RIGHT : Vector3(0, -90, 0),
   Cube.BACK : Vector3(0, -180, 0),
   Cube.FRONT : Vector3(0, 0, 0),
}
SQUARE_OFFSETS = [Vector3(-0.5, 0.5, -0.5), Vector3(0.5, 0.5, -0.5), Vector3(0.5, -0.5, -0.5), Vector3(-0.5, -0.5, -0.5)]
TRIANGLE_OFFSETS = [Vector3(-0.3, 0.7, -0.5), Vector3(0.3, 0.7, -0.5), Vector3(0.0, 1.0, -0.5)]

# 3D Rotation of vectors around origin
def _rotate(v: Vector3, pitch=0, yaw=0, roll=0, direction_order="ypr") -> Vector3:
    for d in direction_order:
        if d == "y":
            # Yaw rotation around Y-axis
            v.rotate_y_ip(yaw)

        if d == "p":
            # Pitch rotation around X-axis
            v.rotate_x_ip(pitch)

        
        if d == "r":
            # Roll rotation around Z-axis
            v.rotate_z_ip(roll)

    return v

class CubeRenderer:
    def __init__(self, cube: Cube, width, height):
        self._cube: Cube = cube
        self.rotation = Vector3(0, 0, 0)
        self._surface: Surface = Surface((width, height))
        self.width, self.height = width, height
        self._sqrt = (3 * (cube.size / 2) ** 2) ** 0.5
        self._half_width = -cube.size / 2 + 0.5

    def clear(self) -> None:
        self._surface.fill((0, 0, 0))

    # Orthographic Projection
    def project(self, v: Vector3) -> Vector2:
        return Vector2(v.x * self.width / 2 * 0.95, v.y * self.height / 2 * 0.95)

    # Draws a single face from aself._cube
    def _drawFace(self, face: Face) -> None:
        normal = Vector3(0, 0, 1)
        normal = _rotate(normal, *DIRECTION_DICT[face.direction]).normalize()
        normal = _rotate(normal, *self.rotation).normalize()
        brightness = normal.dot(Vector3(0, 0, 1))

        if brightness <= 0.01:
            return

        for y in range(face.size):
            for x in range(face.size):
                self._drawTile(face, x, y, brightness)

    # Draws a single tile from a face
    def _drawTile(self, face, x, y, brightness):
        vertices = []

        for offset in SQUARE_OFFSETS:
            position = (Vector3(x + self._half_width, y + self._half_width, self._half_width) + offset) / self._sqrt
            position = _rotate(position, *DIRECTION_DICT[face.direction])
            position = _rotate(position, *self.rotation)
            position = self.project(position)
            position = position + Vector2(self.width, self.height) / 2
            vertices.append(position)

        draw.polygon(self._surface, (face.tiles[y][x] * brightness).color, vertices)
        draw.polygon(self._surface, [60]*3, vertices, width=2)

    # Draws the wholeself._cube
    def drawCube(self):
        for face in self._cube.faces.values():
            self._drawFace(face)
        

    def drawButtons(self, mouse: Vector2, hovered: bool):
        front = self.getForwardFace()
        closest = None
        dist = inf
        id = None

        for i in range(4):
            for x in range(self._cube.size):
                vertices = []
                origin = Vector3(x + self._half_width, -self._half_width, self._half_width)

                for offset in TRIANGLE_OFFSETS:
                    position = (origin + offset) / self._sqrt
                    position = _rotate(position, *Vector3(0, 0, 90 * i))
                    position = _rotate(position, *DIRECTION_DICT[front.direction])
                    position = _rotate(position, *self.rotation)
                    position = self.project(position)
                    position = position + Vector2(self.width, self.height) / 2
                    
                    vertices.append(position)

                if vertices[0].distance_squared_to(mouse) < dist:
                    dist = vertices[0].distance_squared_to(mouse)
                    closest = tuple(vertices)
                    id = i + 4 * x
                draw.polygon(self._surface, [200, 200, 201], vertices)
                draw.polygon(self._surface, [130]*3, vertices, width=2)

        vertices = []
        for i in range(16):
            half_width = -self._cube.size / 2 + 0.5
            
            position = (Vector3(0.3, 0, half_width - 0.5)) / self._sqrt
            position = _rotate(position, *Vector3(0, 0, 360/16 * i))
            position = _rotate(position, *DIRECTION_DICT[front.direction])
            position = _rotate(position, *self.rotation)
            position = self.project(position)
            position = position + Vector2(self.width, self.height) / 2
            
            vertices.append(position)
            
        if vertices[0].distance_squared_to(mouse) < dist:
            dist = vertices[0].distance_squared_to(mouse)
            closest = tuple(vertices)
            id = -1
            
        draw.polygon(self._surface, [200, 200, 201], vertices)
        draw.polygon(self._surface, [130]*3, vertices, width=2)

        if hovered:
            draw.polygon(self._surface, [200, 200, 201], closest)
            draw.polygon(self._surface, [250]*3, closest, width=4)
        
        return id, front.direction


    def getForwardFace(self):
        front_most_alignment = -1
        front_most_face = None
        for face in self._cube.faces.values():
            normal = Vector3(0, 0, 1)
            normal = _rotate(normal, *DIRECTION_DICT[face.direction]).normalize()
            normal = _rotate(normal, *self.rotation).normalize()
            alignment = normal.dot(Vector3(0, 0, 1))

            if alignment > front_most_alignment:
                front_most_alignment = alignment
                front_most_face = face

        return front_most_face
