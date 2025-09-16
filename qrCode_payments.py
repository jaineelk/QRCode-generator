
import qrcode
import tkinter as tk
from tkinter import messagebox
from PIL import ImageTk
import csv
import os

def generate_qr():
	upi_id = upi_entry.get().strip()
	amount = amount_entry.get().strip()
	note = note_entry.get().strip()
	name = name_entry.get().strip()
	if not upi_id or not name:
		messagebox.showerror("Input Error", "UPI ID and Recipient Name are required.")
		return
	url = f"upi://pay?pa={upi_id}&pn={name}"
	if amount:
		url += f"&am={amount}"
	if note:
		url += f"&tn={note}"
	qr_img = qrcode.make(url)
	# Save and display QR
	qr_img.save("upi_qr.png")
	img = qr_img.resize((200, 200))
	img_tk = ImageTk.PhotoImage(img)
	qr_label.config(image=img_tk)
	qr_label.image = img_tk

	# Store input in CSV file
	csv_file = "upi_qr_data.csv"
	file_exists = os.path.isfile(csv_file)
	with open(csv_file, mode="a", newline='', encoding="utf-8") as f:
		writer = csv.writer(f)
		if not file_exists:
			writer.writerow(["UPI ID", "Recipient Name", "Amount", "Note"])
		writer.writerow([upi_id, name, amount, note])


# Sleek white theme colors
BG = "#ffffff"  # Main background
FG = "#222222"  # Main foreground/text
BTN = "#0078d7" # Button color
INP = "#f5f5f5" # Input field background

root = tk.Tk()
root.title("UPI QR Code Generator")
root.geometry("420x480")
root.configure(bg=BG)

tk.Label(
	root,
	text="UPI Payment QR Generator",
	font=("Segoe UI", 20, "bold"),
	fg=FG,
	bg=BG
).pack(pady=(30, 10))

form = tk.Frame(root, bg=BG)
form.pack(pady=10)

def add_row(label, entry_var, row):
	tk.Label(form, text=label, font=("Segoe UI", 12), fg=FG, bg=BG, anchor="e", width=16).grid(row=row, column=0, padx=(0,8), pady=6)
	ent = tk.Entry(form, textvariable=entry_var, font=("Segoe UI", 12), width=22, bg=INP, fg=FG, relief="solid", borderwidth=1)
	ent.grid(row=row, column=1, pady=6)
	return ent

upi_var = tk.StringVar()
name_var = tk.StringVar()
amount_var = tk.StringVar()
note_var = tk.StringVar()

upi_entry = add_row("UPI ID:", upi_var, 0)
name_entry = add_row("Recipient Name:", name_var, 1)
amount_entry = add_row("Amount (optional):", amount_var, 2)
note_entry = add_row("Note (optional):", note_var, 3)

qr_label = tk.Label(root, bg=BG)
qr_label.pack(pady=18)

tk.Button(
	root,
	text="Generate QR",
	font=("Segoe UI", 14, "bold"),
	fg="#ffffff",
	bg=BTN,
	activebackground="#005fa3",
	activeforeground="#ffffff",
	command=generate_qr,
	relief="flat",
	padx=16,
	pady=7,
	borderwidth=0
).pack(pady=8)

tk.Label(
	root,
	text="Made By Jaineel Kansara",
	font=("Segoe UI", 10, "italic"),
	fg="#888888",
	bg=BG
).pack(side="bottom", pady=12)

root.mainloop()
