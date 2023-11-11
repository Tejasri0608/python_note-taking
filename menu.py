from tkinter import *
from tkinter import filedialog
from PIL import Image, ImageTk
from create import CreateNotePage
from upload import UploadPage
from notes import TakeNotesPage
from extract import PDFTextExtractor
import fitz  # PyMuPDF library

class MenuPage:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Menu")
        self.parent.geometry("925x500+300+200")
        self.parent.configure(bg="white")
        self.parent.resizable(False, False)

        # Load and display the background image
        img = Image.open('note.jpeg')
        img = img.resize((425, 425))  # Resize the image to fit the window
        self.photo = ImageTk.PhotoImage(img)
        self.image_label = Label(self.parent, image=self.photo, bg='white')
        self.image_label.place(x=50, y=50)

        self.create_menu()

        self.parent.mainloop()

    def create_menu(self):
        frame = Frame(self.parent, width=350, height=350, bg="white")
        frame.place(x=480, y=70)

        heading = Label(frame, text='Menu', fg='#57a1f8', bg='white', font=('Microsoft YaHei UI Light', 23, 'bold'))
        heading.place(x=135, y=5)

        # Create and place the "Create Note" button
        create_button = Button(frame, width=39, pady=7, text='Create Imagination', bg='#57a1f8', fg='white', border=0, command=self.create_note)
        create_button.place(x=55, y=120)

        # Create and place the "Take Notes" button
        take_notes_button = Button(frame, width=39, pady=7, text='Take Notes', bg='#57a1f8', fg='white', border=0, command=self.open_take_notes_page)
        take_notes_button.place(x=55, y=180)

        # Create and place the "Upload PDF" button
        upload_button = Button(frame, width=39, pady=7, text='Upload PDF', bg='#57a1f8', fg='white', border=0, command=self.upload_pdf)
        upload_button.place(x=55, y=240)

        # Create and place the "Extract Text" button
        extract_button = Button(frame, width=39, pady=7, text='Extract Text', bg='#57a1f8', fg='white', border=0, command=self.extract_pdf)
        extract_button.place(x=55, y=300)

    def extract_pdf(self):
        extract_window=Toplevel(self.parent)
        extract_page = PDFTextExtractor(extract_window)

    def create_note(self):
        create_window = Toplevel(self.parent)
        create_page = CreateNotePage(create_window)

    def upload_pdf(self):
        upload_window = Toplevel(self.parent)
        upload_page = UploadPage(upload_window)

    def open_take_notes_page(self):
        take_notes_window = Toplevel(self.parent)
        take_notes_page = TakeNotesPage(take_notes_window)

if __name__ == "__main__":
    root = Tk()
    menu_page = MenuPage(root)
