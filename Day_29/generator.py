import tkinter as tk
from random import randint, choice, shuffle
from math import ceil, floor

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['`', '~', '!', '@', '#', '$', '%', '^', '&', '*', '+', '-', '_', '=', '(', ')', '{', '}', '[', ']', '\\',
           '/', '|', '.', ',', ':', ';', '<', '>', '?']
lower = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
         'w', 'x', 'y', 'z']
upper = [letter.upper() for letter in lower]

class Popup():
    def __init__(self):
        self.password = ""
        self.password_length = 16
        self.remaining = 16
        self.qty_lower = 0
        self.list_password = []

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
        self.scale_length = tk.Scale(self.popup, label="Password Length", from_=1, to=99, length=200,
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
        """Create the password every time a widget is altered"""
        self.password = []  # Clear out any existing password
        self.remaining = self.password_length  # Number of characters in password yet to be filled

        number_qty = int(self.spinbox_number.get())
        symbol_qty = int(self.spinbox_symbol.get())

        # Restrict numbers and symbols to two less than the password length to make room for the upper and lowercase
        if self.check_number.get():
            self.spinbox_number["to"] = self.password_length - 2
        if self.check_symbol.get():
            self.spinbox_symbol["to"] = self.password_length - 2

        # Generate the password
        if self.check_symbol.get():
            self.password += [choice(symbols) for _ in range(0, symbol_qty)]
            self.remaining = self.password_length - len(self.password)
        if self.check_number.get():
            self.password += [choice(numbers) for _ in range(0, number_qty)]
            self.remaining = self.password_length - len(self.password)
        if self.check_lower.get() and self.remaining > 0:
            if self.check_upper.get():
                self.qty_lower = randint(1, self.remaining)
            else:
                self.qty_lower = self.remaining
            self.password += [choice(lower) for _ in range(1, self.qty_lower)]
            self.remaining = self.password_length - len(self.password)
        if self.check_upper.get() and self.remaining > 0:
            self.password += [choice(upper) for _ in range(0, self.remaining)]

        self.list_password = list(self.password)
        shuffle(self.list_password)
        self.password = "".join(self.list_password)
        self.label_password["text"] = self.password

    def close(self):
        self.popup.quit()   # This allows the password to be access by main.py
        self.popup.destroy()    # Then destroy this script window
