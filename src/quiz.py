import pygame

pygame.init()

pygame.font.init()

quiz_font = pygame.freetype.Font('res/Roboto-Regular.ttf', 27)

def display_question(surface, question_index):
    quiz_font.render_to(surface, (20, 20), questions_array[question_index], (0, 0, 0))

def display_options_num(surface):
    quiz_font.render_to(surface, (50, 100), "1.  ", (0, 0, 0))
    quiz_font.render_to(surface, (50, 150), "2.  ", (0, 0, 0))
    quiz_font.render_to(surface, (50, 200), "3.  ", (0, 0, 0))
    quiz_font.render_to(surface, (50, 250), "4.  ", (0, 0, 0))

def display_options(surface, options_index):
    quiz_font.render_to(surface, (80, 100), options_array[options_index], (0, 0, 0))
    quiz_font.render_to(surface, (80, 150), options_array[options_index + 1], (0, 0, 0))
    quiz_font.render_to(surface, (80, 200), options_array[options_index + 2], (0, 0, 0))
    quiz_font.render_to(surface, (80, 250), options_array[options_index + 3], (0, 0, 0))

def remove_newline_from_string_array(arr):
    for i in range(len(arr)):
        arr[i] = arr[i].strip()

def draw_tickbox(surface):
    pygame.draw.rect(surface, black_color, (15, 100, 20, 20), 1)
    pygame.draw.rect(surface, black_color, (15, 150, 20, 20), 1)
    pygame.draw.rect(surface, black_color, (15, 200, 20, 20), 1)
    pygame.draw.rect(surface, black_color, (15, 250, 20, 20), 1)

questions_array = []
options_array = []

with open("res/questions.txt") as questions_txtfile:
    questions_array = questions_txtfile.readlines()

with open("res/options.txt") as options_txtfile:
    options_array = options_txtfile.readlines()

remove_newline_from_string_array(questions_array)
remove_newline_from_string_array(options_array)

white_color = (255, 255, 255)
black_color = (0, 0, 0)

width = 1200

height = 500

surface = pygame.display.set_mode((width, height))

pygame.display.set_caption("Quiz")

running = True

question_index = 0
options_index = 0

while running:
    surface.fill(white_color)

    display_question(surface, question_index)

    display_options_num(surface)
    
    display_options(surface, options_index)

    draw_tickbox(surface)

    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if question_index + 1 != len(questions_array):
                    question_index += 1
                    options_index += 4

            if event.key == pygame.K_LEFT:
                if question_index - 1 != -1:
                    question_index -= 1
                    options_index -= 4

            if event.key == pygame.K_ESCAPE:
                running = False