from PIL import Image, ImageTk
import fitz
import tkinter as tk
from tkinter import simpledialog, Toplevel, Label, BOTH, filedialog

class PDFTextExtractor:
    def __init__(self,parent):
        self.pdf_file_path = None
        self.page_number = None
        self.extracted_text = None

        self.parent = parent
        self.parent.title("PDF Text Extractor")
        self.parent.geometry("925x500+300+200")
        self.create_background()

        self.create_ui()

    def create_ui(self):
        pdf_file_button = tk.Button(self.parent, text="Select PDF File", command=self.get_pdf_file)
        pdf_file_button.pack()

        back_to_menu_button = tk.Button(self.parent, text="Back to Menu", command=self.back_to_menu)
        back_to_menu_button.pack(pady=10)

    def back_to_menu(self):
        self.parent.destroy()
        
    def create_background(self):
        img = Image.open('background.jpeg')
        img = img.resize((925, 500))
        self.background_photo = ImageTk.PhotoImage(img)
        self.background_label = Label(self.parent, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def get_pdf_file(self):
        self.pdf_file_path = filedialog.askopenfilename(filetypes=[("PDF files", "*.pdf")])
        if self.pdf_file_path:
            self.get_page_number()

    def get_page_number(self):
        self.page_number = simpledialog.askinteger("Page Number", "Enter a page number to extract text from:")
        if self.page_number:
            self.extract_text()

    def extract_text(self):
        if self.pdf_file_path and self.page_number:
            pdf_document = fitz.open(self.pdf_file_path)

            if 1 <= self.page_number <= pdf_document.page_count:
                page = pdf_document[self.page_number - 1]
                self.extracted_text = page.get_text()
            else:
                self.extracted_text = "Invalid page number."

            pdf_document.close()

            self.show_extracted_text()

    def show_extracted_text(self):
        text_window = Toplevel(self.parent)
        text_window.title("Extracted Text")
        text_window.geometry("925x500+300+200")

        text_label = Label(text_window, text=self.extracted_text, justify="left", anchor="w", wraplength=750)
        text_label.pack(fill=BOTH, expand=True)

    def run(self):
        self.parent.mainloop()

if __name__ == "__main__":
    extractor = PDFTextExtractor()
    extractor.run()
