from tkinter import *
import tkinter.ttk as ttk
from tkinter import colorchooser
from tkinter import filedialog
from tkinter import messagebox
from PIL import Image, ImageTk
from PIL import Image, ImageGrab
import fitz
import os

class CreateNotePage:
    def __init__(self, parent):
        self.parent = parent
        self.parent.title('Create Notes')

        self.canvas_width = 700
        self.canvas_height = 500
        self.bg_color = "white"  # default canvas background color

        # Set the root window's geometry to match the canvas size
        self.parent.geometry('925x500+300+200')

        self.brush_color = "black"  # default brush color
        self.brush_type = "round"  # default brush shape
        self.png_file_path = ""  # Global variable to store the PNG file path

        self.shape_choice = StringVar()
        self.shape_choice.set("Rectangle")

        self.create_background()
        

        self.create_note_form()

        self.parent.mainloop()
    
    def create_background(self):
        img = Image.open('background.jpeg')
        img = img.resize((925, 500))  # Resize the image to fit the window
        self.background_photo = ImageTk.PhotoImage(img)
        self.background_label = Label(self.parent, image=self.background_photo)
        self.background_label.place(x=0, y=0, relwidth=1, relheight=1)

    def paint(self, e):
        brush_width = '%0.0f' % float(self.my_slider.get())
        x1 = e.x - 1
        y1 = e.y - 1
        x2 = e.x + 1
        y2 = e.y + 1
        self.my_canvas.create_line(x1, y1, x2, y2, fill=self.brush_color, width=brush_width, capstyle=self.brush_type, smooth=True)

    def change_brush_size(self, thing):
        self.slider_label.config(text='%0.0f' % float(self.my_slider.get()))

    def change_brush_color(self):
        self.brush_color = colorchooser.askcolor(color=self.brush_color)[1]

    def change_canvas_color(self):
        bg_color = colorchooser.askcolor(color=self.bg_color)[1]
        self.bg_color = bg_color
        self.my_canvas.config(bg=self.bg_color)

    def clear_screen(self):
        self.my_canvas.delete(ALL)
        self.my_canvas.config(bg=self.bg_color)

    def save_as_png(self):
        self.png_file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG Files", "*.png")])
        if self.png_file_path:
            self.my_canvas.update()
            x = self.parent.winfo_rootx() + self.my_canvas.winfo_x()
            y = self.parent.winfo_rooty() + self.my_canvas.winfo_y()
            x1 = x + self.my_canvas.winfo_width()
            y1 = y + self.my_canvas.winfo_height()
            ImageGrab.grab(bbox=(x+80, y+60, x1+240, y1+170)).save(self.png_file_path)
            print("Canvas saved as PNG")

            # Display a popup message
            messagebox.showinfo("Success", "Canvas saved as PNG")

    def save_as_jpg(self):
        self.png_file_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPG Files", "*.jpg")])
        if self.png_file_path:
            self.my_canvas.update()
            x = self.parent.winfo_rootx() + self.my_canvas.winfo_x()
            y = self.parent.winfo_rooty() + self.my_canvas.winfo_y()
            x1 = x + self.my_canvas.winfo_width()
            y1 = y + self.my_canvas.winfo_height()
            ImageGrab.grab(bbox=(x+80, y+60, x1+240, y1+170)).save(self.png_file_path)
            print("Canvas saved as JPG")

            # Display a popup message
            messagebox.showinfo("Success", "Canvas saved as JPG")

    
    

    def create_note_form(self):
        # Create Canvas
        self.my_canvas = Canvas(self.parent, width=self.canvas_width, height=self.canvas_height, bg=self.bg_color)
        self.my_canvas.pack(side=LEFT, padx=20)
        self.my_canvas.bind('<B1-Motion>', self.paint)


        # Brush Size
        brush_size_frame = Frame(self.parent)
        brush_size_frame.pack()

        self.my_slider = ttk.Scale(brush_size_frame, from_=1, to=min(self.canvas_width, self.canvas_height),
                                  orient=HORIZONTAL, value=10, command=self.change_brush_size)
        self.my_slider.pack(side=LEFT, padx=5)
        self.slider_label = Label(brush_size_frame, text=self.my_slider.get())
        self.slider_label.pack(side=LEFT, padx=5)

        # Color Wheel
        color_button = Button(self.parent, text="Select Brush Color", command=self.change_brush_color)
        color_button.pack(pady=10)

        # Canvas Color
        canvas_color_button = Button(self.parent, text="Change Canvas Color", command=self.change_canvas_color)
        canvas_color_button.pack(pady=10)

        # Brush Shape
        brush_shape_frame = Frame(self.parent)
        brush_shape_frame.pack()

        self.brush_type_label = Label(brush_shape_frame, text="Brush Shape:")
        self.brush_type_label.pack(side=LEFT, padx=5)

        self.brush_type_var = StringVar()
        self.brush_type_var.set(self.brush_type)

        brush_shape_radio1 = Radiobutton(brush_shape_frame, text="Round", variable=self.brush_type_var, value="round", command=self.update_brush_shape)
        brush_shape_radio2 = Radiobutton(brush_shape_frame, text="Square", variable=self.brush_type_var, value="butt", command=self.update_brush_shape)
        brush_shape_radio3 = Radiobutton(brush_shape_frame, text="Diamond", variable=self.brush_type_var, value="projecting", command=self.update_brush_shape)

        brush_shape_radio1.pack(anchor=W)
        brush_shape_radio2.pack(anchor=W)
        brush_shape_radio3.pack(anchor=W)

        
        

        

        
        # Clear Screen
        clear_button = Button(self.parent, text="Clear Screen", command=self.clear_screen)
        clear_button.pack(pady=10)

        # Save as PNG Button
        save_pdf_button = Button(self.parent, text="Save as PNG", command=self.save_as_png)
        save_pdf_button.pack(pady=10)

        # Save as JPG Button
        save_jpg_button = Button(self.parent, text="Save as JPG", command=self.save_as_jpg)
        save_jpg_button.pack(pady=10)

        # Back to Menu Button
        back_to_menu_button = Button(self.parent, text="Back to Menu", command=self.back_to_menu)
        back_to_menu_button.pack(pady=10)

   

    def update_brush_shape(self):
        self.brush_type = self.brush_type_var.get()

    def back_to_menu(self):
        self.parent.destroy()  # Close the current window

if __name__ == "__main__":
    root = Tk()
    create_page = CreateNotePage(root)
    root.mainloop()

