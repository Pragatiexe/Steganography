import ttkbootstrap as ttk
from ttkbootstrap.constants import *
from tkinter import filedialog, messagebox
from steganography import encode_message, decode_message

# --- Theme Setup ---
current_theme = "darkly"

# --- Create App Window ---
app = ttk.Window(themename=current_theme)
app.title("Steganography Tool")
app.geometry("550x430")
app.resizable(False, False)

# --- Functions ---
def browse_input_image():
    file_path = filedialog.askopenfilename(title="Select Image", filetypes=[("PNG files", "*.png")])
    if file_path:
        input_path_entry.delete(0, END)
        input_path_entry.insert(0, file_path)

def save_encoded_image():
    file_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("PNG files", "*.png")])
    if file_path:
        output_path_entry.delete(0, END)
        output_path_entry.insert(0, file_path)

def encode():
    input_path = input_path_entry.get()
    secret = secret_entry.get()
    output_path = output_path_entry.get()

    if not input_path or not secret or not output_path:
        messagebox.showerror("Error", "All fields are required.")
        return

    try:
        success = encode_message(input_path, secret, output_path)
        if success:
            messagebox.showinfo("Success", "✅ Message encoded and saved successfully!")
        else:
            messagebox.showerror("Error", "Encoding failed.")
    except Exception as e:
        messagebox.showerror("Error", f"Failed: {e}")

def decode():
    file_path = filedialog.askopenfilename(title="Select Encoded Image", filetypes=[("PNG files", "*.png")])
    if not file_path:
        return
    try:
        message = decode_message(file_path)
        decoded_message_entry.delete(0, END)
        decoded_message_entry.insert(0, message)
    except Exception as e:
        messagebox.showerror("Error", f"Failed to decode: {e}")

def switch_theme():
    global current_theme
    new_theme = "cosmo" if current_theme == "darkly" else "darkly"
    current_theme = new_theme
    app.style.theme_use(new_theme)

# --- Font ---
font = ("Segoe UI", 11)

# --- GUI Layout ---

# Input Image
ttk.Label(app, text="Input Image:", font=font).pack(pady=(10, 2))
input_frame = ttk.Frame(app)
input_frame.pack()
input_path_entry = ttk.Entry(input_frame, width=50)
input_path_entry.pack(side=LEFT, padx=(0, 5))
ttk.Button(input_frame, text="Browse", bootstyle="secondary", command=browse_input_image).pack(side=LEFT)

# Secret Message
ttk.Label(app, text="Secret Message:", font=font).pack(pady=(15, 2))
secret_entry = ttk.Entry(app, width=50)
secret_entry.pack()

# Output File Name
ttk.Label(app, text="Output Image Filename:", font=font).pack(pady=(15, 2))
output_frame = ttk.Frame(app)
output_frame.pack()
output_path_entry = ttk.Entry(output_frame, width=50)
output_path_entry.pack(side=LEFT, padx=(0, 5))
ttk.Button(output_frame, text="Save As", bootstyle="secondary", command=save_encoded_image).pack(side=LEFT)

# Encode Button
ttk.Button(app, text="Encode Message", bootstyle="success", command=encode).pack(pady=(20, 10))

# Decode Section
ttk.Button(app, text="Decode Message from Image", bootstyle="info", command=decode).pack()
decoded_message_entry = ttk.Entry(app, width=50)
decoded_message_entry.pack(pady=(5, 10))

# Theme Switcher Button
ttk.Button(app, text="Toggle Theme (Light/Dark)", bootstyle="warning", command=switch_theme).pack(pady=10)

# Run App
app.mainloop()
