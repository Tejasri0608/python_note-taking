from tkinter import *
from tkinter import messagebox
import ast
from PIL import Image, ImageTk
from signup_page import SignupPage  # Import the SignupPage class
from menu import MenuPage
import hashlib

class LoginPage:
    def __init__(self, root):
        self.root = root
        self.root.title('Login')
        self.root.geometry('925x500+300+200')
        self.root.configure(bg="#fff")
        self.root.resizable(False, False)

        # Load and display the background image
        img = Image.open('ss.jpeg')
        img = img.resize((425, 425))  # Resize the image to fit the window
        self.photo = ImageTk.PhotoImage(img)
        self.image_label = Label(self.root, image=self.photo, bg='white')
        self.image_label.place(x=50, y=50)

        # Create and place the login form
        self.create_login_form()

        self.root.mainloop()

    def create_login_form(self):
        frame = Frame(self.root, width=350, height=350, bg="white")
        frame.place(x=480, y=70)

        heading = Label(frame, text='Login Page', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=100, y=5)

        # Create and place the username entry field
        self.user = Entry(frame, width=25, fg="black", border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.user.place(x=30, y=80)
        self.user.insert(0, 'Username')
        self.user.bind('<FocusIn>', self.on_enter_user)
        self.user.bind('<FocusOut>', self.on_leave_user)

        Frame(frame, width=295, height=2, bg="black").place(x=25, y=107)

        # Create and place the password entry field
        self.code = Entry(frame, width=25, fg='black', border=0, bg="white", font=('Microsoft YaHei UI Light', 11))
        self.code.place(x=30, y=150)
        self.code.insert(0, 'Password')
        self.code.bind('<FocusIn>', self.on_enter_code)
        self.code.bind('<FocusOut>', self.on_leave_code)

        Frame(frame, width=295, height=2, bg="black").place(x=25, y=177)

        self.code.bind('<KeyRelease>', self.show_password)

        # Create and place the "Sign in" button
        Button(frame, width=39, pady=7, text='Sign in', bg='#57a1f8', fg='white', border=0, command=self.signin).place(x=35, y=204)

        # Create and place the "Sign up" label and button
        label = Label(frame, text="Don't have an account?", fg='black', bg='white', font=('Microsoft YaHei UI Light', 9))
        label.place(x=75, y=270)
        sign_up = Button(frame, width=6, text='Sign up', border=0, bg='white', cursor='hand2', fg='#57a1f8', command=self.open_signup_page)
        sign_up.place(x=215, y=270)

    def on_enter_user(self, e):
        if self.user.get() == 'Username':
            self.user.delete(0, 'end')

    def on_leave_user(self, e):
        if self.user.get() == '':
            self.user.insert(0, 'Username')

    def on_enter_code(self, e):
        if self.code.get() == 'Password':
            self.code.delete(0, 'end')

    def on_leave_code(self, e):
        if self.code.get() == '':
            self.code.insert(0, 'Password')

    def show_password(self, e):
        if self.code.get() == '':
            self.code.config(show="")
        else:
            self.code.config(show="*")

    def hash_password(self, password):
        # Create a hash object
        hasher = hashlib.sha256()
        # Update the hash object with the password
        hasher.update(password.encode('utf-8'))
        # Get the hexadecimal representation of the hash
        return hasher.hexdigest()

    def signin(self):
        username = self.user.get()
        password = self.code.get()

        file = open('datasheet.txt', 'r')
        d = file.read()
        r = ast.literal_eval(d)
        file.close()
        
        if username in r.keys():
            hashed_password = self.hash_password(password)
            if hashed_password == r[username]:
                self.open_new_window()
            else:
                messagebox.showerror('Invalid', 'Invalid username or password')
        else:
            messagebox.showerror('Invalid', 'Invalid username or password')

    def open_menu_page(self):
        self.root.withdraw() 
        menu_window = Toplevel(self.root)
        menu_page = MenuPage(menu_window)

    def open_new_window(self):
        new_window = Toplevel(self.root)
        new_window.title("App")
        new_window.geometry('925x500+300+200')
        new_window.config(bg="white")
        
        img = Image.open('mindnode.jpg')
        img_display = ImageTk.PhotoImage(img)
        image_label = Label(new_window, image=img_display)
        image_label.image = img_display
        image_label.pack(pady=20)
        
        create_button = Button(new_window, text="Menu", command=self.open_menu_page,bg='#57a1f8', fg='white')
        create_button.pack(pady=10)

    def open_signup_page(self):
        signup_window = Toplevel(self.root)
        signup_page = SignupPage(signup_window)

# If this is the main file being run
if __name__ == "__main__":
    root = Tk()
    login_page = LoginPage(root)
