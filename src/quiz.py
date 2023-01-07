import pygame

pygame.init()

pygame.font.init()

quiz_font = pygame.freetype.Font('res/Roboto-Regular.ttf', 27)
game_over_font = pygame.freetype.Font('res/Roboto-Regular.ttf', 50)

b1color = (0, 0, 0)
b2color = (0, 0, 0)
b3color = (0, 0, 0)
b4color = (0, 0, 0)

score = 0

b1f = 1
b2f = 1
b3f = 1
b4f = 1

box_selected = [False, False, False, False]

save_button_filled = 1
submit_button_filled = 1

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
    pygame.draw.rect(surface, b1color, (15, 100, 20, 20), b1f)
    pygame.draw.rect(surface, b2color, (15, 150, 20, 20), b2f)
    pygame.draw.rect(surface, b3color, (15, 200, 20, 20), b3f)
    pygame.draw.rect(surface, b4color, (15, 250, 20, 20), b4f)

def draw_savebutton(surface):
    pygame.draw.rect(surface, (0, 255, 0), (1100, 400, 80, 50), save_button_filled)
    quiz_font.render_to(surface, (1107, 415), "SAVE", (0, 0, 0))

def draw_submitbutton(surface):
    pygame.draw.rect(surface, (0, 255, 0), (900, 400, 110, 50), submit_button_filled)
    quiz_font.render_to(surface, (907, 415), "SUBMIT", (0, 0, 0))


questions_array = []
options_array   = []
answers_array   = []

with open("res/questions.txt") as questions_txtfile:
    questions_array = questions_txtfile.readlines()

with open("res/options.txt") as options_txtfile:
    options_array = options_txtfile.readlines()

with open("res/answers.txt") as answers_txtfile:
    answers_array = answers_txtfile.readlines()

remove_newline_from_string_array(questions_array)
remove_newline_from_string_array(options_array)
remove_newline_from_string_array(answers_array)

for i in range(len(answers_array)):
    answers_array[i] = int(answers_array[i])

print("Answer: {}".format(answers_array))

user_given_answers_array = [None] * len(questions_array)

white_color = (255, 255, 255)
black_color = (0, 0, 0)

width   = 1200

height  = 500

surface = pygame.display.set_mode((width, height))

pygame.display.set_caption("Quiz")

running = True

question_index = 0
options_index  = 0
answers_index  = 0

is_quiz_over = False

while running:
    surface.fill(white_color)

    if is_quiz_over:
        game_over_font.render_to(surface, (500, 200), "Score: {}".format(score), (0, 0, 0))
        game_over_font.render_to(surface, (400, 350), "Press ESC to quit", (0, 0, 0))


    if not is_quiz_over:

        display_question(surface, question_index)

        display_options_num(surface)

        display_options(surface, options_index)

        draw_tickbox(surface)

        draw_savebutton(surface)

        draw_submitbutton(surface)

    pygame.display.flip()

    mouse_x = pygame.mouse.get_pos()[0]
    mouse_y = pygame.mouse.get_pos()[1]

    # save-button
    if mouse_x >= 1100 and mouse_x <= 1190 and mouse_y >= 400 and mouse_y <= 450:
        save_button_filled = 0
    else:
        save_button_filled = 1

    # submit-button
    if mouse_x >= 900 and mouse_x <= 1010 and mouse_y >= 400 and mouse_y <= 450:
        submit_button_filled = 0
    else:
        submit_button_filled = 1

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                if question_index + 1 != len(questions_array):
                    question_index += 1
                    options_index += 4
                    answers_index += 1

                    b1color = (0, 0, 0)
                    b2color = (0, 0, 0)
                    b3color = (0, 0, 0)
                    b4color = (0, 0, 0)

                    b1f = 1
                    b2f = 1
                    b3f = 1
                    b4f = 1

                    box_selected = [False, False, False, False]

            if event.key == pygame.K_LEFT:
                if question_index - 1 != -1:
                    question_index -= 1
                    options_index -= 4
                    answers_index -= 1

                    b1color = (0, 0, 0)
                    b2color = (0, 0, 0)
                    b3color = (0, 0, 0)
                    b4color = (0, 0, 0)

                    b1f = 1
                    b2f = 1
                    b3f = 1
                    b4f = 1

                    box_selected = [False, False, False, False]

            if event.key == pygame.K_ESCAPE:
                running = False

        if event.type == pygame.MOUSEBUTTONDOWN:
            # box 1
            if mouse_x >= 15 and mouse_x <= 35:
                if mouse_y >= 100 and mouse_y <= 120:
                    print("checkbox 1 clicked!")
                    b1color = (0, 255, 0)
                    b2color = (0, 0, 0)
                    b3color = (0, 0, 0)
                    b4color = (0, 0, 0)

                    b1f = 0
                    b2f = 1
                    b3f = 1
                    b4f = 1

                    box_selected[0] = True
                    box_selected[1] = False
                    box_selected[2] = False
                    box_selected[3] = False

                    print(box_selected)
            # box 2
            if mouse_x >= 15 and mouse_x <= 35:
                if mouse_y >= 150 and mouse_y <= 170:
                    print("checkbox 2 clicked!")
                    b2color = (0, 255, 0)
                    b1color = (0, 0, 0)
                    b3color = (0, 0, 0)
                    b4color = (0, 0, 0)

                    b1f = 1
                    b2f = 0
                    b3f = 1
                    b4f = 1

                    box_selected[0] = False
                    box_selected[1] = True
                    box_selected[2] = False
                    box_selected[3] = False

                    print(box_selected)
            # box 3
            if mouse_x >= 15 and mouse_x <= 35:
                if mouse_y >= 200 and mouse_y <= 220:
                    print("checkbox 3 clicked!")
                    b3color = (0, 255, 0)
                    b1color = (0, 0, 0)
                    b2color = (0, 0, 0)
                    b4color = (0, 0, 0)

                    b1f = 1
                    b2f = 1
                    b3f = 0
                    b4f = 1

                    box_selected[0] = False
                    box_selected[1] = False
                    box_selected[2] = True
                    box_selected[3] = False

                    print(box_selected)
            # box 4
            if mouse_x >= 15 and mouse_x <= 35:
                if mouse_y >= 250 and mouse_y <= 270:
                    print("checkbox 4 clicked!")
                    b4color = (0, 255, 0)
                    b1color = (0, 0, 0)
                    b2color = (0, 0, 0)
                    b3color = (0, 0, 0)

                    b1f = 1
                    b2f = 1
                    b3f = 1
                    b4f = 0

                    box_selected[0] = False
                    box_selected[1] = False
                    box_selected[2] = False
                    box_selected[3] = True

                    print(box_selected)

            # save button pressed
            if mouse_x >= 1100 and mouse_x <= 1190 and mouse_y >= 400 and mouse_y <= 450:
                print("Save button pressed")

                if(box_selected[0]):
                    user_given_answers_array[question_index] = 1
                elif(box_selected[1]):
                    user_given_answers_array[question_index] = 2
                elif(box_selected[2]):
                    user_given_answers_array[question_index] = 3
                elif(box_selected[3]):
                    user_given_answers_array[question_index] = 4

                print(user_given_answers_array)

            # submit button pressed
            if mouse_x >= 900 and mouse_x <= 1010 and mouse_y >= 400 and mouse_y <= 450:
                print("Submit button pressed")

                for i in range(len(answers_array)):
                    if answers_array[i] == user_given_answers_array[i]:
                        score += 1

                print("Score: {}".format(score))

                is_quiz_over = True