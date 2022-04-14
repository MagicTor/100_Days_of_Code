import tkinter as tk
from random import randint, choice, shuffle
from math import ceil, floor

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '+', '-', '_', '=', '(', ')', '{', '}', '[', ']', '\\',
           '/', '|', '.', ',', ':', ';', '<', '>', '?']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
upper = [letter.upper() for letter in lower]

password_characters = lower + upper + numbers + symbols

class Popup():
    def __init__(self):
        self.password = ""
        self.password_length = 16

        # UI Setup
        self.popup = tk.Toplevel()
        self.popup.title("Password Generator")
        self.popup.config(padx=30, pady=30)

        self.check_upper = tk.IntVar()
        self.check_upper.set(1)
        self.check_lower = tk.IntVar()
        self.check_lower.set(1)
        self.check_number = tk.IntVar()
        self.check_number.set(1)
        self.check_symbol = tk.IntVar()
        self.check_symbol.set(1)

        self.label_title = tk.Label(self.popup, text="Password Generator", fg='dark green', font=("Sergoe UI",16,"bold"))
        self.label_password = tk.Label(self.popup, text="Password", fg="blue", font=("Sergoe UI",16,"bold"),
                                       width=16, height=3, relief='sunken')
        self.scale_length = tk.Scale(self.popup, label="Password Length", from_=0, to=99, length=200,
                                     orient=tk.HORIZONTAL, command=self.scale)
        self.checkbox_upper = tk.Checkbutton(self.popup, text="Use A-Z", variable=self.check_upper, command=self.do_it)
        self.checkbox_lower = tk.Checkbutton(self.popup, text="Use a-z", variable=self.check_lower, command=self.do_it)
        self.checkbox_number = tk.Checkbutton(self.popup, text="Use 0-9", variable=self.check_number, command=self.do_it)
        self.checkbox_symbol = tk.Checkbutton(self.popup, text="Use !@#$%^&*", variable=self.check_symbol, command=self.do_it)
        self.label_number = tk.Label(self.popup, text="How many numbers", pady=5)
        self.label_symbol = tk.Label(self.popup, text="How many symbols", pady=5)
        self.spinbox_number = tk.Spinbox(self.popup, from_=1, to=99, width=3, command=self.do_it)
        self.spinbox_symbol = tk.Spinbox(self.popup, from_=1, to=99, width=3, command=self.do_it)
        self.button_close = tk.Button(self.popup, text="Close", command=self.close)

        self.scale_length.set(self.password_length)

        # Layout
        self.label_title.grid(column=0, row=0, columnspan=3)
        self.label_password.grid(column=0, row=1, columnspan=3)
        self.scale_length.grid(column=0, row=2, columnspan=3)
        self.checkbox_upper.grid(column=1, row=3, sticky=tk.W)
        self.checkbox_lower.grid(column=1, row=4, sticky=tk.W)
        self.checkbox_number.grid(column=1, row=5, sticky=tk.W)
        self.checkbox_symbol.grid(column=1, row=6, sticky=tk.W)
        self.label_number.grid(column=0, row=7, columnspan=2)
        self.spinbox_number.grid(column=2, row=7)
        self.label_symbol.grid(column=0, row=8, columnspan=2)
        self.spinbox_symbol.grid(column=2, row=8)
        self.button_close.grid(column=0, row=9, columnspan=3)

        # ---------------------------

        self.popup.mainloop()

    def scale(self, val):
        self.password_length = int(val)
        self.do_it()

    def do_it(self):
        """Create a password every time a widget is altered"""
        # Get Numbers
        number_qty = int(self.spinbox_number.get())
        symbol_qty = int(self.spinbox_symbol.get())

        space_taken = 0
        space_taken += 1 if self.check_lower.get() else space_taken
        space_taken += 1 if self.check_upper.get() else space_taken

        # Restrict numbers and symbols to half the password length
        if (number_qty + symbol_qty) >= (self.password_length - space_taken):
            self.spinbox_number["to"] = number_qty
            self.spinbox_symbol["to"] = symbol_qty
        else:
            self.spinbox_number["to"] = self.password_length - space_taken
            self.spinbox_symbol["to"] = self.password_length - space_taken

        remaining = self.password_length
        password_list = []
        if self.check_symbol.get():
            password_list += [choice(symbols) for char in range(symbol_qty)]
            remaining -= symbol_qty
        if self.check_number.get():
            password_list += [choice(numbers) for char in range(number_qty)]
            remaining -= number_qty
        if self.check_lower.get() and self.check_upper.get():
            letter_list = lower + upper
            password_list += [choice(letter_list) for char in range(remaining)]
        elif self.check_lower.get():
            password_list += [choice(lower) for char in range(remaining)]
        elif self.check_upper.get():
            password_list += [choice(upper) for char in range(remaining)]

        # password_list += [choice(upper)]
        # password_list = [choice(password_characters) for char in range(self.password_length)]

        self.password = "".join(password_list)
        self.label_password["text"] = self.password

    def close(self):
        self.popup.quit()   # This allows the password to be access by main.py
        self.popup.destroy()    # Then destroy this script window
