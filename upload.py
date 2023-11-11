

from tkinter import *
from tkinter import filedialog
import fitz  # PyMuPDF library
from PIL import Image, ImageTk

class UploadPage:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Upload PDF')
        self.parent.geometry('925x500+300+200')
        self.parent.configure(bg="#fff")

        self.create_background()

        self.pdf_file_path = ""
        self.pil_image = None

        self.create_upload_form()

    def create_background(self):
        img = Image.open('background.jpeg')
        img = img.resize((925, 500))
        self.background_photo = ImageTk.PhotoImage(img)
        self.background_label = Label(self.parent, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_upload_form(self):
        upload_label = Label(self.parent, text="Upload a PDF File", font=("Helvetica", 16), bg="#fff")
        upload_label.pack(pady=80)

        upload_button = Button(self.parent, text="Browse PDF", command=self.upload_pdf)
        upload_button.pack(pady=10)

        show_pdf_button = Button(self.parent, text="Show PDF", command=self.show_pdf)
        show_pdf_button.pack(pady=10)

        back_to_menu_button = Button(self.parent, text="Back to Menu", command=self.back_to_menu)
        back_to_menu_button.pack(pady=10)

    def back_to_menu(self):
        self.parent.destroy()

    def upload_pdf(self):
        self.pdf_file_path = filedialog.askopenfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if self.pdf_file_path:
            print("PDF Uploaded:", self.pdf_file_path)


    def show_pdf(self):
        if self.pdf_file_path:
            pdf_window = Toplevel(self.parent)
            pdf_window.title("Uploaded PDF")
            pdf_window.geometry("925x500+300+200")

            pdf_document = fitz.open(self.pdf_file_path)

            def show_page(page_num):
                page = pdf_document[page_num]
                zoom_matrix = fitz.Matrix(2, 2)
                pixmap = page.get_pixmap(matrix=zoom_matrix)
                self.pil_image = Image.frombytes("RGB", [pixmap.width, pixmap.height], pixmap.samples)
                self.pil_image.thumbnail((925, 500))
                pil_image_tk = ImageTk.PhotoImage(self.pil_image)
                pdf_label.config(image=pil_image_tk)
                pdf_label.image = pil_image_tk

            pdf_label = Label(pdf_window)
            pdf_label.pack(fill=BOTH, expand=True)

            show_page(0)

            pdf_document.close()

            

if __name__ == "__main__":
    root = Tk()
    upload_page = UploadPage(root)
    root.mainloop()
