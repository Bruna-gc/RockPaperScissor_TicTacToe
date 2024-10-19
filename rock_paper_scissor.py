import tkinter as tk
from tkinter import ttk
import random
import subprocess

# BUTTON CREATION :
# https://www.clickminded.com/button-generator/
# https://www.flaticon.com/free-icons/image-button

root = tk.Tk()
root.title("Rock Paper Scissor")
root.geometry("900x900")

global button_enable
button_enable = True

life = 3
computer_life = 3

computer_choice = {
    "0": "Rock",
    "1": "Paper",
    "2": "Scissor"
}

# variable with phrases
tie = "Tie!"
computer_Win = "Computer Win!"
player_win = "Player Win!"

life_label = tk.Label(root, text=f"Player Lives: {life}", font=('Bold Courier', 15))
comp_life_label = tk.Label(root, text=f"Computer: {computer_life}", font=('Bold Courier', 15))

# game status display (win, lose, tie)
string_game_status = tk.StringVar()
label = ttk.Label(root, textvariable=string_game_status)
label.grid(row=1, column=2, pady=20)

# images
rock_image = tk.PhotoImage(file='rock.png')
paper_image = tk.PhotoImage(file='paper.png')
scissor_image = tk.PhotoImage(file='scissor.png')
start_image = tk.PhotoImage(file='button_start.png')
reset_image = tk.PhotoImage(file="reset_button.png")

back_button = tk.PhotoImage(file="button_back.png")

# choice images display label
computer_image_label = tk.Label(root, borderwidth=0)
player_imgae_label = tk.Label(root, borderwidth=0)

def back_func():
    root.destroy()
    subprocess.run(["python3", "initial_interface.py"])

def reset_button():
    global life
    global computer_life
    computer_life = 3
    life = 3
    life_label.configure(text=f"Player Lives: {life}")
    comp_life_label.configure(text=f"Computer Lives: {computer_life}")
    # set variable to none.
    string_game_status.set("")
    button_status(button_enable)
    # reset image displayed
    computer_image_label.configure(image='')
    player_imgae_label.configure(image='')


def button_status(boolean_value):
    button_list = [rockButton, paperButton, scissorButton]
    if not boolean_value:
        for button in button_list:
            button.config(state=tk.DISABLED)
    elif boolean_value:
        for button in button_list:
            button.config(state=tk.NORMAL)


def display_image(variable, type=""):
    if type == "comp" or type == "":
        computer_image_label.configure(image=variable)
        computer_image_label.grid(row=2, column=0)
    elif type == "player":
        player_imgae_label.configure(image=variable)
        player_imgae_label.grid(row=2, column=6)


def display_label(string):
    string_game_status.set(string)
    label.configure(textvariable=string_game_status, font=('Courier', 25))


def rock():
    global life
    global computer_life
    cc = computer_choice[str(random.randint(0, 2))]
    if life > 0 and computer_life > 0:
        if cc == "Rock":
            display_label(tie)
            display_image(rock_image, type="comp")
        elif cc == "Paper":
            display_label(computer_Win)
            display_image(paper_image)
            life -= 1
            life_label.configure(text=f"Player Lives: {life}")
        else:
            display_label(player_win)
            display_image(scissor_image)
            computer_life -= 1
            comp_life_label.config(text=f"Computer Lives: {computer_life} ")
    else:
        button_enable = False
        button_status(button_enable)
        computer_life.config()

    display_image(rock_image, type="player")


def paper():
    global life
    global computer_life
    if life > 0 and computer_life > 0:
        cc = computer_choice[str(random.randint(0, 2))]
        if cc == "Rock":
            display_label(player_win)
            display_image(rock_image)
            computer_life -= 1
            comp_life_label.configure(text=f"Computer Lives: {computer_life}")
        elif cc == "Paper":
            display_label(tie)
            display_image(paper_image, type="comp")
        else:
            display_label(computer_Win)
            display_image(scissor_image)
            life -= 1
            life_label.configure(text=f"Player Lives: {life}")
    else:
        button_enable = False
        button_status(button_enable)
    display_image(paper_image, type="player")


def scissor():
    global life
    global computer_life
    if life > 0 and computer_life > 0:
        cc = computer_choice[str(random.randint(0, 2))]
        if cc == "Rock":
            display_label(computer_Win)
            display_image(rock_image)
            life -= 1
            life_label.configure(text=f"Player Lives: {life}")
        elif cc == "Paper":
            display_label(player_win)
            display_image(paper_image)
            computer_life -= 1
            comp_life_label.configure(text=f"Computer Lives: {computer_life}")
        else:
            display_label(tie)
            display_image(scissor_image, type="comp")
    else:
        button_enable = False
        button_status(button_enable)

    display_image(scissor_image, type="player")


# buttons
rockButton = tk.Button(root, text="Rock", command=rock, borderwidth=0, image=rock_image)
paperButton = tk.Button(root, text="Paper", command=paper, borderwidth=0, image=paper_image)
scissorButton = tk.Button(root, text="Scissor", command=scissor, borderwidth=0, image=scissor_image)
resetButton = tk.Button(root, text="Rest", command=reset_button, borderwidth=0, image=reset_image)

back = tk.Button(root, image=back_button, command=back_func, borderwidth=0)
back.grid(row=0, column=0)


rockButton.grid(row=6, column=0,)
paperButton.grid(row=6, column=2,)
scissorButton.grid(row=6, column=6,)

resetButton.grid(row=8, column=2, pady=40)

# grid label
ttk.Label(root, text="PLAYER", font=('Bold Courier', 15)).grid(row=5, column=6, pady=20)
ttk.Label(root, text="COMPUTER", font=('Bold Courier', 15)).grid(row=5, column=0, pady=20)
ttk.Label(root, text="Rock-Paper-Scissor", font=('Courier', 25)).grid(row=0, column=2, pady=30)
ttk.Label(root, text="VS", font=('Courier', 30)).grid(row=5, column=2)

life_label.grid(row=9, column=2)
comp_life_label.grid(row=10, column=2)

root.columnconfigure(0, weight=1)
root.columnconfigure(6, weight=1)

root.mainloop()
