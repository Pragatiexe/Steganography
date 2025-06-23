🕵️‍♀️ Steganography – Hiding Information in Images
IBM Cyber Security Internship Project
Developed using Python & Tkinter with Dark/Light Theme Support


📌 Project Description
This project demonstrates Steganography – the practice of hiding secret messages within images. It uses Python and image processing to encode and decode secret text data invisibly within PNG files.


🎯 Features:

🔐 Encode a secret message inside an image

🔎 Decode the hidden message from the image

🖼️ Easy-to-use GUI with Dark/Light Theme Switcher

✅ Supports .png images

🚫 Error handling and user-friendly messages


🛠️ Technologies Used

Component   	Details
Language	    Python
GUI Library 	ttkbootstrap (Tkinter + Themes)
Image Lib	    Pillow (PIL)


🚀 How to Run
1. Install Requirements

pip install ttkbootstrap pillow

2. Run the GUI

python gui.py



🧪 How It Works

Encoding: The program modifies the least significant bit (LSB) of image pixels to store the binary form of your message.

Decoding: It reads those bits and reconstructs the original hidden message.



🧠 Learning Outcome
✔ Learned about steganography principles
✔ Gained experience in Python GUI programming
✔ Applied cyber security concepts practically
✔ Understood how data can be concealed & retrieved securely


📁 Project Structure

Steganography_ibm/
├── gui.py                  # Main GUI interface
├── steganography.py        # Encode/Decode logic
├── input_image.png         # Sample input image (optional)
└── output_image.png        # Encoded image (output)


🙋‍♀️ Developed By
Pragati Kumari
IBM Cyber Security Virtual Internship Project, 2025
