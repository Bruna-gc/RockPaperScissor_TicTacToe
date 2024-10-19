import tkinter as tk
from tkinter import ttk


def main(status_dict, winning_label, button_list, background_img, x_image, circle_image):
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

    # check win
    def win(type):
        for key in status_dict.items():
            print(key)

        if column1(type) or column2(type) or column3(type) or row1(type) or row2(type) or row3(type) or diagnal1(type) or diagnal2(type):
            return True
        

    def win_display():
        winning_label.config(text=f"Player {type} wins!")
        winning_label.grid(row=0, column=1)
        for button in button_list:
            button.config(state=tk.DISABLED)

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
            if win(type="x"):
                win_display()

        elif imageX_used == 1:
            circle_display(button)
            reset_status("x")
            change_button(button, button_number, "o")
            if win(type="o"):
                win_display()

        elif imageCircle_used == 1:
            x_display(button)
            reset_status("o")
            change_button(button, button_number, "x")
            if win(type="o"):
                win_display()
        button_disable(button)