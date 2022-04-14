from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import generator
import pyperclip
# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():

    popup = generator.Popup()
    password = popup.password
    password_entry.delete(0, END)
    password_entry.insert(0, password)
    pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():

    website = website_entry.get()
    email = email_entry.get()
    username = username_entry.get()
    password = password_entry.get()

    if len(website) == 0 or len(username) == 0 or len(password) == 0 or len(email) == 0:
        messagebox.showinfo(title="Oops", message="Please don't leave any fields empty!")
    else:
        is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered: \nEmail: {email} "
                                                              f"\nUsername: {username}\nPassword: {password} \n"
                                                              f"Is it ok to save?")
        if is_ok:
            with open("data.txt", "a") as file:
                file.write(f"{website} | {email} | {username} | {password}\n")
                website_entry.delete(0, END)
                email_entry.insert(0, common_email)
                username_entry.delete(0, END)
                password_entry.delete(0, END)

# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=20, pady=20)

canvas = Canvas(width=200, height=200)
logo = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo)
canvas.grid(column=1, row=0)

website_label = Label(text="Website:")
website_label.grid(column=0, row=1)
website_entry = Entry(width=52)
website_entry.grid(column=1, row=1, columnspan=2, sticky='W')
website_entry.focus()

common_email = "example@live.com"
email_label = Label(text="Email:")
email_label.grid(column=0, row=2)
email_entry = Entry(width=52)
email_entry.insert(END, string=common_email)
email_entry.grid(column=1, row=2, columnspan=2, sticky='W')

username_label = Label(text="Username:")
username_label.grid(column=0, row=3)
username_entry = Entry(width=52)
username_entry.grid(column=1, row=3, columnspan=2, sticky='W')

password_label = Label(text="Password:")
password_label.grid(column=0, row=4)
password_entry = Entry(width=33)
password_entry.grid(column=1, row=4, sticky='W')

generate_password_button = Button(text="Generate Password", command=generate_password)
generate_password_button.grid(column=2, row=4)

add_button = Button(text="Add", width=44, command=save)
add_button.grid(column=1, row=5, columnspan=2, sticky='W')


window.mainloop()
