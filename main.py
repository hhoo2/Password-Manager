# Import necessary modules
from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json

# ---------------------------- PASSWORD GENERATOR ------------------------------- #
def generate_password():
  # Clear the password entry field
  password_entry.delete(0, END)

  # Define character sets for generating a password
  letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
  numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
  symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

  # Generate random characters for the password
  password_letters = [choice(letters) for _ in range(randint(8, 10))]
  password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
  password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

  # Combine the characters and shuffle them to create the password
  password_list = password_letters + password_symbols + password_numbers
  shuffle(password_list)
  password = "".join(password_list)

  # Insert the generated password into the password entry field and copy it to the clipboard
  password_entry.insert(0, password)
  pyperclip.copy(password)

# ---------------------------- SAVE PASSWORD ------------------------------- #
def save():
  # Get the user input for website, email, and password
  website = website_entry.get()
  email = email_entry.get()
  password = password_entry.get()
  new_data = {
    website: {
    "email": email,
    "password": password,
    }
  }
  # Check if the website and password fields are not empty
  if len(website) == 0 or len(password) == 0:
      messagebox.showinfo(title="Oops",message="Please make sure you haven't left any fields empty")
  else:
    # Prompt the user to confirm saving the details
    is_ok = messagebox.askokcancel(title=website, message=f"These are the details entered:\n\nEmail: {email}\nPassword: {password}\n\nIs it ok to save?")
    if is_ok:
        # Append the website, email, and password to a jason file and clear the input fields
      try:
        with open("password_data.json", "r") as data_file:
          #reading old data
          data = json.load(data_file)
      except FileNotFoundError:
        with open("password_data.json", "w") as data_file:
          json.dump(new_data,data_file,indent = 4)
      else:
        #updating old data with new data
        data.update(new_data)
        with open("password_data.json", "w") as data_file:
          #saving updated data
          json.dump(data,data_file, indent = 4)
      finally:
        website_entry.delete(0, END)
        password_entry.delete(0, END)

# ---------------------------- SEARCH PASSWORD ------------------------------- #
def search():
  website = website_entry.get()
  try:
  # open the file
    with open("password_data.json") as data_file:
      data =json.load(data_file) 
  except FileNotFoundError:
    messagebox.showinfo(title="Error", message="No Data File Found.")
  else:
    # check if the website is in the file
    if website in data:
      email = data[website]["email"]
      password = data[website]["password"]
      messagebox.showinfo(title=website, message=f"Email: {email}\nPassword:{password}")
    else:
      messagebox.showinfo(title="Error", message=f"No details for {website} exists.")
 
# ---------------------------- UI SETUP ------------------------------- #
# Create the main window
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

# Create a canvas and display the logo image
canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
logo_img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=logo_img)
canvas.grid(row=0, column=1)

# Labels for website, email, and password
website_label = Label(text="Website:", bg="white")
website_label.grid(row=1, column=0)
email_label = Label(text="Email/Username:", bg="white")
email_label.grid(row=2, column=0,columnspan=2)
password_label = Label(text="Password:", bg="white")
password_label.grid(row=3, column=0)

# Entry fields for website, email, and password
website_entry = Entry()
website_entry.grid(row=1, column=1)
website_entry.focus()
email_entry = Entry(width=38)
email_entry.grid(row=2, column=1, columnspan=2)
email_entry.insert(0, "youremail@gmail.com")
password_entry = Entry()
password_entry.grid(row=3, column=1)

# Buttons for generating a password and saving the information
search_button = Button(text="Search",width=12,command=search)
search_button.grid(row=1, column=2) 
generate_password_button = Button(text="Generate Password",command=generate_password)
generate_password_button.grid(row=3, column=2)
add_button = Button(text="Add", width=36, command=save)
add_button.grid(row=4, column=1, columnspan=2)

# Start the GUI application
window.mainloop()
