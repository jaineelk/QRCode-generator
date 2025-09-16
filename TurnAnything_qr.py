

import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import qrcode

# Colors
BG, FG, BTN, INP = "#0b1f3a", "#ffe066", "#3a86ff", "#7c3aed"

root = tk.Tk()
root.title("🚀 Space QR Code 🚀")
root.geometry("520x650")
root.configure(bg=BG)
tk.Label(root, text="🚀 Space QR Code Generator 🚀", font=("Comic Sans MS", 26, "bold"), fg=FG, bg=BG).pack(pady=20)
tk.Label(root, text="Type your secret message, link, phone, email, WiFi, contact, or social media below and blast off!", font=("Comic Sans MS", 14), fg="#f4faff", bg=BG, wraplength=480, justify="center").pack(pady=5)
f = tk.Frame(root, bg=INP); f.pack(pady=15, padx=30, fill="x")
tk.Label(f, text="Your Message:", font=("Comic Sans MS", 14), fg="#f4faff", bg=INP).pack(side="left", padx=10)
e = tk.Entry(f, font=("Comic Sans MS", 14), width=28, bg="#f4faff", fg=BG, relief="groove", borderwidth=3); e.pack(side="left", padx=10)
qr_label = tk.Label(root, bg=BG); qr_label.pack(pady=30)
def gen():
    d = e.get()
    if not d:
        messagebox.showerror("Oops!", "Please enter a message or link to launch your QR code."); return
    img = qrcode.make(d).resize((260, 260))
    image = ImageTk.PhotoImage(img)
    qr_label.configure(image=image)
    qr_label.image = image
tk.Button(root, text="Generate QR Code!", font=("Comic Sans MS", 18, "bold"), fg="#f4faff", bg=BTN, activebackground=INP, activeforeground=FG, command=gen, relief="raised", padx=24, pady=12, borderwidth=4).pack(pady=10)
tk.Label(root, text="Made By Jaineel Kansara", font=("Comic Sans MS", 12, "italic"), fg=FG, bg=BG).pack(side="bottom", pady=16)
root.mainloop()
