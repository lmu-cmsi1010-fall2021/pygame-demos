"""
Description: Test tkinter buttons, labels, and layout managers.
Author: Dr. Korpusik
Date: 11/5/2020
"""

import tkinter as tk


def button_pressed():
    print('The button was pressed!')

window = tk.Tk()

frame = tk.LabelFrame(window, text='Commands')
frame.grid(row=1, column=1)

label = tk.Label(frame, text='tk.button')
label.grid(row=2, column=1)

button = tk.Button(frame, text='do something')
button.grid(row=2, column=2)
button['command'] = button_pressed

window.mainloop()