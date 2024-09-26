from tkinter import Tk, Label, Button, Entry, END
from random import shuffle

# making our Ui
window = Tk()
window.title("password ganerator")
window.geometry("400x400")
window.grid_columnconfigure(1, weight=1)

# making website lable and entry
website = Label(window, text="Website:")
website.grid(row=0, column=0, padx=10, pady=10)
website_entry = Entry(window, width=50)
website_entry.grid(row=0, column=1, columnspan=2, padx=(0, 10), pady=10, sticky="ew")
# making username lable and entry
username = Label(window, text="Username:")
username.grid(row=1, column=0, padx=10, pady=(0, 10))
username_entry = Entry(window, width=50)
username_entry.grid(row=1, column=1, columnspan=2, padx=(0, 10), pady=(0, 10), sticky="ew")
# making password lable and entry
password = Label(window, text="Password:")
password.grid(row=2, column=0, padx=10, pady=(0, 10))
password_entry = Entry(window, width=20)
password_entry.grid(row=2, column=1, padx=(0, 10), pady=(0, 10), sticky="ew")


# generator function
def password_generator():
    # 1 getting values from username entry and website and concating them
    website = website_entry.get()
    username = username_entry.get()
    website_and_username = f"{website}{username}"
    # 2 making list of characters
    password_characters = []
    for password in website_and_username:
        password_characters.append(password)
        # 3 shuffeling the password list and generate a new password
        shuffle(password_characters)
        new_password = ""
        for index in password_characters:
            new_password += index
            password_entry.delete(0, END)
            password_entry.insert(0, new_password)


# generate password button
Generate_passord_button = Button(window, text="Generate password", command=password_generator)
Generate_passord_button.grid(row=2, column=2, padx=(0, 10), pady=(0, 10), sticky="e")

window.mainloop()
