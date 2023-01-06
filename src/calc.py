from tkinter import *

root = Tk()
root.title('Calculator')

window_width = 300
window_height = 400

screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

center_x = int(screen_width / 2 - window_width / 2)
center_y = int(screen_height / 2 - window_height / 2)

root.geometry(f'{window_width}x{window_height}+{center_x}+{center_y}')
root.resizable(False, False)
root.maxsize(window_width, window_height)

last_operator = ""

result = 0

def add():
    global result
    global last_operator

    result += float(input_data.get())
    
    input_textbox.delete(0, END)
    
    last_operator = "+"

def equal():
    if last_operator == "+":
        global result

        result += float(input_data.get())
        
        input_textbox.delete(0, END)
        
        input_textbox.insert(0, str(result))

        result = 0

def clear():
    input_textbox.delete(0, END)

frame = LabelFrame(root, width = 300, height = 50, bd = 0)

frame.pack()

input_data = StringVar()

input_textbox = Entry(frame, text = input_data, bd = 0, font=('Roboto 50'))

input_textbox.pack()
input_textbox.focus_set()

calculate_button = Button(root, text = "+", command = add)
calculate_button.place(x = 0, y = 300, width = 50, height = 50)

equal_button = Button(root, text = "=", command = equal)
equal_button.place(x = 0, y = 350, width = 50, height = 50)

print(input_data)

root.mainloop()