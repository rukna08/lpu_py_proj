import pygame

from pygame import gfxdraw

import numpy as np

game_matrix = np.array(
    [
        [0, 0, 0],
        [0, 0, 0],
        [0, 0, 0]
    ]
)

shape_index = 0

game_is_over = False

def push_data_to_game_matrix(i, j):
    if game_matrix[i][j] == 0:
        if (shape_index) % 2 == 0:
            game_matrix[i][j] = 1
        else:
            game_matrix[i][j] = 2

    print(game_matrix)

def draw_circle(surface, radius, coord):
    gfxdraw.aacircle(surface, coord[0], coord[1], radius, black_color)
    gfxdraw.aacircle(surface, coord[0], coord[1], radius - 1, black_color)

def draw_cross(coord):
    cross_sprite = pygame.image.load("cross_sprite.png").convert_alpha()

    surface.blit(cross_sprite, (coord[0] - 15, coord[1] - 15))

def draw_shape(surface, radius, coord):
    global shape_index
    
    if shape_index % 2 == 0:
        draw_circle(surface, radius, coord)

    else:
        draw_cross(coord)
    
    shape_index += 1

def check_game_win_condition():
    global game_is_over

    circle_wins = False
    cross_wins = False
    
    if((game_matrix[0][0] == 1 and game_matrix[0][1] == 1 and game_matrix[0][2] == 1)
    or (game_matrix[1][0] == 1 and game_matrix[1][1] == 1 and game_matrix[1][2] == 1)
    or (game_matrix[2][0] == 1 and game_matrix[2][1] == 1 and game_matrix[2][2] == 1)
    or (game_matrix[0][0] == 1 and game_matrix[1][0] == 1 and game_matrix[2][0] == 1)
    or (game_matrix[0][1] == 1 and game_matrix[1][1] == 1 and game_matrix[2][1] == 1)
    or (game_matrix[0][2] == 1 and game_matrix[1][2] == 1 and game_matrix[2][2] == 1)
    or (game_matrix[0][2] == 1 and game_matrix[1][1] == 1 and game_matrix[2][0] == 1)
    or (game_matrix[0][0] == 1 and game_matrix[1][1] == 1 and game_matrix[2][2] == 1)):
        circle_wins = True
        game_is_over = True

    if((game_matrix[0][0] == 2 and game_matrix[0][1] == 2 and game_matrix[0][2]) == 2
    or (game_matrix[1][0] == 2 and game_matrix[1][1] == 2 and game_matrix[1][2]) == 2
    or (game_matrix[2][0] == 2 and game_matrix[2][1] == 2 and game_matrix[2][2]) == 2
    or (game_matrix[0][0] == 2 and game_matrix[1][0] == 2 and game_matrix[2][0]) == 2
    or (game_matrix[0][1] == 2 and game_matrix[1][1] == 2 and game_matrix[2][1]) == 2
    or (game_matrix[0][2] == 2 and game_matrix[1][2] == 2 and game_matrix[2][2]) == 2
    or (game_matrix[0][2] == 2 and game_matrix[1][1] == 2 and game_matrix[2][0] == 2)
    or (game_matrix[0][0] == 2 and game_matrix[1][1] == 2 and game_matrix[2][2] == 2)):
        cross_wins = True
        game_is_over = True
    
    if circle_wins == True:
        print("circle wins")
    elif cross_wins == True:
        print("cross wins")


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

    if not game_is_over:
        # vertical lines
        pygame.draw.line(surface, black_color, ((width / 2) - offset, 0), ((width / 2) - offset, height), 1)
        pygame.draw.line(surface, black_color, ((width / 2) + offset, 0), ((width / 2) + offset, height), 1)

        # horizontal lines
        pygame.draw.line(surface, black_color, (0, (height / 2) - offset), (width, (height / 2) - offset), 1)
        pygame.draw.line(surface, black_color, (0, (height / 2) + offset), (width, (height / 2) + offset), 1)

    pygame.display.flip()
    
    for event in pygame.event.get():

        if not game_is_over:
            if event.type == pygame.MOUSEBUTTONDOWN:

                # box 0
                if pygame.mouse.get_pos()[0] >= 0 and pygame.mouse.get_pos()[0] <= 100:
                    if pygame.mouse.get_pos()[1] >= 0 and pygame.mouse.get_pos()[1] <= 100:
                        print("Inside box 0")

                        # 1 = O
                        # 2 = X

                        push_data_to_game_matrix(0, 0)
                    
                        draw_shape(surface, 22, (50, 50))

                # box 1
                if pygame.mouse.get_pos()[0] >= 100 and pygame.mouse.get_pos()[0] <= 200:
                    if pygame.mouse.get_pos()[1] >= 0 and pygame.mouse.get_pos()[1] <= 100:
                        print("Inside box 1")

                        push_data_to_game_matrix(0, 1)

                        draw_shape(surface, 22, (150, 50))

                # box 2
                if pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 300:
                    if pygame.mouse.get_pos()[1] >= 0 and pygame.mouse.get_pos()[1] <= 100:
                        print("Inside box 2")

                        push_data_to_game_matrix(0, 2)

                        draw_shape(surface, 22, (250, 50))

                # box 3
                if pygame.mouse.get_pos()[0] >= 0 and pygame.mouse.get_pos()[0] <= 100:
                    if pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[1] <= 200:
                        print("Inside box 3")

                        push_data_to_game_matrix(1, 0)

                        draw_shape(surface, 22, (50, 150))
                # box 4
                if pygame.mouse.get_pos()[0] >= 100 and pygame.mouse.get_pos()[0] <= 200:
                    if pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[1] <= 200:
                        print("Inside box 4")

                        push_data_to_game_matrix(1, 1)

                        draw_shape(surface, 22, (150, 150))
                # box 5
                if pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 300:
                    if pygame.mouse.get_pos()[1] >= 100 and pygame.mouse.get_pos()[1] <= 200:
                        print("Inside box 5")

                        push_data_to_game_matrix(1, 2)

                        draw_shape(surface, 22, (250, 150))

                # box 6
                if pygame.mouse.get_pos()[0] >= 0 and pygame.mouse.get_pos()[0] <= 100:
                    if pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 300:
                        print("Inside box 6")

                        push_data_to_game_matrix(2, 0)

                        draw_shape(surface, 22, (50, 250))
                # box 7
                if pygame.mouse.get_pos()[0] >= 100 and pygame.mouse.get_pos()[0] <= 200:
                    if pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 300:
                        print("Inside box 7")

                        push_data_to_game_matrix(2, 1)

                        draw_shape(surface, 22, (150, 250))
                # box 8
                if pygame.mouse.get_pos()[0] >= 200 and pygame.mouse.get_pos()[0] <= 300:
                    if pygame.mouse.get_pos()[1] >= 200 and pygame.mouse.get_pos()[1] <= 300:
                        print("Inside box 8")

                        push_data_to_game_matrix(2, 2)

                        draw_shape(surface, 22, (250, 250))

                check_game_win_condition()

        if game_is_over:
            surface.fill(background_color)

        if event.type == pygame.QUIT:
            running = False
