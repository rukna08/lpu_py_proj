from tkinter import *

root = Tk()
root.title('Child Calorie Calculator')

window_width = 300
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.maxsize(window_width, window_height)
root.iconbitmap('baby_icon.ico')

def print_calories(cal):
    cal_label = Label(root, text = "Intake " + str(cal) + " cal per day", fg = "green", font = ("Roboto", 16))
    cal_label.place(x = 20, y = 300)

    cal_label_perday = Label(root, text = "Intake " + "{:.2f}".format(cal / 4) + " cal per meal", fg = "green", font = ("Roboto", 16))
    cal_label_perday.place(x = 20, y = 330)


def calculate():
    if gender.get() == 1:
        cal_male = (10 * float(weight.get())) + (6.25 * float(height.get())) - (5 * float(age.get())) + 5
        print_calories(cal_male)
    else:    
        cal_female = (10 * float(weight.get())) + (6.25 * float(height.get())) - (5 * float(age.get())) - 161
        print_calories(cal_female)

weight = StringVar()
height = StringVar()
age = StringVar()
fat = StringVar()

weight_label = Label(root, text = "Weight: ", fg = "black")
weight_label.place(x = 20, y = 0)
weight_textbox = Entry(root, text = weight, bd = 1)
weight_textbox.place(x = 100, y = 0)

height_label = Label(root, text = "Height: ", fg = "black")
height_label.place(x = 20, y = 25)
height_textbox = Entry(root, text = height, bd = 1)
height_textbox.place(x = 100, y = 25)

age_label = Label(root, text = "Age: ", fg = "black")
age_label.place(x = 20, y = 50)
age_textbox = Entry(root, text = age, bd = 1)
age_textbox.place(x = 100, y = 50)

fat_label = Label(root, text = "Fat: ", fg = "black")
fat_label.place(x = 20, y = 75)
fat_textbox = Entry(root, text = fat, bd = 1)
fat_textbox.place(x = 100, y = 75)

gender = IntVar()

male_radio = Radiobutton(root, text = "Male: ", variable = gender, value = 1)
female_radio = Radiobutton(root, text = "Female: ", variable = gender, value = 2)

male_radio.place(x = 20, y = 125)
female_radio.place(x = 20, y = 150)

calculate_button = Button(root, text = "Calculate", command = calculate)
calculate_button.place(x = 20, y = 200)

root.mainloop()