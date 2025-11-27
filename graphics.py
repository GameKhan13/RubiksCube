from pygame import Surface, Vector3, Vector2
from cube import Cube

CUBE_SURFACE: Surface = None
WIDTH, HEIGHT = None, None
SQUARE_ROOT_3 = 3 ** 0.5
DIRECTION_DICT = {
    Cube.UP : Vector3(0, 1, 0),
    Cube.DOWN : Vector3(0, -1, 0),
    Cube.LEFT : Vector3(-1, 0, 0),
    Cube.RIGHT : Vector3(1, 0, 0),
    Cube.FRONT : Vector3(0, 0, -1),
    Cube.BACK : Vector3(0, 0, 1),
}

# Create Surface For Cube
def createSurface(w, h) -> None:
    CUBE_SURFACE = Surface(w, h)
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
def rotate(v: Vector3, yaw=0, pitch=0, roll=0, direction_order="ypr") -> Vector3:
    for d in direction_order:
        if d == "y":
            # Yaw rotation around Y-axis
            v.rotate_y_ip(yaw)

        if d == "p":
            # Pitch rotation around X-axis
            v.rotate_x_ip(yaw)

        
        if d == "r":
            # Roll rotation around Z-axis
            v.rotate_z_ip(yaw)

    return v

# Orthographic Projection
@checkSurface
def project(v: Vector3) -> Vector2:
    return Vector2(v.x * WIDTH / 2, v.y * HEIGHT / 2)

    









