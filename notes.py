
from tkinter import *
from tkinter import filedialog
from tkinter import colorchooser
from tkinter import messagebox
from fpdf import FPDF
from PIL import Image, ImageTk

class TakeNotesPage:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title("Take Notes")
        self.parent.geometry("925x500+300+200")  # Changed root geometry
        self.parent.configure(bg="white")
        self.parent.resizable(False, False)

        self.create_background()

        self.text_color = "black"  # Default text color
        self.color_dialog = None  # Store the color chooser dialog

        self.create_notes_form()

        self.parent.mainloop()
    
    def create_background(self):
        img = Image.open('background.jpeg')
        img = img.resize((925, 500))
        self.background_photo = ImageTk.PhotoImage(img)
        self.background_label = Label(self.parent, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def create_notes_form(self):
        self.text_input = Text(self.parent, wrap=WORD, height=15, font=("Helvetica", 12))
        self.text_input.pack(pady=20, padx=20)

        color_button = Button(self.parent, text="Text Color", command=self.change_text_color)
        color_button.pack(pady=5)

        save_button = Button(self.parent, text="Save as PDF", command=self.save_as_pdf)
        save_button.pack(pady=10)

        # Back to Menu Button
        back_to_menu_button = Button(self.parent, text="Back to Menu", command=self.back_to_menu)
        back_to_menu_button.pack(pady=10)

        self.text_input.bind("<Key>", self.on_key_press)  # Bind key event

        self.text_input.focus_set()

    def back_to_menu(self):
        self.parent.destroy()  # Close the current window

    def change_text_color(self):
        if self.color_dialog is None or not self.color_dialog.winfo_exists():
            color = colorchooser.askcolor(color=self.text_color)[1]
            if color:
                self.text_color = color
                self.text_input.tag_configure("color_tag", foreground=self.text_color)

    def on_key_press(self, event):
        self.text_input.tag_add("color_tag", "insert -1c", INSERT)
        self.text_input.tag_config("color_tag", foreground=self.text_color)

    def save_as_pdf(self):
        file_path = filedialog.asksaveasfilename(defaultextension=".pdf", filetypes=[("PDF Files", "*.pdf")])
        if file_path:
            pdf = FPDF()
            pdf.add_page()
            pdf.set_font("Arial", size=12)
            
            text = self.text_input.get("1.0", "end-1c")
            pdf.set_text_color(0, 0, 0)  # Reset text color before setting
            pdf.multi_cell(190, 10, txt=text, border=0, align='L')
            
            pdf.output(file_path)
            messagebox.showinfo("Success", "Notes saved as PDF")

# If this is the main file being run
if __name__ == "__main__":
    root = Tk()
    notes_page = TakeNotesPage(root)
