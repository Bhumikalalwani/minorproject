import tkinter as tk
from tkinter import colorchooser

class WhiteboardApp(tk.Tk):
    def __init__(self):
        super().__init__()

        # Window properties
        self.title("Whiteboard & Video Call Interface")
        self.geometry("1200x700")
        self.resizable(True, True)  # Allow resizing

        # Frame for Whiteboard (left side)
        self.whiteboard_frame = tk.Frame(self, bg="white", width=600, height=700, relief="sunken", bd=3)
        self.whiteboard_frame.grid(row=0, column=0, sticky="nsew")

        # Frame for Video Call and color palette (right side)
        self.video_call_frame = tk.Frame(self, bg="black", width=600, height=700, relief="sunken", bd=3)
        self.video_call_frame.grid(row=0, column=1, sticky="nsew")

        # Split screen layout control
        self.grid_columnconfigure(0, weight=1)
        self.grid_columnconfigure(1, weight=1)
        self.grid_rowconfigure(0, weight=1)

        # Whiteboard functionality
        self.whiteboard_canvas = tk.Canvas(self.whiteboard_frame, bg="white", cursor="cross")
        self.whiteboard_canvas.pack(fill=tk.BOTH, expand=True)
        self.whiteboard_canvas.bind("<B1-Motion>", self.paint)

        # Color palette button
        self.color_btn = tk.Button(self.whiteboard_frame, text="🎨", command=self.choose_color)

        self.color_btn.pack(side=tk.BOTTOM, pady=10)

        # Eraser button
        self.eraser_btn = tk.Button(self.whiteboard_frame, text="🩹", command=self.use_eraser)
        self.eraser_btn.pack(side=tk.BOTTOM, pady=10)

        #save file button 
        #self.save_btn = tk.Button(self.whiteboard_frame, text="💾", command=self.save_file)
        

        # Clear canvas button
        self.clear_btn = tk.Button(self.whiteboard_frame, text="Clear Board", command=self.clear_canvas)
        self.clear_btn.pack(side=tk.BOTTOM, pady=10)

        # Color palette for quick selection (transparent background at the bottom center of the video call frame)
        self.create_color_palette()

        # Pen and eraser icons at the top center of the video call frame
        self.create_tools_bar()

        # Color attributes
        self.brush_color = "black"
        self.eraser_on = False

        # Window minimize, maximize, close buttons
        self.minimize_btn = tk.Button(self, text="➖", command=self.iconify)
        self.minimize_btn.place(x=10, y=10)

        self.maximize_btn = tk.Button(self, text="🔳", command=self.toggle_maximize)
        self.maximize_btn.place(x=35, y=10)

        self.close_btn = tk.Button(self, text="❌", command=self.destroy)
        self.close_btn.place(x=60, y=10)

    def toggle_maximize(self):
        self.state("zoomed" if self.state() == "normal" else "normal")

    def choose_color(self):
        # Open color picker dialog
        color = colorchooser.askcolor()[1]
        if color:
            self.brush_color = color
            self.eraser_on = False

    def use_eraser(self):
        # Use white color for eraser
        self.brush_color = "white"
        self.eraser_on = True

    def clear_canvas(self):
        # Clear the whiteboard
        self.whiteboard_canvas.delete("all")

    def paint(self, event):
        x1, y1 = (event.x - 1), (event.y - 1)
        x2, y2 = (event.x + 1), (event.y + 1)
        self.whiteboard_canvas.create_oval(x1, y1, x2, y2, fill=self.brush_color, outline=self.brush_color, width=5)

    def create_color_palette(self):
        # Create a transparent color palette at the bottom of the video call frame
        colors = ["black", "red", "green", "blue", "yellow", "purple", "orange", "pink"]
        palette_frame = tk.Frame(self.video_call_frame, bg="black", height=50)
        palette_frame.pack(side=tk.BOTTOM, pady=10)

        palette_canvas = tk.Canvas(palette_frame, bg="black", highlightthickness=0)
        palette_canvas.pack(fill=tk.BOTH, expand=True)

        for i, color in enumerate(colors):
            palette_canvas.create_rectangle(80*i+10, 10, 80*i+70, 40, fill=color, outline=color, tags=color)
            palette_canvas.tag_bind(color, "<Button-1>", lambda event, c=color: self.set_color(c))

    def set_color(self, color):
        self.brush_color = color
        self.eraser_on = False

    def create_tools_bar(self):
        # Create a pen and eraser symbol at the top center of the video call frame
        tools_frame = tk.Frame(self.video_call_frame, bg="black", height=50)
        tools_frame.pack(side=tk.TOP, pady=10)

        tools_canvas = tk.Canvas(tools_frame, bg="black", highlightthickness=0)
        tools_canvas.pack()

        # Pen symbol (circle)
        tools_canvas.create_oval(150, 10, 180, 40, fill="pink", outline="white", tags="pen")
        tools_canvas.create_text(165, 25, text="✏️", tags="pen_label", font=("Arial", 8))
        tools_canvas.tag_bind("pen", "<Button-1>", lambda event: self.use_pen())


        # Eraser symbol (rectangle)
        tools_canvas.create_rectangle(220, 10, 260, 40, fill="pink", outline="black", tags="eraser")
        tools_canvas.create_text(240, 25, text="🩹", tags="eraser_label", font=("Arial", 8))
        tools_canvas.tag_bind("eraser", "<Button-1>", lambda event: self.use_eraser())
       
        
        

    def use_pen(self):
        self.brush_color = "black"
        self.eraser_on = False

if __name__ == "__main__":
    app = WhiteboardApp()
    app.mainloop()
