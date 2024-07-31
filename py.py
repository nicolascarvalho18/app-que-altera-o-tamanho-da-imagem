import tkinter as tk
from tkinter import filedialog
from PIL import Image

class ImageResizerApp:
    def __init__(self, master):
        self.master = master
        master.title("Image Resizer")

        self.label = tk.Label(master, text="Resize an image")
        self.label.pack()

        self.open_button = tk.Button(master, text="Open Image", command=self.open_image)
        self.open_button.pack()

        self.width_label = tk.Label(master, text="Width:")
        self.width_label.pack()
        self.width_entry = tk.Entry(master)
        self.width_entry.pack()

        self.height_label = tk.Label(master, text="Height:")
        self.height_label.pack()
        self.height_entry = tk.Entry(master)
        self.height_entry.pack()

        self.resize_button = tk.Button(master, text="Resize Image", command=self.resize_image)
        self.resize_button.pack()

        self.image_path = None

    def open_image(self):
        self.image_path = filedialog.askopenfilename()
        if self.image_path:
            print(f"Selected image: {self.image_path}")

    def resize_image(self):
        if self.image_path:
            new_width = int(self.width_entry.get())
            new_height = int(self.height_entry.get())
            output_path = filedialog.asksaveasfilename(defaultextension=".jpg", filetypes=[("JPEG files", "*.jpg"), ("All files", "*.*")])
            if output_path:
                with Image.open(self.image_path) as img:
                    resized_img = img.resize((new_width, new_height))
                    resized_img.save(output_path)
                    print(f"Image saved to {output_path} with size {new_width}x{new_height}")

root = tk.Tk()
app = ImageResizerApp(root)
root.mainloop()
