import pygame
pygame.init()

FPS = 60
WIDTH, HEIGHT = 800, 600


clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("LOL")

radius = 50
x_position, y_position = WIDTH/2, HEIGHT/2
vel = 5
red, green, blue = (255, 255, 255)

run = True
while run:
    clock.tick(FPS)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_z:
                print("player moved up")
                y_position -= vel
            elif event.key == pygame.K_s:
                print("player moved down")
                y_position += vel
            elif event.key == pygame.K_q:
                print("player moved left")
                x_position -= vel
            elif event.key == pygame.K_d:
                print("player moved right")
                x_position += vel
        mouse = pygame.mouse.get_pressed()
        if mouse[0]:
            print("mouse pressed left click")
            red = (red + 100) % 255
            green = (green + 57) % 255
            blue = (blue + 23) % 255

        if mouse[2]:
            print("mouse pressed right click")
            mouse_position = pygame.mouse.get_pos()
            x_position = mouse_position[0]
            y_position = mouse_position[1]

        #screen.fill((0, 0, 0))
        pygame.draw.circle(screen, (red, green, blue), (x_position, y_position), radius)


    pygame.display.update()

pygame.quit()
exit()