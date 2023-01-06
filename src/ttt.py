import pygame

background_color = (255, 255, 255)

black_color = (0, 0, 0)

width = 300

height = 300

offset = 50

surface = pygame.display.set_mode((width, height))

pygame.display.set_caption("Tic-Tac-Toe")

surface.fill(background_color)

running = True

while running:

    # vertical lines
    pygame.draw.line(surface, black_color, ((width / 2) - offset, 0), ((width / 2) - offset, height), 1)
    pygame.draw.line(surface, black_color, ((width / 2) + offset, 0), ((width / 2) + offset, height), 1)

    # horizontal lines
    pygame.draw.line(surface, black_color, (0, (height / 2) - offset), (width, (height / 2) - offset), 1)
    pygame.draw.line(surface, black_color, (0, (height / 2) + offset), (width, (height / 2) + offset), 1)

    pygame.display.flip()
    
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            
            running = False