
# Password Manager
## Author
- Hay Oo

![alt text](/logoscreen.png)

<b><a href="https://replit.com/@HayOo1/Password-Manager" style="color:purple;">Click here to use this program in Replit</a></b>

## Introduction

This is a simple Password Manager program developed using Python and the Tkinter library. The program provides an easy-to-use graphical user interface (GUI) to generate and store website passwords securely. It allows you to generate strong passwords, save them along with the associated website and your email/username, and manage your login information efficiently.

## Features

- **Password Generation:** The program can generate strong, random passwords containing letters (both uppercase and lowercase), numbers, and special symbols. You can customize the length and complexity of the generated passwords.

- **Password Storage:** Save website details, email or username, and passwords securely. The information is stored in a text file for future reference.

- **Clipboard Integration:** You can easily copy generated passwords to your clipboard, making it convenient to use them for account registration or login.

## Getting Started

### Prerequisites

- Python 3.x is required to run this program. You can download it from [python.org](https://www.python.org/downloads/).

### Installation

1. Clone or download the repository to your local machine.

2. Install the required Python packages:
   ```bash
   pip install pyperclip
   ```

### Usage

1. Run the program using the following command:
   ```bash
   python password_manager.py
   ```

2. Use the GUI to generate passwords and save website login information.

## How It Works

- **Generate Password:** Click the "Generate Password" button to create a random, secure password. You can customize the password length and complexity.

- **Save Password:** Fill in the website, email/username, and password fields, then click the "Add" button to save the information. The data is stored in a text file named "password_data.txt."

- **Clipboard Integration:** The generated password is automatically copied to your clipboard for easy pasting.

## Acknowledgments

- The program was developed as part of a Udemy Python programming course.
- The Tkinter library was used for creating the graphical user interface.
- Random password generation was implemented using Python's `random` module.

---

**Disclaimer**: This password manager is a simple project for educational purposes. It may not provide the same level of security as dedicated password management software. Use it responsibly, and consider using a trusted password manager for important and sensitive information.

