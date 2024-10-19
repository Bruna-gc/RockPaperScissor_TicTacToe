import tkinter as tk
from tkinter import ttk
import subprocess

root = tk.Tk()
root.title("Tic Tac Toe")
root.geometry("900x900")

# global variables to switch between x and o images
global imageX_used
imageX_used = False

global imageCircle_used
imageCircle_used = False

# images
circle_image = tk.PhotoImage(file="ooo.png")
background_img = tk.PhotoImage(file="purple.png")
x_image = tk.PhotoImage(file="xxx.png")
reset_button_image = tk.PhotoImage(file="reset_button.png")

# home 
back_image = tk.PhotoImage(file="button_back.png")

# frame in root.
frame = ttk.Frame(root, width=64, height=64)
# those positions so it can strech
frame.grid(row=1, column=1)

x = ""
# label
winning_label = tk.Label(root, text=f"Player {x} wins", font=('Courier', 30))

# center frame
root.columnconfigure(0, weight=1)
root.columnconfigure(2, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

# button dictionary
status_dict = {
    "button1": "",
    "button2": "",
    "button3": "",
    "button4": "",
    "button5": "",
    "button6": "",
    "button7": "",
    "button8": "",
    "button9": "",
}


# columns
def column1(type):
    if (status_dict["button1"] + status_dict["button4"] + status_dict["button7"]) == (3 * type):
        return True

def column2(type):
    if (status_dict["button2"] + status_dict["button5"] + status_dict["button8"]) == (3 * type):
        return True
    else:
        return False

def column3(type):
    if (status_dict["button3"] + status_dict["button6"] + status_dict["button9"]) == (3 * type):
        return True
    else:
        return False

# rows
def row1(type):
    if (status_dict["button1"] + status_dict["button2"] + status_dict["button3"]) == (3 * type):
        return True
    else:
        return False

def row2(type):
    if (status_dict["button4"] + status_dict["button5"] + status_dict["button6"]) == (3 * type):
        return True
    else:
        return False

def row3(type):
    if (status_dict["button7"] + status_dict["button8"] + status_dict["button9"]) == (3 * type):
        return True
    else:
        return False

# diagnals
def diagnal1(type):
    if (status_dict["button1"] + status_dict["button5"] + status_dict["button9"]) == (3 * type):
        return True
    else:
        return False

def diagnal2(type):
    if (status_dict["button7"] + status_dict["button5"] + status_dict["button3"]) == (3 * type):
        return True
    else:
        return False
    

def back_func():
    root.destroy()
    subprocess.run(["python3", "initial_interface.py"])

# check win
def check_win(type):
    count = 0
    for key in status_dict.items():
        print(key)

    if column1(type) or column2(type) or column3(type) or row1(type) or row2(type) or row3(type) or diagnal1(type) or diagnal2(type):
        winning_label.config(text=f"Player {type} wins!")
        winning_label.grid(row=0, column=1)
        for button in button_list:
                button.config(state=tk.DISABLED)
    else:
        for button in status_dict:
            if status_dict[button] != "":
                count += 1
                if count == 9:
                    winning_label.config(text="Tie!")
                    winning_label.grid(row=0, column=1)
            
def reset():
    for button in button_list:
        button.config(state=tk.ACTIVE, image=background_img)
        for button in status_dict:
            status_dict[button] = ""
    winning_label.grid_forget()

def reset_status(image):
    global imageX_used
    global imageCircle_used

    if image == "x":
        if imageX_used == 0:
            imageX_used = True
        else:
            imageX_used = False

    elif image == "o":
        if imageCircle_used == 0:
            imageCircle_used = True
        else:
            imageCircle_used = False

def button_disable(button, type=""):
    button.config(state=tk.DISABLED)

def x_display(button):
    button.config(image=x_image)

def circle_display(button):
    button.config(image=circle_image)

def change_button(button, button_number, value):
    button_number = "button" + button_number
    print(button_number)
    status_dict[button_number] = value
    print(status_dict[button_number])

# button press
def button_press(button, button_number):
    global imageCircle_used
    global imageX_used

    if imageX_used == 0 and imageCircle_used == 0:
        # first player must be x
        x_display(button)
        reset_status("x")
        change_button(button, button_number, "x")
        check_win(type="x")

    elif imageX_used == 1:
        circle_display(button)
        reset_status("x")
        change_button(button, button_number, "o")
        check_win(type="o")

    elif imageCircle_used == 1:
        x_display(button)
        reset_status("o")
        change_button(button, button_number, "x")
        check_win(type="o")
    button_disable(button)

# buttons colum 1
button1 = tk.Button(frame, image=background_img, command=lambda x="1": button_press(button1, x), borderwidth=0)
button4 = tk.Button(frame, image=background_img, command=lambda x="4": button_press(button4, x), borderwidth=0)
button7 = tk.Button(frame, image=background_img, command=lambda x="7": button_press(button7, x), borderwidth=0)

# button colum 2
button2 = tk.Button(frame, image=background_img, command=lambda x="2": button_press(button2, x), borderwidth=0)
button5 = tk.Button(frame, image=background_img, command=lambda x="5": button_press(button5, x), borderwidth=0)
button8 = tk.Button(frame, image=background_img, command=lambda x="8": button_press(button8, x), borderwidth=0)

# buttons colum 3
button3 = tk.Button(frame, image=background_img, command=lambda x="3": button_press(button3, x), borderwidth=0)
button6 = tk.Button(frame, image=background_img, command=lambda x="6": button_press(button6, x), borderwidth=0)
button9 = tk.Button(frame, image=background_img, command=lambda x="9": button_press(button9, x), borderwidth=0)

back_button = tk.Button(root, image=back_image,command=back_func, borderwidth=0)

# reset button
reset_button = tk.Button(root, image=reset_button_image, command=reset, borderwidth=0)

# list of buttons
button_list = [button1, button2, button3, button4, button5, button6, button7, button8, button9]

# grid reset
reset_button.grid(row=2, column=1)

# grid buttons 1 column
button1.grid(row=2, column=1)
button4.grid(row=5, column=1)
button7.grid(row=8, column=1)

# grid buttons 2 column
button2.grid(row=2, column=3)
button5.grid(row=5, column=3)
button8.grid(row=8, column=3)

# grid buttons 3 column
button3.grid(row=2, column=6)
button6.grid(row=5, column=6)
button9.grid(row=8, column=6)

back_button.grid(row=0, column=0)


root.mainloop()