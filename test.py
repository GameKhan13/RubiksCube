import pygame
import graphics
import cube

screen = pygame.display.set_mode((800, 600))


graphics.createSurface(400, 400)
clock = pygame.time.Clock()


c = cube.Cube(size=70)

a = 0
b = 22.5
while True:
    for event in pygame.event.get():
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_u:
                c.rotate(c.UP, direction=pygame.key.get_pressed()[pygame.K_LSHIFT], index=0)
            if event.key == pygame.K_d:
                c.rotate(c.DOWN, direction=pygame.key.get_pressed()[pygame.K_LSHIFT], index=0)
            if event.key == pygame.K_e:
                c.rotate(c.DOWN, direction=pygame.key.get_pressed()[pygame.K_LSHIFT], index=1)
    m = pygame.mouse.get_rel()
    a += m[0]
    b += m[1]
    graphics.clear()
    graphics.drawCube(c, pygame.Vector3(b, a, 0))
    screen.blit(graphics.CUBE_SURFACE, (600 - 400, 500 - 400))
    clock.tick(60)
    pygame.display.flip()















