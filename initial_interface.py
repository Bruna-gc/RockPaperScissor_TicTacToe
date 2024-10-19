import tkinter as tk
import subprocess
# take funtion start from rock and put it here
# OBS: when close first window, the inital_window pop up

# https://www.clickminded.com/button-generator/

root = tk.Tk()
root.geometry("900x900")
root.title("Initial Interface")

# frame in root
frame = tk.Frame(root, height=64, width=64)
frame.grid(row=1, column=1)

root.columnconfigure(0, weight=1)
root.columnconfigure(2, weight=1)

root.rowconfigure(0, weight=1)
root.rowconfigure(2, weight=1)

rps = tk.PhotoImage(file="button_rock-paper-scissor.png")
ttt = tk.PhotoImage(file="button_tic-tac-toe.png")

def on_rps():
    # running other file using run()
    root.destroy()
    subprocess.run(["python3", "rock_paper_scissor.py"])

def on_ttt():
    root.destroy()
    subprocess.run(["python3", "tic_tac_toe.py"])

# buttons
rps_button = tk.Button(frame, image=rps, command=on_rps, borderwidth=0)
ttt_button = tk.Button(frame, image=ttt, command=on_ttt, borderwidth=0)

# label
welcome_label = tk.Label(root, text="WELCOME! CHOSE YOUR GAME!", font=('Courier', 30))

rps_button.grid(row=3, column=3, padx=20)
ttt_button.grid(row=3, column=4, padx=20)
welcome_label.grid(row=0, column=1, pady=20)

root.mainloop()