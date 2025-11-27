from pygame import Surface, Vector3, Vector2, draw
from cube import Cube, Face

CUBE_SURFACE: Surface = None
WIDTH, HEIGHT = None, None
DIRECTION_DICT = {
    Cube.UP : Vector3(-90, 0, 0),
    Cube.DOWN : Vector3(90, 0, 0),
    Cube.LEFT : Vector3(0, -270, 0),
    Cube.RIGHT : Vector3(0, -90, 0),
    Cube.BACK : Vector3(0, -180, 0),
    Cube.FRONT : Vector3(0, 0, 0),
}
OFFSETS = [Vector3(-0.5, 0.5, -0.5), Vector3(0.5, 0.5, -0.5), Vector3(0.5, -0.5, -0.5), Vector3(-0.5, -0.5, -0.5)]


# Create Surface For Cube
def createSurface(w, h) -> None:
    global CUBE_SURFACE, WIDTH, HEIGHT
    CUBE_SURFACE = Surface((w, h))
    WIDTH, HEIGHT = w, h

def checkSurface(func):
    def wrapper(*args, **kwargs):
        # Check if Surface Initialized
        if CUBE_SURFACE is None:
            raise Exception("Surface not initialized. Call <createSurface> first!")
        
        result = func(*args, **kwargs)

        return result
    return wrapper
        

# 3D Rotation Around Origin
def rotate(v: Vector3, pitch=0, yaw=0, roll=0, direction_order="ypr") -> Vector3:
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

# Orthographic Projection
@checkSurface
def project(v: Vector3) -> Vector2:
    return Vector2(v.x * WIDTH / 2, v.y * HEIGHT / 2)

@checkSurface
def clear() -> None:
    CUBE_SURFACE.fill((0, 0, 0))


@checkSurface
def drawFace(face: Face, rotation: Vector3) -> None:

    normal = Vector3(0, 0, 1)
    normal = rotate(normal, *DIRECTION_DICT[face.direction]).normalize()
    normal = rotate(normal, *rotation).normalize()
    brightness = normal.dot(Vector3(0, 0, 1))
    sqrt = (3 * (face.size / 2) ** 2) ** 0.5


    if brightness <= 0.01:
        return

    for y in range(face.size):
        for x in range(face.size):
            drawTile(face, x, y, brightness, rotation, sqrt)

@checkSurface
def drawTile(face, x, y, brightness, rotation, sqrt):
    vertices = []

    for offset in OFFSETS:
        position = (Vector3(x - face.size / 2 + 0.5, y - face.size / 2 + 0.5, -face.size / 2 + 0.5) + offset) / sqrt
        position = rotate(position, *DIRECTION_DICT[face.direction])
        position = rotate(position, *rotation)
        position = project(position)
        position = position + Vector2(WIDTH, HEIGHT) / 2
        vertices.append(position)

    draw.polygon(CUBE_SURFACE, (face.tiles[y][x] * brightness).color, vertices)
    draw.polygon(CUBE_SURFACE, [60]*3, vertices, width=2)

@checkSurface
def drawCube(cube: Cube, rotation: Vector3):
    for face in cube.faces.values():
        drawFace(face, rotation)
        

            
        









