import tkinter as tk
from tkinter import ttk, messagebox

# ================= MATEMATIKA DASAR =================
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n ** 0.5) + 1):
        if n % i == 0:
            return False
    return True

# ================= KONVERSI =================
def text_to_ascii(text):
    return [ord(c) for c in text]

def ascii_to_text(blocks):
    return ''.join(chr(b) for b in blocks)

# ================= ELGAMAL =================
def elgamal_encrypt(blocks, p, g, y, k, log):
    cipher = []
    log.insert(tk.END, "===== PROSES ENKRIPSI ELGAMAL =====\n\n")

    for i, m in enumerate(blocks, start=1):
        a = pow(g, k, p)
        b = (pow(y, k, p) * m) % p
        cipher.append((a, b))

        log.insert(tk.END, f"Blok m{i} = {m}\n")
        log.insert(tk.END, f"a = g^k mod p = {g}^{k} mod {p} = {a}\n")
        log.insert(tk.END, f"b = y^k * m mod p = {y}^{k} * {m} mod {p} = {b}\n\n")

    return cipher

def elgamal_decrypt(cipher, p, x, log):
    blocks = []
    log.insert(tk.END, "===== PROSES DEKRIPSI ELGAMAL =====\n\n")

    for i, (a, b) in enumerate(cipher, start=1):
        ax_inv = pow(a, p - 1 - x, p)
        m = (b * ax_inv) % p
        blocks.append(m)

        log.insert(tk.END, f"Cipher blok {i}: (a,b)=({a},{b})\n")
        log.insert(tk.END, f"(a^x)^-1 = a^(p-1-x) mod p = {ax_inv}\n")
        log.insert(tk.END, f"m = b * (a^x)^-1 mod p = {m}\n\n")

    return blocks

# ================= GUI FUNCTIONS =================
def hitung_y():
    try:
        p = int(entry_p.get())
        g = int(entry_g.get())
        x = int(entry_x.get())

        if not is_prime(p):
            raise ValueError("p harus bilangan prima")
        if g >= p:
            raise ValueError("g harus < p")
        if not (1 <= x <= p - 2):
            raise ValueError("x harus 1 ≤ x ≤ p−2")

        y = pow(g, x, p)
        entry_y.config(state="normal")
        entry_y.delete(0, tk.END)
        entry_y.insert(0, str(y))
        entry_y.config(state="readonly")

    except Exception as e:
        messagebox.showerror("Error", str(e))

def enkripsi():
    global cipher_data
    try:
        log_text.delete(1.0, tk.END)

        text = entry_plain.get()
        p = int(entry_p.get())
        g = int(entry_g.get())
        y = int(entry_y.get())
        k = int(entry_k.get())

        if not (1 <= k <= p - 2):
            raise ValueError("k harus 1 ≤ k ≤ p−2")

        ascii_blocks = text_to_ascii(text)
        for m in ascii_blocks:
            if m >= p:
                raise ValueError("Nilai ASCII harus < p")

        log_text.insert(tk.END, f"Plaintext : {text}\n")
        log_text.insert(tk.END, f"ASCII     : {ascii_blocks}\n\n")

        cipher_data = elgamal_encrypt(ascii_blocks, p, g, y, k, log_text)
        entry_cipher.delete(0, tk.END)
        entry_cipher.insert(0, str(cipher_data))

    except Exception as e:
        messagebox.showerror("Error", str(e))

def dekripsi():
    try:
        p = int(entry_p.get())
        x = int(entry_x.get())

        blocks = elgamal_decrypt(cipher_data, p, x, log_text)
        result = ascii_to_text(blocks)
        entry_result.delete(0, tk.END)
        entry_result.insert(0, result)

    except Exception as e:
        messagebox.showerror("Error", str(e))

# ================= DESAIN GUI =================
root = tk.Tk()
root.title("Aplikasi ElGamal Encryption & Decryption")
root.geometry("1000x700")
root.minsize(900, 650)
root.resizable(True, True)

style = ttk.Style()
style.theme_use("clam")

main = ttk.Frame(root, padding=15)
main.pack(fill="both", expand=True)

root.columnconfigure(0, weight=1)
root.rowconfigure(0, weight=1)
main.columnconfigure(0, weight=1)
main.columnconfigure(1, weight=1)

# -------- PLAINTEXT --------
plain_frame = ttk.LabelFrame(main, text="Plaintext", padding=10)
plain_frame.grid(row=0, column=0, sticky="ew")

entry_plain = ttk.Entry(plain_frame, width=50)
entry_plain.pack(fill="x")

# -------- PARAMETER --------
param_frame = ttk.LabelFrame(main, text="Parameter ElGamal", padding=10)
param_frame.grid(row=1, column=0, sticky="ew", pady=5)

labels = ["p (prima)", "g (< p)", "x (private)", "y = g^x mod p", "k (acak)"]
entries = []

for lbl in labels:
    row = ttk.Frame(param_frame)
    row.pack(fill="x", pady=2)
    ttk.Label(row, text=lbl, width=15).pack(side="left")
    e = ttk.Entry(row, width=20)
    e.pack(side="left")
    entries.append(e)

entry_p, entry_g, entry_x, entry_y, entry_k = entries
entry_y.config(state="readonly")

# -------- BUTTON --------
btn_frame = ttk.Frame(main)
btn_frame.grid(row=2, column=0, pady=5)

ttk.Button(btn_frame, text="Hitung y", command=hitung_y).pack(side="left", padx=5)
ttk.Button(btn_frame, text="Enkripsi", command=enkripsi).pack(side="left", padx=5)
ttk.Button(btn_frame, text="Dekripsi", command=dekripsi).pack(side="left", padx=5)

# -------- OUTPUT --------
out_frame = ttk.LabelFrame(main, text="Output", padding=10)
out_frame.grid(row=3, column=0, sticky="ew", pady=5)

ttk.Label(out_frame, text="Ciphertext (a,b)").pack(anchor="w")
entry_cipher = ttk.Entry(out_frame, width=80)
entry_cipher.pack(fill="x")

ttk.Label(out_frame, text="Hasil Dekripsi").pack(anchor="w", pady=(5, 0))
entry_result = ttk.Entry(out_frame, width=50)
entry_result.pack()

# -------- LOG PROSES --------
log_frame = ttk.LabelFrame(main, text="Proses Perhitungan (Manual View)", padding=10)
log_frame.grid(row=0, column=1, rowspan=4, padx=10, sticky="nsew")

log_scroll = ttk.Scrollbar(log_frame, orient="vertical")
log_scroll.pack(side="right", fill="y")

log_text = tk.Text(log_frame, wrap="word", yscrollcommand=log_scroll.set)
log_text.pack(fill="both", expand=True)

log_scroll.config(command=log_text.yview)

root.mainloop()
