import tkinter as tk
from PIL import Image, ImageTk
import pyqrcode

def generate_qr(content, filename):
    url = pyqrcode.create(content)
    url.png(filename, scale=6)

def display_qr(filename):
    img = Image.open(filename)
    
    qr_window = tk.Toplevel()
    qr_window.attributes('-fullscreen', True)
    qr_window.bind('<Escape>', lambda e: qr_window.destroy())  # Press 'Escape' to exit full screen

    img = ImageTk.PhotoImage(img)
    label = tk.Label(qr_window, image=img)
    label.pack(expand=True)

    # Bind a click event to the QR code screen to close the window
    label.bind("<Button-1>", lambda e: qr_window.destroy())

    # Keep a reference to the image to avoid garbage collection
    label.image = img

def send_qr():
    filename = "send_qr.png"
    generate_qr("Send / Gửi Hàng", filename)
    display_qr(filename)

def receive_qr():
    filename = "receive_qr.png"
    generate_qr("Receive / Nhận Hàng", filename)
    display_qr(filename)

# Create the main Tkinter window
root = tk.Tk()
root.title("QR Code Generator")

# Make the main window fullscreen
root.attributes('-fullscreen', True)

# Bind the Escape key to exit fullscreen mode and close the app
root.bind('<Escape>', lambda e: root.destroy())

# Create and pack the "Send / Gửi Hàng" button
send_button = tk.Button(root, text="Send / Gửi Hàng", command=send_qr, font=("Helvetica", 16))
send_button.pack(pady=20)

# Create and pack the "Receive / Nhận Hàng" button
receive_button = tk.Button(root, text="Receive / Nhận Hàng", command=receive_qr, font=("Helvetica", 16))
receive_button.pack(pady=20)

# Run the Tkinter event loop
root.mainloop()
