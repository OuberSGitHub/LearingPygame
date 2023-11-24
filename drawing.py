import pygame
from math import cos, sin, pi
pygame.init()

FPS = 60
WIDTH, HEIGHT = 800, 600
SPACE_BETWEEN = 20
BIG_RADIUS = 100
SMALL_RADIUS = 50
THETA = 0
NUMBER_OF_CIRCLES = 20


screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LINES")

clock = pygame.time.Clock()

run = True

while run:
    clock.tick(FPS)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #Drawing the grid
    for i in range(WIDTH//SPACE_BETWEEN):
        pygame.draw.line(screen, (255, 255, 255), (SPACE_BETWEEN*i, 0), (SPACE_BETWEEN*i, HEIGHT))

    for i in range(HEIGHT//SPACE_BETWEEN):
        pygame.draw.line(screen, (255, 255, 255), (0, SPACE_BETWEEN*i), (WIDTH, SPACE_BETWEEN*i))

    #Drawing the curved plan
    for i in range(WIDTH//SPACE_BETWEEN):
        pygame.draw.line(screen, (255, 255, 255), (0, SPACE_BETWEEN*i), (SPACE_BETWEEN*i, HEIGHT))

    #Drawing the circles
    while THETA < 2*pi:
        pygame.draw.circle(screen, (255, 255, 255), (WIDTH/2 + BIG_RADIUS*cos(THETA), HEIGHT/2 + BIG_RADIUS*sin(THETA)), SMALL_RADIUS, 1)
        THETA += (2*pi / NUMBER_OF_CIRCLES)
    

    dt = clock.tick(FPS)/1000

    pygame.display.update()

    