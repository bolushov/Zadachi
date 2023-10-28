import tkinter as tk
from tkinter import ttk
from tkinter.colorchooser import askcolor

class SimplePaint:
    def __init__(self, root):
        self.root = root
        self.root.title("Простой графический редактор")
        self.pen_color = "black"
        self.fill_color = "black"
        self.brush_size = 2
        self.mode = "brush"
        self.drawing = None
        self.shapes = []

        self.canvas_frame = ttk.LabelFrame(root, text="Холст", padding=(10, 5))
        self.canvas_frame.grid(row=0, column=0, padx=10, pady=10, sticky=tk.W + tk.E + tk.N + tk.S)

        self.canvas = tk.Canvas(self.canvas_frame, bg="white", width=400, height=400)
        self.canvas.pack(padx=10, pady=10)
        self.canvas.bind("<Button-1>", self.on_canvas_click)
        self.canvas.bind("<B1-Motion>", self.on_canvas_drag)
        self.canvas.bind("<ButtonRelease-1>", self.on_canvas_release)

        self.control_frame = ttk.LabelFrame(root, text="Управление", padding=(10, 5))
        self.control_frame.grid(row=0, column=1, padx=10, pady=10, sticky=tk.N)

        brush_button = ttk.Button(self.control_frame, text="Кисть", command=lambda: self.set_mode("brush"))
        brush_button.pack(fill=tk.X, pady=5)

        square_button = ttk.Button(self.control_frame, text="Квадрат", command=lambda: self.set_mode("square"))
        square_button.pack(fill=tk.X, pady=5)

        rectangle_button = ttk.Button(self.control_frame, text="Прямоугольник", command=lambda: self.set_mode("rectangle"))
        rectangle_button.pack(fill=tk.X, pady=5)

        circle_button = ttk.Button(self.control_frame, text="Круг", command=lambda: self.set_mode("circle"))
        circle_button.pack(fill=tk.X, pady=5)

        triangle_button = ttk.Button(self.control_frame, text="Треугольник", command=lambda: self.set_mode("triangle"))
        triangle_button.pack(fill=tk.X, pady=5)

        clear_button = ttk.Button(self.control_frame, text="Очистить", command=self.clear_canvas)
        clear_button.pack(fill=tk.X, pady=5)

        color_button = ttk.Button(self.control_frame, text="Выбрать цвет", command=self.change_color)
        color_button.pack(fill=tk.X, pady=5)

        self.root.grid_rowconfigure(0, weight=1)
        self.root.grid_columnconfigure(0, weight=1)

        self.prev_x = None
        self.prev_y = None

    def set_mode(self, mode):
        self.mode = mode

    def on_canvas_click(self, event):
        self.prev_x = event.x
        self.prev_y = event.y

    def on_canvas_drag(self, event):
        x, y = event.x, event.y
        if self.mode == "brush":
            if self.prev_x and self.prev_y:
                self.canvas.create_line(self.prev_x, self.prev_y, x, y, fill=self.pen_color, width=self.brush_size)
                self.prev_x = x
                self.prev_y = y
        elif self.mode in ["square", "rectangle", "circle", "triangle"]:
            self.preview_shape(x, y)

    def on_canvas_release(self, event):
        if self.mode in ["square", "rectangle", "circle", "triangle"] and self.drawing:
            self.finalize_shape(event.x, event.y)

    def preview_shape(self, x, y):
        if self.drawing:
            self.canvas.delete(self.drawing)
        if self.mode == "square":
            side = max(abs(x - self.prev_x), abs(y - self.prev_y))
            if x < self.prev_x:
                side = -side
            if y < self.prev_y:
                self.drawing = self.canvas.create_rectangle(self.prev_x, self.prev_y-side, self.prev_x-side, self.prev_y, outline=self.pen_color, fill=self.fill_color)
            else:
                self.drawing = self.canvas.create_rectangle(self.prev_x, self.prev_y, self.prev_x+side, self.prev_y+side, outline=self.pen_color, fill=self.fill_color)

        elif self.mode == "rectangle":
            self.drawing = self.canvas.create_rectangle(self.prev_x, self.prev_y, x, y, outline=self.pen_color, fill=self.fill_color)
        elif self.mode == "circle":
            r = ((x - self.prev_x) ** 2 + (y - self.prev_y) ** 2) ** 0.5
            self.drawing = self.canvas.create_oval(self.prev_x - r, self.prev_y - r, self.prev_x + r, self.prev_y + r, outline=self.pen_color, fill=self.fill_color)
        elif self.mode == "triangle":
            self.draw_triangle(x, y)

    def draw_triangle(self, x, y):
        if self.drawing:
            self.canvas.delete(self.drawing)
        middle_x = (self.prev_x + x) / 2
        self.drawing = self.canvas.create_polygon(
            self.prev_x, self.prev_y,
            middle_x, y,
            x, self.prev_y,
            outline=self.pen_color,
            fill=self.fill_color
        )

    def finalize_shape(self, x, y):
        self.preview_shape(x, y)
        self.shapes.append(self.drawing)
        self.drawing = None

    def clear_canvas(self):
        self.canvas.delete("all")
        self.shapes = []

    def change_color(self):
        color = askcolor(color=self.pen_color)[1]
        if color:
            self.pen_color = color
            self.fill_color = color

def main():
    root = tk.Tk()
    app = SimplePaint(root)
    root.mainloop()

if __name__ == "__main__":
    main()
