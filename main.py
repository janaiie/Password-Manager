from tkinter import *
from tkinter import messagebox
from password_generator import generator
import pyperclip
import json


def generate_password():
    password = generator()
    entry_password.insert(0, password)
    pyperclip.copy(password)


def find_password():
    desired_website = entry_website.get().title()
    try:
        with open("credential_folder.json", "r") as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(title="Error", message="No Data found")
    else:
        if desired_website in data:
            password = data[desired_website]["password"]
            messagebox.showinfo(title=desired_website, message="Password saved to clipboard")
            pyperclip.copy(password)
        else:
            messagebox.showinfo(title="Error", message=f"No Details for {desired_website}")


def append_entry():
    site = entry_website.get().title()
    password = entry_password.get()
    email = entry_email_uname.get()

    new_data = {
        site: {
            "email": email,
            "password": password,
        }
    }

    if len(site) == 0 or len(password) == 0:
        messagebox.showinfo(title="Error", message="Fields cannot be empty")
    else:
        try:
            with open("credential_folder.json", "r") as file:
                data = json.load(file)
        except (FileNotFoundError, json.JSONDecodeError):
            with open("credential_folder.json", "w") as file:
                json.dump(new_data, file, indent=4)
        else:
            data.update(new_data)
            with open("credential_folder.json", "w") as file:
                json.dump(data, file, indent=4)
        finally:
            entry_website.delete(0, 'end')
            entry_password.delete(0, "end")


window = Tk()

window.config(padx=50, pady=50)
window.title("Password Manager")

canvas = Canvas(width=200, height=200)
tomato_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=tomato_img)
canvas.grid(column=1, row=0)

label_website = Label(text="Website:")
label_website.grid(column=0, row=1)

entry_website = Entry()
entry_website.grid(column=1, row=1, sticky="EW")
entry_website.focus()

label_email_uname = Label(text="Email/Username:")
label_email_uname.grid(column=0, row=2)

entry_email_uname = Entry()
entry_email_uname.grid(column=1, row=2, columnspan=2, sticky="EW")
entry_email_uname.insert(0, "example@gmail.com")

label_password = Label(text="Password:")
label_password.grid(column=0, row=3)

entry_password = Entry()
entry_password.grid(column=1, row=3, sticky="EW")

generate_btn = Button(text="Generate Password", command=generate_password)
generate_btn.grid(column=2, row=3, sticky="EW")

add_btn = Button(text="Add", width=35, command=append_entry)
add_btn.grid(column=1, row=4, columnspan=2, sticky="EW")

generate_btn = Button(text="Search", command=find_password)
generate_btn.grid(column=2, row=1, sticky="EW")

window.mainloop()