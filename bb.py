import tkinter as tk

class ShapeDrawer:
    def __init__(self, root):
        self.root = root
        self.root.title("Shape Drawer")

        self.canvas = tk.Canvas(self.root, width=400, height=400)
        self.canvas.pack()

        self.shape_choice = tk.StringVar()
        self.shape_choice.set("Rectangle")

        self.create_buttons()
        self.canvas.bind("<Button-1>", self.start_drawing)
        self.canvas.bind("<B1-Motion>", self.update_drawing)
        self.canvas.bind("<ButtonRelease-1>", self.finish_drawing)

        self.start_x = None
        self.start_y = None
        self.current_shape = None

    def create_buttons(self):
        shape_label = tk.Label(self.root, text="Choose a shape:")
        shape_label.pack()

        shape_options = ["Rectangle", "Oval", "Line"]
        for option in shape_options:
            shape_button = tk.Radiobutton(self.root, text=option, variable=self.shape_choice, value=option)
            shape_button.pack()

    def start_drawing(self, event):
        self.start_x = event.x
        self.start_y = event.y
        self.current_shape = None

    def update_drawing(self, event):
        if self.current_shape:
            self.canvas.delete(self.current_shape)

        shape = self.shape_choice.get()
        if shape == "Rectangle":
            self.current_shape = self.canvas.create_rectangle(self.start_x, self.start_y, event.x, event.y, outline="black")
        elif shape == "Oval":
            self.current_shape = self.canvas.create_oval(self.start_x, self.start_y, event.x, event.y, outline="black")
        elif shape == "Line":
            self.current_shape = self.canvas.create_line(self.start_x, self.start_y, event.x, event.y, fill="black")

    def finish_drawing(self, event):
        self.start_x = None
        self.start_y = None
        self.current_shape = None

if __name__ == "__main__":
    root = tk.Tk()
    app = ShapeDrawer(root)
    root.mainloop()
