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

    print("Result: {}".format(result))
    
    input_textbox.delete(0, END)
    
    last_operator = "+"

def sub():
    global result
    global last_operator

    if(last_operator == ""):
        result = float(input_data.get())
    else:
        result -= float(input_data.get())

    print("Result: {}".format(result))
    
    input_textbox.delete(0, END)
    
    last_operator = "-"

def mult():
    global result
    global last_operator

    if(last_operator == ""):
        result = float(input_data.get())
    else:
        result *= float(input_data.get())

    print("Result: {}".format(result))
    
    input_textbox.delete(0, END)
    
    last_operator = "*"

def div():
    global result
    global last_operator

    if(last_operator == ""):
        result = float(input_data.get())
    else:
        result /= float(input_data.get())
    
    print("Result: {}".format(result))

    input_textbox.delete(0, END)
    
    last_operator = "/"

def equal():
    global result
    global last_operator

    if last_operator == "+":
        result += float(input_data.get())
        
        input_textbox.delete(0, END)
        
        input_textbox.insert(0, str(result))

        result = 0

        print("Last operator: {}".format(last_operator))
        print("Result: {}".format(result))
    elif last_operator == "-":
        result -= float(input_data.get())
        
        input_textbox.delete(0, END)
        
        input_textbox.insert(0, str(result))

        result = 0
        print("Last operator: {}".format(last_operator))
        print("Result: {}".format(result))
    elif last_operator == "*":
        result *= float(input_data.get())
        
        input_textbox.delete(0, END)
        
        input_textbox.insert(0, str(result))

        result = 0
        print("Last operator: {}".format(last_operator))
        print("Result: {}".format(result))
    elif last_operator == "/":
        result /= float(input_data.get())
        
        input_textbox.delete(0, END)
        
        input_textbox.insert(0, str(result))

        result = 0
        print("Last operator: {}".format(last_operator))
        print("Result: {}".format(result))
    
    last_operator = ""

def clear():
    input_textbox.delete(0, END)

frame = LabelFrame(root, width = 300, height = 50, bd = 0)

frame.pack()

input_data = StringVar()

input_textbox = Entry(frame, text = input_data, bd = 0, font=('Roboto 50'))

input_textbox.pack()
input_textbox.focus_set()

add_button = Button(root, text = "+", command = add, font = ('Consolas 30'))
add_button.place(x = 0, y = 300, width = 50, height = 50)

equal_button = Button(root, text = "=", command = equal, font = ('Consolas 30'))
equal_button.place(x = 0, y = 350, width = 50, height = 50)

clear_button = Button(root, text = "Clear", command = clear, font = ('Consolas 10'))
clear_button.place(x = 100, y = 350, width = 50, height = 50)

sub_button = Button(root, text = "-", command = sub, font = ('Consolas 30'))
sub_button.place(x = 0, y = 250, width = 50, height = 50)

mult_button = Button(root, text = "*", command = mult, font = ('Consolas 30'))
mult_button.place(x = 0, y = 200, width = 50, height = 50)

div_button = Button(root, text = "/", command = div, font = ('Consolas 30'))
div_button.place(x = 0, y = 150, width = 50, height = 50)

root.mainloop()