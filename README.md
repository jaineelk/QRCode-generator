
# QR Code Mini Project

This project provides two distinct features, each in its own file:



## 1️⃣ UPI Payment QR Generator (`qrCode.py`)

- **Purpose:** Generate QR codes specifically for UPI payments.
- **Features:**
  - Enter UPI ID, recipient name, amount (optional), and note (optional).
  - Generates a QR code for payment using UPI protocol.
  - Every entry is stored in a CSV file (`upi_qr_data.csv`) for record-keeping.
  - Error handling: Alerts if UPI ID or recipient name is missing.
  - Sleek, modern white theme for a professional and consistent look.
  - Instantly displays the QR code and saves it as `upi_qr.png`.
- **Use case:** For merchants, individuals, or anyone who wants to quickly create UPI payment QR codes and keep a log of transactions/requests.

---


## 2️⃣ General QR Code Generator GUI (`qr_gui.py`)

- **Purpose:** Generate QR codes for any text, link, contact, WiFi, or social media.
- **Features:**
  - Space-themed, visually appealing GUI for kids and beginners.
  - Supports text, links, phone numbers, emails, WiFi credentials, contacts, and social media.
  - Fun fonts, bright colors, and rocket/astronaut motifs.
  - Error handling: Alerts if input is empty.
  - Instantly generates and displays the QR code in the app.
  - Easy-to-use interface: Just type and click!
- **Use case:** For anyone who wants to create QR codes for sharing information, links, contacts, or WiFi credentials in a fun and engaging way.

---

## Features

### UPI Payment QR Generator
- UPI payment QR creation
- CSV storage for all generated QR/payment requests
- Simple, direct interface for payment use only

### General QR Code GUI
- Sleek, white-themed GUI for universal QR generation
- Supports text, links, phone, email, WiFi, contact, social media
- Instant QR preview
- Modern, minimal design

---

## Requirements

- Python 3.10+
- Libraries:
  - `qrcode`
  - `Pillow`
  - `tkinter` (default in Python)

Install dependencies:
```bash
pip install qrcode[pil] Pillow
```

---

## How to Run

### UPI Payment QR
```bash
python qrCode.py
```

### General QR Code GUI
```bash
python qr_gui.py
```

---

## Usage

### UPI Payment QR
1. Run `qrCode.py`.
2. Enter UPI ID, recipient name, amount, and note.
3. Get a payment QR code and store the entry in CSV.

### General QR Code GUI
1. Run `qr_gui.py`.
2. Enter any text, link, contact, WiFi, or social media info.
3. Instantly view the QR code in a clean, white-themed window.

---

## Credits

Made by Jaineel Kansara.

---

For feedback or feature requests, reach out at: jaineelnkansara@gmail.com

Install dependencies with:
```bash
pip install qrcode[pil] Pillow
```

---

## 🚦 How to Run

### 1. Run the Space GUI
```bash
python qr_gui.py
```

### 2. Run the Basic Script
```bash
python qrCode.py
```

---

## 🖥️ How to Use the GUI

1. Launch `qr_gui.py`.
2. Read the hint above the input box to know what you can generate.
3. Type your message, link, phone, email, WiFi info, contact, or social media link.
4. Click **Generate QR Code!**
5. Your QR code appears instantly—scan it with any QR code reader!

---

## 🎨 Space Theme Details

- **Background:** Deep space blue
- **Highlight Colors:** Star yellow, planet purple, rocket red
- **Fonts:** Comic Sans MS for a playful look
- **Icons:** Rocket and stars for fun
- **Layout:** Large buttons, clear labels, and easy-to-read instructions

---

## 💡 Examples

- **Text:** `Hello World!`
- **URL:** `www.linkedin.com/in/jaineel-kansara-`
- **Phone:** `+911234567890`
- **Email:** `jaineelnkansara@gmail.com`
- **WiFi:** `WIFI:S:MySSID;T:WPA;P:mypassword;;`
- **Contact (vCard):**
  ```
  BEGIN:VCARD
  VERSION:3.0
  N:Doe;John;;;
  FN:John Doe
  TEL;TYPE=CELL:1234567890
  EMAIL:jaineelnkansara@gmail.com
  END:VCARD
  ```
- **Social Media:** `https://www.instagram.com/jaineel.786?igsh=MThiNHJxZ3YyNGp3ZQ==`

---

## 🧑‍🚀 For Young Astronauts

This app is designed for kids and beginners. No coding skills needed—just imagination! Try making QR codes for:
- Secret messages
- Sharing links with friends
- WiFi passwords for guests
- Fun contact cards
- Social media profiles

---

## ❓ FAQ

**Q: What is a QR code?**
A: QR (Quick Response) code is a type of barcode that stores information like text, links, or contact details. Scan it with your phone to access the info instantly!

**Q: Can I save or share the QR code?**
A: Currently, the GUI displays the QR code. If you want a save/share feature, let us know!

**Q: Is it safe for kids?**
A: Yes! The app is simple, safe, and does not collect any data.

---

## 📝 Credits

Made with ❤️ for young astronauts and Python learners By Jaineel Kansara.

---

## 📧 Contact

For feedback or feature requests, reach out at: jaineelnkansara@gmail.com

---

Enjoy your journey through the universe of QR codes! 🚀✨
