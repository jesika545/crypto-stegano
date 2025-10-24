import tkinter as tk
from tkinter import ttk, messagebox

# Fungsi konversi utama
def convert_number():
    try:
        base_from = base_from_var.get()
        base_to = base_to_var.get()
        number = entry_number.get().strip()

        if not number:
            messagebox.showwarning("Peringatan", "Masukkan angka terlebih dahulu!")
            return

        # Konversi ke desimal dulu
        if base_from == "Desimal":
            decimal_value = int(number)
        elif base_from == "Biner":
            decimal_value = int(number, 2)
        elif base_from == "Oktal":
            decimal_value = int(number, 8)
        elif base_from == "Hexa":
            decimal_value = int(number, 16)

        # Konversi dari desimal ke basis target
        if base_to == "Desimal":
            result = str(decimal_value)
        elif base_to == "Biner":
            result = bin(decimal_value)[2:]
        elif base_to == "Oktal":
            result = oct(decimal_value)[2:]
        elif base_to == "Hexa":
            result = hex(decimal_value)[2:].upper()

        result_label.config(text=f"Hasil: {result}")
        global last_process
        last_process = f"{number} ({base_from}) -> {result} ({base_to})"

    except ValueError:
        messagebox.showerror("Error", "Angka yang dimasukkan tidak valid!")

# Fungsi menampilkan proses di belakang layar
def show_process():
    if last_process:
        messagebox.showinfo("Proses Konversi", last_process)
    else:
        messagebox.showinfo("Proses Konversi", "Belum ada konversi yang dilakukan.")

# === UI ===
root = tk.Tk()
root.title("Kalkulator Konversi Bilangan")
root.geometry("500x400")
root.config(bg="#e8f0fe")

title_label = tk.Label(
    root,
    text="🔢 Kalkulator Konversi Bilangan 🔢",
    font=("Segoe UI", 16, "bold"),
    bg="#e8f0fe",
    fg="#1a237e"
)
title_label.pack(pady=15)

# Frame utama
main_frame = ttk.Frame(root, padding=20)
main_frame.pack(fill="both", expand=True)

# Input angka
ttk.Label(main_frame, text="Masukkan Angka:").grid(row=0, column=0, sticky="w")
entry_number = ttk.Entry(main_frame, font=("Segoe UI", 12))
entry_number.grid(row=0, column=1, padx=10, pady=5)

# Pilihan basis
bases = ["Desimal", "Biner", "Oktal", "Hexa"]
base_from_var = tk.StringVar(value="Desimal")
base_to_var = tk.StringVar(value="Biner")

ttk.Label(main_frame, text="Dari Basis:").grid(row=1, column=0, sticky="w", pady=5)
ttk.OptionMenu(main_frame, base_from_var, *bases).grid(row=1, column=1, sticky="ew", padx=10)

ttk.Label(main_frame, text="Ke Basis:").grid(row=2, column=0, sticky="w", pady=5)
ttk.OptionMenu(main_frame, base_to_var, *bases).grid(row=2, column=1, sticky="ew", padx=10)

# Tombol konversi
convert_button = ttk.Button(main_frame, text="Hitung", command=convert_number)
convert_button.grid(row=3, column=0, columnspan=2, pady=15)

# Hasil
result_label = tk.Label(root, text="Hasil: ", font=("Consolas", 14, "bold"), bg="#e8f0fe", fg="#0d47a1")
result_label.pack(pady=10)

# Tombol lihat proses
see_process_button = ttk.Button(root, text="Lihat Proses di Balik Layar", command=show_process)
see_process_button.pack(pady=10)

# Variabel global
last_process = ""

# Gaya modern
style = ttk.Style()
style.theme_use("clam")
style.configure("TButton", font=("Segoe UI", 11), padding=6)
style.configure("TLabel", font=("Segoe UI", 11))
style.configure("TEntry", font=("Segoe UI", 11))

root.mainloop()
