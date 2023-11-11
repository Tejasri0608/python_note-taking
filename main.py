import tkinter as tk
from PIL import Image, ImageTk
from login_page import LoginPage  # Import the LoginPage class from login_page.py

def main():
    root = tk.Tk()
    root.title("Homepage")
    root.geometry("925x500+300+200")

    # Load the image using PIL
    image_path = "pythonhomepage.png"  
    image = Image.open(image_path)
    image = image.resize((850, 425))  # Resize the image to fit the window
    photo = ImageTk.PhotoImage(image)

    # Create a label to display the image
    image_label = tk.Label(root, image=photo)
    image_label.image = photo  # Keep a reference to the photo object
    image_label.pack(pady=20)

    # Create the login button
    login_button = tk.Button(root, text="Login", command=lambda: show_login_page(root), bg='#57a1f8', fg='white')
    login_button.pack()

    # Start the main event loop 
    root.mainloop()

def show_login_page(root):
    root.withdraw()  # Hide the main window
    login_window = tk.Toplevel(root)
    login_page = LoginPage(login_window)

if __name__ == "__main__":
    main()
