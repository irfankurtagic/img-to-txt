import os
import tkinter as tk
from tkinter import filedialog, messagebox
from PIL import Image
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Replace with the path to your Tesseract executable

class ImageToTextConverterApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Image to Text Converter")
        self.root.geometry("300x240")  # Set the initial size of the window

        self.file_paths = []

        # Create UI elements
        #self.label = tk.Label(root, text="Select up to 10 images:")
        #self.label.pack(pady=10)

        self.select_button = tk.Button(root, text="Select Images", command=self.select_images)
        self.select_button.pack(pady=10)

        self.convert_button = tk.Button(root, text="Convert", command=self.convert_images)
        self.convert_button.pack(pady=10)

    def select_images(self):
        self.file_paths = filedialog.askopenfilenames(
            title="Select Images",
            filetypes=(("Image files", "*.png;*.jpg;*.jpeg;*.gif;*.bmp"), ("all files", "*.*"))
        )

    def convert_images(self):
        if not self.file_paths:
            return

        all_text = ""
        for file_path in self.file_paths:
            image = Image.open(file_path)
            text = pytesseract.image_to_string(image)
            all_text += f"Text from {file_path}:\n{text}\n{'='*30}\n"

        # Save all text to a single file in the Downloads folder
        downloads_folder = os.path.join(os.path.expanduser('~'), 'Downloads')
        output_file_path = os.path.join(downloads_folder, "all_text_output.txt")

        with open(output_file_path, 'w') as text_file:
            text_file.write(all_text)

        messagebox.showinfo("Conversion Complete", f"Images converted to text successfully. Check '{output_file_path}'.")

if __name__ == "__main__":
    root = tk.Tk()
    app = ImageToTextConverterApp(root)
    root.mainloop()
