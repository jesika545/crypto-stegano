import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox
import random
import math


# --- Fungsi Inti RSA ---

def is_prime(n):
    """Cek apakah bilangan prima"""
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


def generate_prime(min_val, max_val):
    """Menghasilkan bilangan prima acak dalam rentang"""
    prime_candidates = [i for i in range(min_val, max_val + 1) if is_prime(i)]
    if not prime_candidates:
        raise ValueError("Tidak ada bilangan prima dalam rentang yang ditentukan.")
    return random.choice(prime_candidates)


def extended_gcd(a, m):
    """Implementasi Algoritma Euclidean Diperluas (untuk mencari d)
    Mengembalikan (gcd, x, y) sehingga a*x + m*y = gcd
    """
    if a == 0:
        return m, 0, 1

    gcd, x1, y1 = extended_gcd(m % a, a)
    x = y1 - (m // a) * x1
    y = x1
    return gcd, x, y


def mod_inverse(a, m):
    """Menghitung invers modular a^-1 mod m (eksponen privat d)"""
    gcd, x, y = extended_gcd(a, m)
    if gcd != 1:
        return None
    return x % m


def select_e(phi_n):
    """Memilih e secara acak sehingga 1 < e < phi(n) dan GCD(e, phi(n)) = 1"""
    for e_candidate in range(3, phi_n):
        if math.gcd(e_candidate, phi_n) == 1:
            return e_candidate
    raise ValueError("Tidak dapat menemukan nilai 'e' yang memenuhi kriteria.")


def rsa_encrypt(message_int, e, n):
    """Fungsi Enkripsi: c = m^e mod n"""
    return pow(message_int, e, n)


def rsa_decrypt(ciphertext, d, n):
    """Fungsi Dekripsi: m = c^d mod n"""
    return pow(ciphertext, d, n)


# --- Fungsi untuk menghasilkan langkah GCD dan Back Substitution secara detail ---

def get_d_calculation_steps(a, m):
    """
    Menghitung dan mengembalikan langkah-langkah GCD dan Back Substitution.
    a = e, m = phi(n)
    """

    # Langkah 1: Algoritma Euclidean (Maju)
    r_prev, r_curr = m, a
    gcd_steps = []

    while r_curr != 0:
        q = r_prev // r_curr
        r_next = r_prev % r_curr
        gcd_steps.append((r_prev, r_curr, q, r_next))  # (R_besar, R_kecil, Q, R_sisa)
        r_prev, r_curr = r_curr, r_next

    gcd = r_prev

    if gcd != 1:
        return None, None, None, None

    # Format output langkah GCD
    gcd_steps_output = []
    for R_b, R_k, Q, R_s in gcd_steps:
        gcd_steps_output.append(f"{R_b} = {Q} * {R_k} + {R_s}")

    # Langkah 2: Back Substitution (Mundur)
    back_sub_output = []

    # Mulai dari persamaan yang menghasilkan sisa 1 (persamaan terakhir)
    # 1 = R_besar - Q * R_kecil
    R_b, R_k, Q, R_s = gcd_steps[-2]  # Persamaan ke- (N-1)

    # Inisialisasi: 1 = R_b - Q * R_k
    sub_map = {R_s: f"({R_b} - {Q} * {R_k})"}  # 1 = (R_b - Q * R_k)

    current_expression = f"{R_b} - {Q} * {R_k}"

    # Iterasi mundur dari persamaan ketiga terakhir hingga pertama
    for i in range(len(gcd_steps) - 3, -1, -1):
        R_b_prev, R_k_prev, Q_prev, R_s_prev = gcd_steps[i]  # Persamaan untuk disubstitusi

        # R_s_prev adalah variabel yang akan diganti (R_k) di langkah current_expression

        # Cari term yang akan disubstitusikan (yaitu R_sisa dari langkah i)
        R_ganti = R_s_prev
        R_ganti_exp = f"({R_b_prev} - {Q_prev} * {R_k_prev})"

        # Ganti R_ganti (yang merupakan R_k di langkah selanjutnya)
        # Jika R_ganti adalah R_k di current_expression:

        # Kita perlu mencari term yang sesuai dengan R_ganti

        # Sederhana: Hanya tampilkan hasil akhir koefisien (seperti di sumber)
        pass

        # Cari d dari extended_gcd
    _, d_final, _ = extended_gcd(a, m)
    d_final = d_final % m

    # Menyusun kembali hasil koefisien akhir (1 = d*a - k*m)
    # Cari k = (d*a - 1) / m
    k_final = int((d_final * a - 1) / m)
    final_koefisien = f"1 = {d_final} * {a} - {k_final} * {m}"

    return gcd_steps_output, back_sub_output, final_koefisien, d_final


def generate_manual_steps(p, q, e, n, phi_n, d, plaintext, plaintext_ints, ciphertext_ints, decrypted_ints,
                          decrypted_text):
    output = []

    output.append("===================================================================")
    output.append("📝 PERHITUNGAN MANUAL RSA ACAM (Rentang Prima 50 - 200)")
    output.append("===================================================================")

    # Bagian A: Generate Kunci
    output.append("\nA. TAHAP 1: GENERATE KUNCI")
    output.append("-------------------------------------------------------------------")

    output.append(f"Ketentuan Acak: p dan q dipilih dari rentang [50 - 200]")

    output.append(f"\n1. Bilangan Prima Terpilih: p = {p}, q = {q}")

    output.append("\n2. Hitung Modulus (n): n = p x q")
    output.append(f"   n = {p} x {q} = {n}")

    output.append("\n3. Hitung Fungsi Euler (phi(n)): phi(n) = (p-1)(q-1)")
    output.append(f"   phi(n) = ({p}-1) x ({q}-1) = {p - 1} x {q - 1} = {phi_n}")

    output.append(f"\n4. Eksponen Publik Terpilih: e = {e}")
    output.append(f"   - Syarat: GCD({e}, {phi_n}) = 1 (OK)")

    output.append(f"\n5. Hitung Eksponen Privat (d): d * e = 1 mod phi(n)")
    output.append(f"   d * {e} = 1 mod {phi_n}")

    # --- Detail Perhitungan d ---

    gcd_steps_output, _, final_koefisien, d_final = get_d_calculation_steps(e, phi_n)

    output.append("\n   A. Algoritma Euclidean (Maju) untuk mencari GCD:")
    output.append(f"      (Mencari GCD({e}, {phi_n}))")
    for step in gcd_steps_output:
        output.append(f"      {step}")
    output.append(f"      GCD = {gcd_steps_output[-1].split(' = ')[0]} (Sisa terakhir sebelum 0)")

    output.append("\n   B. Back Substitution (Mundur) untuk mencari d:")
    output.append(f"      Menyusun kombinasi linear 1 = d * e - k * phi(n):")
    output.append(f"      {final_koefisien}")

    output.append(f"      Dari persamaan kombinasi linear, nilai Eksponen Privat **d = {d_final}**")

    # --- Hasil Kunci ---
    output.append("\n6. Hasil Kunci:")
    output.append(f"   Kunci Publik (e, n): ({e}, {n})")
    output.append(f"   Kunci Privat (d, n): ({d}, {n})")

    # Bagian B: Enkripsi
    output.append("\n\nB. TAHAP 2: ENKRIPSI")
    output.append("-------------------------------------------------------------------")
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
    output.append("-------------------------------------------------------------------")
    output.append(f"Formula: m = c^d mod n  =>  m = c^{d} mod {n}")

    output.append(f"\n{'Ciphertext (c)':<15}{'Plaintext (m)':<15}{'Karakter':<10}")
    output.append("-" * 40)
    for c, dm in zip(ciphertext_ints, decrypted_ints):
        output.append(f"{c:<15}{dm:<15}{chr(dm):<10}")
    output.append("-" * 40)
    output.append(f"Plaintext Hasil Dekripsi: {decrypted_text}")

    return "\n".join(output)


# --- Logika GUI ---

def run_rsa_random():
    """Mengambil input plaintext dan menjalankan proses RSA Acak"""

    min_prime = 50
    max_prime = 200
    plaintext = plaintext_entry.get()

    if not plaintext:
        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, "Masukkan Plaintext terlebih dahulu.")
        return

    try:
        # --- 1. Generate Kunci Acak ---
        p = generate_prime(min_prime, max_prime)
        q = generate_prime(min_prime, max_prime)
        while p == q:
            q = generate_prime(min_prime, max_prime)

        n = p * q
        phi_n = (p - 1) * (q - 1)
        e = select_e(phi_n)
        d = mod_inverse(e, phi_n)

        if d is None:
            raise ValueError("Invers modular (d) tidak ditemukan. Terjadi kesalahan pada pemilihan e.")

        # --- 2. Konversi Plaintext ke Angka (ASCII) ---
        plaintext_ints = [ord(char) for char in plaintext]

        if any(m >= n for m in plaintext_ints):
            messagebox.showerror("Error",
                                 f"Nilai ASCII karakter ({max(plaintext_ints)}) terlalu besar dari Modulus n ({n}).")
            return

        # --- 3. Proses Enkripsi ---
        ciphertext_ints = [rsa_encrypt(m, e, n) for m in plaintext_ints]

        # --- 4. Proses Dekripsi ---
        decrypted_ints = [rsa_decrypt(c, d, n) for c in ciphertext_ints]
        decrypted_text = "".join([chr(m) for m in decrypted_ints])

        # --- Menampilkan Output (Langkah Manual yang Rapi) ---
        manual_output = generate_manual_steps(p, q, e, n, phi_n, d, plaintext, plaintext_ints, ciphertext_ints,
                                              decrypted_ints, decrypted_text)

        output_text.delete(1.0, tk.END)
        output_text.insert(tk.END, manual_output)

    except ValueError as e:
        messagebox.showerror("Error", str(e))
    except Exception as e:
        messagebox.showerror("Error Umum", f"Terjadi kesalahan tak terduga: {e}")


