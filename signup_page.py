from tkinter import *
import tkinter as tk
from tkinter import messagebox
from PIL import Image, ImageTk
import ast
import hashlib

class SignupPage:
    def __init__(self, root):
        self.root = root
        self.root.title("Sign Up")
        self.root.geometry('925x500+300+200')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        # Load and display the background image
        img = Image.open('login.png')
        img = img.resize((425, 425))  # Resize the image to fit the window
        self.photo = ImageTk.PhotoImage(img)
        self.image_label = Label(self.root, image=self.photo, bg='white')
        self.image_label.place(x=50, y=50)

        self.create_signup_form()

        self.root.mainloop()

    def create_signup_form(self):
        frame = tk.Frame(self.root, width=350, height=400, bg="white")
        frame.place(x=480, y=70)

        heading = tk.Label(frame, text='Sign Up', fg="#57a1f8", bg='white', font=('Microsoft Yahei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        def signup():
            username = self.user.get()
            password = self.code.get()
            confirm_password = self.confirm_code.get()

            if password == confirm_password:
                try:
                    file = open('datasheet.txt', 'r+')
                    d = file.read()
                    r = ast.literal_eval(d)

                    # Hash the password before storing it
                    hashed_password = self.hash_password(password)

                    dict2 = {username: hashed_password}
                    r.update(dict2)
                    file.truncate(0)
                    file.close()

                    file = open('datasheet.txt', 'w')
                    w = file.write(str(r))

                    messagebox.showinfo('Sign Up', 'Successfully signed up')

                except Exception as e:
                    print(e)
                    file = open('datasheet.txt', 'w')
                    pp = str({'Username': 'password'})
                    file.write(pp)
                    file.close()

            else:
                messagebox.showerror('Invalid', "Both Passwords should match")

        self.user = tk.Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind("<FocusIn>", self.on_enter_user)
        self.user.bind("<FocusOut>", self.on_leave_user)

        tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=107)

        self.code = tk.Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        self.code.place(x=30, y=150)
        self.code.insert(0, 'Password')
        self.code.bind("<FocusIn>", self.on_enter_code)
        self.code.bind("<FocusOut>", self.on_leave_code)

        tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=177)

        self.confirm_code = tk.Entry(frame, width=25, fg='black', border=0, bg='white', font=('Microsoft Yahei UI Light', 11))
        self.confirm_code.place(x=30, y=220)
        self.confirm_code.insert(0, 'Confirm Password')
        self.confirm_code.bind("<FocusIn>", self.on_enter_confirm)
        self.confirm_code.bind("<FocusOut>", self.on_leave_confirm)

        tk.Frame(frame, width=295, height=2, bg='black').place(x=25, y=247)

        tk.Button(frame, width=39, pady=7, text='Sign Up', bg='#57a1f8', fg='white', border=0, command=signup).place(x=35, y=280)

        label = tk.Label(frame, text='I have an account', fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=90, y=340)

        sign_in = tk.Button(frame, width=6, text='Sign in', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=self.signin)
        sign_in.place(x=200, y=340)

    def on_enter_user(self, e):
        if self.user.get() == 'Username':
            self.user.delete(0, 'end')

    def on_leave_user(self, e):
        if self.user.get() == '':
            self.user.insert(0, 'Username')

    def on_enter_code(self, e):
        if self.code.get() == 'Password':
            self.code.delete(0, 'end')
            self.code.config(show='*')  # Show asterisks when entering password

    def on_leave_code(self, e):
        if self.code.get() == '':
            self.code.insert(0, 'Password')
            self.code.config(show='')  # Hide text when not focused

    def on_enter_confirm(self, e):
        if self.confirm_code.get() == 'Confirm Password':
            self.confirm_code.delete(0, 'end')
            self.confirm_code.config(show='*')  # Show asterisks when entering password

    def on_leave_confirm(self, e):
        if self.confirm_code.get() == '':
            self.confirm_code.insert(0, 'Confirm Password')
            self.confirm_code.config(show='')  # Hide text when not focused

    def hash_password(self, password):
        # Create a hash object
        hasher = hashlib.sha256()
        # Update the hash object with the password
        hasher.update(password.encode('utf-8'))
        # Get the hexadecimal representation of the hash
        return hasher.hexdigest()

    def signin(self):
        self.root.destroy()

if __name__ == "__main__":
    root = tk.Tk()
    signup_page = SignupPage(root)
