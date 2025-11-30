import pygame
import graphics as g
import cube

screen = pygame.display.set_mode((800, 600), pygame.SCALED)


clock = pygame.time.Clock()
c = cube.Cube(size=3)
graphics = g.CubeRenderer(c, 400, 400)

a = 0
b = 22.5
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        if event.type == pygame.MOUSEBUTTONDOWN:
            if event.button in [1, 3]:
                if button == -1:
                    c.rotate(side, event.button == 1)
            
    m = pygame.mouse.get_rel()
    if pygame.mouse.get_pressed()[2]:
        a -= m[0]
        b += m[1]

    mouse_pos = pygame.mouse.get_pos()
    top_left = pygame.Vector2(600 - 400, 500 - 400)
    mouse_pos = pygame.Vector2(mouse_pos) -top_left
    mouse_pos.x = max(0, min(graphics.width - 1, mouse_pos.x))
    mouse_pos.y = max(0, min(graphics.height - 1, mouse_pos.y))
    color = graphics._surface.get_at([int(a) for a in mouse_pos])

    graphics.clear()
    graphics.drawCube()
    graphics.rotation = pygame.Vector3(b, a, 0)
    button, side = graphics.drawButtons(mouse_pos, color == (200, 200, 201, 255))
    screen.blit(graphics._surface, top_left)
    clock.tick(60)
    pygame.display.flip()