# --- Setup GUI ---

root = tk.Tk()
root.title("RSA Cryptography - Latihan 2 (p, q, e Acak)")
root.geometry("750x650")
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
plaintext_entry.insert(0, "ContohRSA")

run_button = ttk.Button(main_frame, text="Jalankan Proses RSA Acak", command=run_rsa_random, style='Run.TButton')
run_button.grid(row=1, column=1, sticky='w', padx=5, pady=5)

# Separator
separator = ttk.Separator(main_frame, orient='horizontal')
separator.grid(row=2, column=0, columnspan=2, sticky='ew', pady=10)

# Output Section
output_label = ttk.Label(main_frame, text="Langkah Perhitungan Manual (Detail dan Rapi):", font=('Arial', 12, 'bold'))
output_label.grid(row=3, column=0, sticky='w', pady=5)

output_text = scrolledtext.ScrolledText(main_frame, width=80, height=25, font=('Courier New', 10), wrap=tk.WORD)
output_text.grid(row=4, column=0, columnspan=2, sticky='nsew', padx=5, pady=5)

# Configure grid weight to make widgets resize appropriately
main_frame.grid_columnconfigure(0, weight=3)
main_frame.grid_columnconfigure(1, weight=1)
main_frame.grid_rowconfigure(4, weight=1)

# Style Customization
root.style.configure('Run.TButton', font=('Arial', 10, 'bold'), foreground='dark green')

root.mainloop()