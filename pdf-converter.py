import tkinter as tk
from tkinter import filedialog
import img2pdf
import os


def convert_to_pdf(image_path, pdf_path):
    with open(pdf_path, "wb") as pdf_file:
        pdf_file.write(img2pdf.convert(image_path))


def select_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg;*.jpeg;*.png")])
    if file_path:
        image_entry.delete(0, tk.END)
        image_entry.insert(0, file_path)


def convert_image_to_pdf():
    image_path = image_entry.get()
    if image_path:
        pdf_filename = os.path.join(os.path.expanduser("~"), "Desktop", "converted_image.pdf")
        convert_to_pdf(image_path, pdf_filename)
        tk.messagebox.showinfo("Conversion Complete", "Image converted to PDF successfully!\nPDF saved on Desktop.")


root = tk.Tk()
root.title("Image to PDF Converter")

tk.Label(root, text="Image Path:").grid(row=0, column=0, padx=5, pady=5, sticky="w")
image_entry = tk.Entry(root, width=50)
image_entry.grid(row=0, column=1, padx=5, pady=5)
tk.Button(root, text="Select Image", command=select_image).grid(row=0, column=2, padx=5, pady=5)

convert_button = tk.Button(root, text="Convert to PDF", command=convert_image_to_pdf)
convert_button.grid(row=1, column=0, columnspan=3, padx=5, pady=5)

root.mainloop()
