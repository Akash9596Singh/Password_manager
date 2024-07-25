import random
from tkinter import *
from tkinter import messagebox
import pyperclip
import json


# ---------------------------- PASSWORD GENERATOR ------------------------------- #

def generate_password():
    # Password Generator Project
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list1 = [random.choice(letters) for i in range(nr_letters)]
    password_list2 = [random.choice(symbols) for i in range(nr_symbols)]
    password_list3 = [random.choice(numbers) for i in range(nr_numbers)]

    # for char in range(nr_letters):
    #     password_list.append(random.choice(letters))
    #
    # for char in range(nr_symbols):
    #     password_list += random.choice(symbols)
    #
    # for char in range(nr_numbers):
    #     password_list += random.choice(numbers)
    password_list = password_list1 + password_list2 + password_list3
    random.shuffle(password_list)

    password = ""
    password = ''.join(password_list)

    password_entry.insert(0, password)
    pyperclip.copy(password)


# ---------------------------- FIND PASSWORD ------------------------------- #
def search():
    web_entry = website_entry.get().title()
    try:
        with open('data.json', mode='r') as file:
            data = json.load(file)
    except FileNotFoundError:
        messagebox.showinfo(message="No Data File Found")
    else:
        if web_entry in data:
            messagebox.showinfo(title=web_entry,
                                message=f"Email: {data[web_entry]['email']}\nPassword: {data[web_entry]['password']}")
        else:
            messagebox.showinfo(message=f"No details found for the {web_entry} exists.")


# ---------------------------- SAVE PASSWORD ------------------------------- #
def add_password():
    web_entry = website_entry.get().title()
    name_entry = username_entry.get()
    pass_entry = password_entry.get()
    new_data = {web_entry: {
        "email": name_entry,
        "password": pass_entry,
    }}

    if len(web_entry) == 0 or len(name_entry) == 0 or len(pass_entry) == 0:
        messagebox.showinfo(title='Oops', message="Please don't leave any fields empty!")
    else:
        # Pop Up
        is_ok = messagebox.askokcancel(title=web_entry, message=f"These are the details entered:\n"
                                                                f"Email: {name_entry}\n"
                                                                f"Password: {pass_entry}\n"
                                                                f"Is it ok to save?")

        if is_ok:
            try:
                with open('data.json', mode="r") as file:
                    # reading old data
                    data = json.load(file)


            except FileNotFoundError:
                with open('data.json', mode="w") as file:
                    # saving updated data
                    json.dump(new_data, file, indent=4)
                    # file.write(f'{web_entry} | {name_entry} | {pass_entry}\n')
                    website_entry.delete(0, END)
                    password_entry.delete(0, END)


            except json.decoder.JSONDecodeError:
                with open('data.json', mode="w") as file:
                    # saving updated data
                    json.dump(new_data, file, indent=4)


            else:
                # updating old data
                data.update(new_data)
                with open('data.json', mode="w") as file:
                    # saving updated data
                    json.dump(data, file, indent=4)
                    # file.write(f'{web_entry} | {name_entry} | {pass_entry}\n')


            finally:
                website_entry.delete(0, END)
                password_entry.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #

window = Tk()
window.config(padx=50, pady=50)
# window.minsize(width=500,height=500)
window.title('Password Manager')
canvas = Canvas(height=200, width=200)
passwod_logo = PhotoImage(file='/Users/akashsingh/Desktop/100Days Python/Day29/password-manager-start/logo.png')
canvas.create_image(100, 100, image=passwod_logo)
canvas.grid(row=0, column=1)

#  WEBISTE LABEL
website_label = Label(text='Website:')
website_label.grid(row=1, column=0)

#  Email/username LABEL
username_label = Label(text='Email/Username:')
username_label.grid(row=2, column=0)

#  Password LABEL
password_label = Label(text='Password:')
password_label.grid(row=3, column=0)

# WEBSITE ENTRY
website_entry = Entry(width=21)
website_entry.focus()
website_entry.grid(row=1, column=1)

# Email/Username Entry
username_entry = Entry(width=36)
username_entry.insert(0, 'singh1508@gmail.com')
username_entry.grid(row=2, column=1, columnspan=2)

# Password Entry
password_entry = Entry(width=21)
password_entry.grid(row=3, column=1)

# Button


# Generate Button
generate_button = Button(width=11, text='Generate Password', command=generate_password)
generate_button.config(padx=0, pady=0)
generate_button.grid(row=3, column=2)

# Add Button

add_button = Button(width=34, text='Add', command=add_password)
add_button.grid(row=4, column=1, columnspan=2)

# search Button
search_button = Button(width=11, text='Search', command=search)
generate_button.config(padx=0, pady=0)
search_button.grid(row=1, column=2)

window.mainloop()

# JSON FILE
# write json.dump()
# write json.load()
# write json.update()
