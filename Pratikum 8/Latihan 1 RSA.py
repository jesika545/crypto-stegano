import tkinter as tk
from tkinter import ttk, scrolledtext
import math


# --- Fungsi Inti RSA ---

def extended_gcd(a, b):
    """Implementasi Algoritma Euclidean Diperluas (untuk mencari d)"""
    if a == 0:
        return b, 0, 1
    gcd, x1, y1 = extended_gcd(b % a, a)
    x = y1 - (b // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(a, m):
    """Menghitung invers modular a^-1 mod m (eksponen privat d)"""
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None
    return x % m


def rsa_encrypt(message_int, e, n):
    """Fungsi Enkripsi: c = m^e mod n"""
    return pow(message_int, e, n)


def rsa_decrypt(ciphertext, d, n):
    """Fungsi Dekripsi: m = c^d mod n"""
    return pow(ciphertext, d, n)


# Fungsi untuk menghasilkan string langkah manual yang detail dan rapi
def generate_manual_steps(p, q, e, n, phi_n, d, plaintext, plaintext_ints, ciphertext_ints, decrypted_ints,
                          decrypted_text):
    output = []

    output.append("====================================================")
    output.append("📝 RINGKASAN PERHITUNGAN MANUAL RSA (Latihan 1)")
    output.append("====================================================")

    # Bagian A: Generate Kunci
    output.append("\nA. TAHAP 1: GENERATE KUNCI")
    output.append("----------------------------------------------------")

    output.append(f"Ketentuan Awal: p={p}, q={q}, e={e}")

    output.append("\n1. Hitung Modulus (n): n = p x q")
    output.append(f"   n = {p} x {q} = {n}")

    output.append("\n2. Hitung Fungsi Euler (phi(n)): phi(n) = (p-1)(q-1)")
    output.append(f"   phi(n) = ({p}-1) x ({q}-1) = 16 x 10 = {phi_n}")

    output.append(f"\n3. Verifikasi Eksponen Publik (e={e}):")
    output.append(f"   - Syarat 1: 1 < {e} < {phi_n} (OK)")
    output.append(f"   - Syarat 2: GCD({e}, {phi_n}) = 1 (OK)")

    output.append(f"\n4. Hitung Eksponen Privat (d): d * e = 1 mod phi(n)")
    output.append(f"   d * {e} = 1 mod {phi_n}")
    output.append(f"   Menggunakan Algoritma Euclidean Diperluas, ditemukan:")
    output.append(f"   d = {d}")

    output.append("\n5. Hasil Kunci:")
    output.append(f"   Kunci Publik (e, n): ({e}, {n})")
    output.append(f"   Kunci Privat (d, n): ({d}, {n})")

    # Bagian B: Enkripsi
    output.append("\n\nB. TAHAP 2: ENKRIPSI")
    output.append("----------------------------------------------------")
    output.append(f"Plaintext: {plaintext}")
    output.append(f"Formula: c = m^e mod n  =>  c = m^{e} mod {n}")

    output.append(f"\n{'Karakter':<10}{'ASCII (m)':<12}{'Ciphertext (c)':<15}")
    output.append("-" * 37)
    for char, m, c in zip(plaintext, plaintext_ints, ciphertext_ints):
        output.append(f"{char:<10}{m:<12}{c:<15}")
    output.append("-" * 37)
    output.append(f"Ciphertext Ints: {ciphertext_ints}")

    # Bagian C: Dekripsi
    output.append("\n\nC. TAHAP 3: DEKRIPSI")
    output.append("----------------------------------------------------")
    output.append(f"Formula: m = c^d mod n  =>  m = c^{d} mod {n}")

    output.append(f"\n{'Ciphertext (c)':<15}{'Plaintext (m)':<15}{'Karakter':<10}")
    output.append("-" * 40)
    for c, dm in zip(ciphertext_ints, decrypted_ints):
        output.append(f"{c:<15}{dm:<15}{chr(dm):<10}")
    output.append("-" * 40)
    output.append(f"Plaintext Hasil Dekripsi: {decrypted_text}")

    return "\n".join(output)


def run_rsa():
    """Mengambil input plaintext dan menjalankan proses RSA"""

    # Nilai Tetap (Sesuai Latihan 1)
    p = 17
    q = 11
    e = 7

    plaintext = plaintext_entry.get()

    if not plaintext:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Masukkan Plaintext terlebih dahulu.")
        return

    # --- 1. Generate Kunci ---
    n = p * q
    phi_n = (p - 1) * (q - 1)
    d = mod_inverse(e, phi_n)

    # --- 2. Konversi Plaintext ke Angka (ASCII) ---
    plaintext_ints = [ord(char) for char in plaintext]

    # --- 3. Proses Enkripsi ---
    ciphertext_ints = [rsa_encrypt(m, e, n) for m in plaintext_ints]

    # --- 4. Proses Dekripsi ---
    decrypted_ints = [rsa_decrypt(c, d, n) for c in ciphertext_ints]
    decrypted_text = "".join([chr(m) for m in decrypted_ints])

    # --- Menampilkan Output (Langkah Manual yang Rapi) ---

    manual_output = generate_manual_steps(p, q, e, n, phi_n, d, plaintext, plaintext_ints, ciphertext_ints,
                                          decrypted_ints, decrypted_text)

    # Clear dan insert output
    output_text.delete(1.0, tk.END)
    output_text.insert(tk.END, manual_output)


# --- Setup GUI ---

root = tk.Tk()
root.title("RSA Cryptography - Latihan 1 (p=17, q=11, e=7)")
root.geometry("750x650")  # Ukuran sedikit lebih besar untuk output yang panjang
root.style = ttk.Style()
root.style.theme_use('clam')

# Main Frame
main_frame = ttk.Frame(root, padding="15 15 15 15")
main_frame.pack(fill='both', expand=True)

# Input Section
input_label = ttk.Label(main_frame, text="Masukkan Plaintext:", font=('Arial', 12, 'bold'))
input_label.grid(row=0, column=0, sticky='w', pady=5)

plaintext_entry = ttk.Entry(main_frame, width=40, font=('Arial', 11))
plaintext_entry.grid(row=1, column=0, sticky='ew', padx=5, pady=5)
plaintext_entry.insert(0, "HASUGIAN")

run_button = ttk.Button(main_frame, text="Jalankan Proses RSA", command=run_rsa, style='Run.TButton')
run_button.grid(row=1, column=1, sticky='w', padx=5, pady=5)

# Separator
separator = ttk.Separator(main_frame, orient='horizontal')
separator.grid(row=2, column=0, columnspan=2, sticky='ew', pady=10)

# Output Section
output_label = ttk.Label(main_frame, text="Langkah Perhitungan Manual :", font=('Arial', 12, 'bold'))
output_label.grid(row=3, column=0, sticky='w', pady=5)

# Menggunakan ScrolledText dan font monospace (Courier New) untuk penataan tabel yang rapi
output_text = scrolledtext.ScrolledText(main_frame, width=80, height=25, font=('Courier New', 10), wrap=tk.WORD)
output_text.grid(row=4, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)

# Configure grid weight to make widgets resize appropriately
main_frame.grid_columnconfigure(0, weight=3)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(4, weight=1)

# Style Customization
root.style.configure('Run.TButton', font=('Arial', 10, 'bold'), foreground='blue')

root.mainloop()