import pygame

pygame.init()

pygame.font.init()

quiz_font = pygame.freetype.Font('res/Roboto-Regular.ttf', 27)

def display_question(surface, question_index):
    quiz_font.render_to(surface, (20, 20), questions_array[question_index], (0, 0, 0))

def display_options_num(surface):
    quiz_font.render_to(surface, (20, 100), "1.  ", (0, 0, 0))
    quiz_font.render_to(surface, (20, 150), "2.  ", (0, 0, 0))
    quiz_font.render_to(surface, (20, 200), "3.  ", (0, 0, 0))
    quiz_font.render_to(surface, (20, 250), "4.  ", (0, 0, 0))

# def preprocess_string(string, index) -> str:
#     new_string = ""
#     for i, letter in enumerate(string):
#         if i % 20 == 0:
#             new_string += '\n'
#         new_string += letter

#     new_string = new_string[1:]

#     questions_array[index] = new_string

def display_options(surface, options_index):
    quiz_font.render_to(surface, (50, 100), options_array[options_index], (0, 0, 0))
    quiz_font.render_to(surface, (50, 150), options_array[options_index + 1], (0, 0, 0))
    quiz_font.render_to(surface, (50, 200), options_array[options_index + 2], (0, 0, 0))
    quiz_font.render_to(surface, (50, 250), options_array[options_index + 3], (0, 0, 0))

def remove_newline_from_string_array(arr):
    for i in range(len(arr)):
        arr[i] = arr[i].strip()

questions_array = []
options_array = []

with open("res/questions.txt") as questions_txtfile:
    questions_array = questions_txtfile.readlines()

with open("res/options.txt") as options_txtfile:
    options_array = options_txtfile.readlines()

remove_newline_from_string_array(questions_array)
remove_newline_from_string_array(options_array)

white_colour = (255, 255, 255)

width = 800

height = 500

surface = pygame.display.set_mode((width, height))

pygame.display.set_caption("Quiz")

running = True

question_index = 0
options_index = 0

# for i in range(len(questions_array)):
#     preprocess_string(questions_array[i], i)

while running:
    surface.fill(white_colour)

    display_question(surface, question_index)

    display_options_num(surface)
    
    display_options(surface, options_index)

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
                pygame.quit()