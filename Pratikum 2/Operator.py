import tkinter as tk
from tkinter import messagebox

# Fungsi untuk menghitung hasil ekspresi
def hitung():
    ekspresi = entry.get()  # Ambil teks dari input
    try:
        # Hapus spasi agar bisa juga input dengan spasi
        ekspresi_bersih = ekspresi.replace(" ", "")
        hasil = eval(ekspresi_bersih)
        label_hasil.config(text=f"Hasil: {hasil}")
    except Exception:
        messagebox.showerror("Error", "Ekspresi tidak valid! Gunakan angka dan operator aritmatika yang benar.")

# Fungsi untuk menghapus input
def hapus():
    entry.delete(0, tk.END)
    label_hasil.config(text="Hasil: -")

# Membuat jendela utama
root = tk.Tk()
root.title("Kalkulator Hybrid - Jesika")
root.geometry("400x250")
root.config(bg="#F5F5F5")

# Judul
judul = tk.Label(root, text="🧮 Kalkulator Hybrid", font=("Poppins", 16, "bold"), bg="#F5F5F5", fg="#2E2E2E")
judul.pack(pady=10)

# Input ekspresi
entry = tk.Entry(root, width=30, font=("Poppins", 12), justify="center")
entry.pack(pady=5)

# Tombol Hitung dan Hapus
frame_tombol = tk.Frame(root, bg="#F5F5F5")
frame_tombol.pack(pady=10)

btn_hitung = tk.Button(frame_tombol, text="Hitung", font=("Poppins", 11, "bold"), bg="#4CAF50", fg="white", width=10, command=hitung)
btn_hitung.grid(row=0, column=0, padx=5)

btn_hapus = tk.Button(frame_tombol, text="Hapus", font=("Poppins", 11, "bold"), bg="#E53935", fg="white", width=10, command=hapus)
btn_hapus.grid(row=0, column=1, padx=5)

# Label hasil
label_hasil = tk.Label(root, text="Hasil: -", font=("Poppins", 13, "bold"), bg="#F5F5F5", fg="#333")
label_hasil.pack(pady=15)

# Jalankan aplikasi
root.mainloop()
