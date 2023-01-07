import pygame

pygame.init()

pygame.font.init()

quiz_font = pygame.freetype.Font('res/Roboto-Regular.ttf', 27)

def display_question(surface, question_index, coordinate):
    quiz_font.render_to(surface, coordinate, questions_array[question_index], (0, 0, 0))

def display_options(surface):
    quiz_font.render_to(surface, (20, 100), "1.  ", (0, 0, 0))
    quiz_font.render_to(surface, (20, 150), "2.  ", (0, 0, 0))
    quiz_font.render_to(surface, (20, 200), "3.  ", (0, 0, 0))
    quiz_font.render_to(surface, (20, 250), "4.  ", (0, 0, 0))

questions_array = []

with open("res/questions.txt") as questions_txtfile:
    questions_array = questions_txtfile.readlines()

white_colour = (255, 255, 255)

width = 800

height = 500

surface = pygame.display.set_mode((width, height))

pygame.display.set_caption("Quiz")

running = True

question_index = 0

while running:
    surface.fill(white_colour)

    display_question(surface, question_index, (20, 20))

    display_options(surface)
    
    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if question_index + 1 != len(questions_array):
                    question_index += 1

            if event.key == pygame.K_LEFT:
                if question_index - 1 != -1:
                    question_index -= 1
