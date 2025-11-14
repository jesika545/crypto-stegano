import tkinter as tk
from tkinter import ttk, scrolledtext, messagebox

# --- 1. Definisi Tabel Permutasi dan Konstanta DES ---

# Permuted Choice 1 (PC-1)
PC_1 = [
    57, 49, 41, 33, 25, 17, 9, 1, 58, 50, 42, 34, 26, 18,
    10, 2, 59, 51, 43, 35, 27, 19, 11, 3, 60, 52, 44, 36,
    63, 55, 47, 39, 31, 23, 15, 7, 62, 54, 46, 38, 30, 22,
    14, 6, 61, 53, 45, 37, 29, 21, 13, 5, 28, 20, 12, 4
]

# Permuted Choice 2 (PC-2)
PC_2 = [
    14, 17, 11, 24, 1, 5, 3, 28, 15, 6, 21, 10,
    23, 19, 12, 4, 26, 8, 16, 7, 27, 20, 13, 2,
    41, 52, 31, 37, 47, 55, 30, 40, 51, 45, 33, 48,
    44, 49, 39, 56, 34, 53, 46, 42, 50, 36, 29, 32
]

# Jumlah pergeseran kiri (Left Shift) untuk 16 putaran
SHIFTS = [1, 1, 2, 2, 2, 2, 2, 2, 1, 2, 2, 2, 2, 2, 2, 1]

# Initial Permutation (IP)
IP = [
    58, 50, 42, 34, 26, 18, 10, 2, 60, 52, 44, 36, 28, 20, 12, 4,
    62, 54, 46, 38, 30, 22, 14, 6, 64, 56, 48, 40, 32, 24, 16, 8,
    57, 49, 41, 33, 25, 17, 9, 1, 59, 51, 43, 35, 27, 19, 11, 3,
    61, 53, 45, 37, 29, 21, 13, 5, 63, 55, 47, 39, 31, 23, 15, 7
]

# Final Permutation (IP Inverse / IP^-1)
IP_INV = [
    40, 8, 48, 16, 56, 24, 64, 32, 39, 7, 47, 15, 55, 23, 63, 31,
    38, 6, 46, 14, 54, 22, 62, 30, 37, 5, 45, 13, 53, 21, 61, 29,
    36, 4, 44, 12, 52, 20, 60, 28, 35, 3, 43, 11, 51, 19, 59, 27,
    34, 2, 42, 10, 50, 18, 58, 26, 33, 1, 41, 9, 49, 17, 57, 25
]

# Expansion Permutation (E-box)
E = [
    32, 1, 2, 3, 4, 5, 4, 5, 6, 7, 8, 9, 8, 9, 10, 11,
    12, 13, 12, 13, 14, 15, 16, 17, 16, 17, 18, 19, 20, 21, 20, 21,
    22, 23, 24, 25, 24, 25, 26, 27, 28, 29, 28, 29, 30, 31, 32, 1
]

# Permutation P
P = [
    16, 7, 20, 21, 29, 12, 28, 17, 1, 15, 23, 26, 5, 18, 31, 10,
    2, 8, 24, 14, 32, 27, 3, 9, 19, 13, 30, 6, 22, 11, 4, 25
]

# S-boxes (S1 sampai S8)
S_BOX = [
    [[14, 4, 13, 1, 2, 15, 11, 8, 3, 10, 6, 12, 5, 9, 0, 7], [0, 15, 7, 4, 14, 2, 13, 1, 10, 6, 12, 11, 9, 5, 3, 8],
     [4, 1, 14, 8, 13, 6, 2, 11, 15, 12, 9, 7, 3, 10, 5, 0], [15, 12, 8, 2, 4, 9, 1, 7, 5, 11, 3, 14, 10, 0, 6, 13]],
    [[15, 1, 8, 14, 6, 11, 3, 4, 9, 7, 2, 13, 12, 0, 5, 10], [3, 13, 4, 7, 15, 2, 8, 14, 12, 0, 1, 10, 6, 9, 11, 5],
     [0, 14, 7, 11, 10, 4, 13, 1, 5, 8, 12, 6, 9, 3, 2, 15], [13, 8, 10, 1, 3, 15, 4, 2, 11, 6, 7, 12, 0, 5, 14, 9]],
    [[10, 0, 9, 14, 6, 3, 15, 5, 1, 13, 12, 7, 11, 4, 2, 8], [13, 7, 0, 9, 3, 4, 6, 10, 2, 8, 5, 14, 12, 11, 15, 1],
     [13, 6, 4, 9, 8, 15, 3, 0, 11, 1, 2, 12, 5, 10, 14, 7], [1, 10, 13, 0, 6, 9, 8, 7, 4, 15, 14, 3, 11, 5, 2, 12]],
    [[7, 13, 14, 3, 0, 6, 9, 10, 1, 2, 8, 5, 11, 12, 4, 15], [13, 8, 11, 5, 6, 15, 0, 3, 4, 7, 2, 12, 1, 10, 14, 9],
     [10, 6, 9, 0, 12, 11, 7, 13, 15, 1, 3, 14, 5, 2, 8, 4], [3, 15, 0, 6, 10, 1, 13, 8, 9, 4, 5, 11, 12, 7, 2, 14]],
    [[2, 12, 4, 1, 7, 10, 11, 6, 8, 5, 3, 15, 13, 0, 14, 9], [14, 11, 2, 12, 4, 7, 13, 1, 5, 0, 15, 10, 3, 9, 8, 6],
     [4, 2, 1, 11, 10, 13, 7, 8, 15, 9, 12, 5, 6, 3, 0, 14], [11, 8, 12, 7, 1, 14, 2, 13, 6, 15, 0, 9, 10, 4, 5, 3]],
    [[12, 1, 10, 15, 9, 2, 6, 8, 0, 13, 3, 4, 14, 7, 5, 11], [10, 15, 4, 2, 7, 12, 9, 5, 6, 1, 13, 14, 0, 11, 3, 8],
     [9, 14, 15, 5, 2, 8, 12, 3, 7, 0, 4, 10, 1, 13, 11, 6], [4, 3, 2, 12, 9, 5, 15, 10, 11, 14, 1, 7, 6, 0, 8, 13]],
    [[4, 11, 2, 14, 15, 0, 8, 13, 3, 12, 9, 7, 5, 10, 6, 1], [13, 0, 11, 7, 4, 9, 1, 10, 14, 3, 5, 12, 2, 15, 8, 6],
     [1, 4, 11, 13, 12, 3, 7, 14, 10, 15, 6, 0, 8, 2, 9, 5], [10, 13, 1, 0, 7, 11, 4, 9, 15, 2, 12, 5, 6, 8, 3, 14]],
    [[13, 2, 8, 4, 6, 15, 11, 1, 10, 9, 3, 14, 5, 0, 12, 7], [1, 15, 13, 8, 10, 3, 7, 4, 12, 5, 6, 11, 0, 14, 9, 2],
     [7, 11, 4, 1, 9, 12, 14, 2, 0, 6, 10, 13, 15, 3, 5, 8], [2, 1, 14, 7, 4, 10, 8, 13, 15, 12, 9, 0, 3, 5, 6, 11]]
]


# --- 2. Fungsi Pembantu Konversi dan Operasi Bit ---

def text_to_binary_des(text, block_size=8, pad_char='00000000'):
    """Konversi teks ke biner dan padding '00000000' untuk kelipatan 64-bit."""
    binary_list = []
    char_bin_map = {}

    for char in text:
        binary_code = format(ord(char), '08b')
        binary_list.append(binary_code)
        key = char if char not in char_bin_map else f"{char}_idx{len(binary_list)}"
        char_bin_map[key] = binary_code

    if len(binary_list) % block_size != 0:
        pad_count = 0
        while len(binary_list) % block_size != 0:
            binary_list.append(pad_char)
            pad_count += 1
            char_bin_map[f"PAD{pad_count}"] = pad_char

    return "".join(binary_list), char_bin_map


def binary_to_hex(binary_str):
    """Konversi biner ke heksadesimal."""
    if not binary_str: return ""
    remainder = len(binary_str) % 4
    if remainder != 0:
        binary_str = '0' * (4 - remainder) + binary_str

    hex_str = hex(int(binary_str, 2))[2:].upper()
    if len(hex_str) % 2 != 0:
        hex_str = '0' + hex_str
    return hex_str


def hex_to_ascii(hex_str):
    """
    Konversi string heksadesimal ke string karakter.
    Menggunakan encoding latin-1 karena output DES (ciphertext) adalah data biner acak
    yang sering di luar rentang karakter cetak ASCII standar.
    """
    try:
        if len(hex_str) % 2 != 0:
            hex_str = '0' + hex_str

        bytes_object = bytes.fromhex(hex_str)
        # Menggunakan 'latin-1' (ISO-8859-1) yang memetakan setiap byte (0-255) ke karakter
        return bytes_object.decode('latin-1')
    except:
        return "[Error konversi ASCII]"


def apply_permutation(data_bits, table):
    """Menerapkan permutasi (tabel berbasis 1)."""
    return [data_bits[i - 1] for i in table]


def left_shift(bits, shift_count):
    """Pergeseran kiri melingkar (Rotasi)."""
    return bits[shift_count:] + bits[:shift_count]


def xor_bits(bits1, bits2):
    """Operasi XOR."""
    return [b1 ^ b2 for b1, b2 in zip(bits1, bits2)]


def bin_to_int(bits):
    """Biner ke integer."""
    return int("".join(map(str, bits)), 2)


def int_to_bin_array(integer, length):
    """Integer ke biner array."""
    return [int(b) for b in format(integer, f'0{length}b')]


# --- 3. Pembentukan Subkunci (Key Schedule) ---

def generate_subkeys(key):
    """Menghasilkan 16 subkunci K1 hingga K16."""

    key_padded = key[:8].ljust(8, '\0')
    key_binary_str, key_char_map = text_to_binary_des(key_padded, block_size=8, pad_char='00000000')
    key_bits_64 = [int(bit) for bit in key_binary_str]

    # 1. PC-1 (-> 56 bit: C0 dan D0)
    key_bits_56 = apply_permutation(key_bits_64, PC_1)

    C_values = [key_bits_56[:28]]  # C0
    D_values = [key_bits_56[28:]]  # D0

    subkeys = []

    # 2. 16 Putaran Rotasi Kiri & PC-2
    for i in range(16):
        shift = SHIFTS[i]

        C_new = left_shift(C_values[-1], shift)
        D_new = left_shift(D_values[-1], shift)

        C_values.append(C_new)
        D_values.append(D_new)

        combined_56 = C_new + D_new

        # PC-2 (-> 48 bit Subkunci Ki)
        K_i = apply_permutation(combined_56, PC_2)
        subkeys.append(K_i)

    # Mengembalikan 5 nilai
    return subkeys, C_values, D_values, key_binary_str, key_char_map


# --- 4. Fungsi Feistel (F-Function) dan Enkripsi Blok ---

def feistel_function(R_in, subkey_k):
    """Fungsi Feistel F(R, K) = P(S(E(R) XOR K))."""

    R_expanded = apply_permutation(R_in, E)
    R_xor_K = xor_bits(R_expanded, subkey_k)
    R_substituted = []

    for i in range(8):
        block_6 = R_xor_K[i * 6: (i + 1) * 6]
        row = bin_to_int([block_6[0], block_6[5]])
        col = bin_to_int(block_6[1:5])
        s_val = S_BOX[i][row][col]
        R_substituted.extend(int_to_bin_array(s_val, 4))

    R_out = apply_permutation(R_substituted, P)

    return R_out


def encrypt_block(block_bits_64, subkeys):
    """Melakukan enkripsi satu blok 64-bit."""

    IP_output = apply_permutation(block_bits_64, IP)
    L = IP_output[:32]
    R = IP_output[32:]

    for i in range(16):
        L_prev = L
        R_prev = R
        K_i = subkeys[i]

        L_new = R_prev
        F_output = feistel_function(R_prev, K_i)
        R_new = xor_bits(L_prev, F_output)

        L = L_new
        R = R_new

    R16L16 = R + L
    ciphertext_block_bits = apply_permutation(R16L16, IP_INV)

    return ciphertext_block_bits


# --- 5. Program Utama GUI (Tkinter) ---

class DESApp:
    def __init__(self, master):
        self.master = master
        master.title("DES Enkripsi - Data Encryption Standard (GUI)")

        self.plaintext_var = tk.StringVar()
        self.key_var = tk.StringVar()

        style = ttk.Style()
        style.configure('TFrame', padding=10)
        style.configure('TLabel', padding=5)

        main_frame = ttk.Frame(master)
        main_frame.pack(padx=10, pady=10, fill='both', expand=True)

        # Input Frame
        input_frame = ttk.LabelFrame(main_frame, text="📥 Input Plaintext & Kunci (Dinamis)")
        input_frame.pack(fill='x', pady=5)

        ttk.Label(input_frame, text="Plaintext (Teks Bebas):").grid(row=0, column=0, sticky='w', padx=5, pady=2)
        self.plaintext_entry = ttk.Entry(input_frame, textvariable=self.plaintext_var, width=60)
        self.plaintext_entry.grid(row=0, column=1, sticky='ew', padx=5, pady=2)

        ttk.Label(input_frame, text="Kunci (Maks 8 Karakter):").grid(row=1, column=0, sticky='w', padx=5, pady=2)
        self.key_entry = ttk.Entry(input_frame, textvariable=self.key_var, width=60)
        self.key_entry.grid(row=1, column=1, sticky='ew', padx=5, pady=2)

        ttk.Button(main_frame, text="PROSES ENKRIPSI DES", command=self.process_des).pack(fill='x', pady=10)

        # Output Frame
        output_frame = ttk.LabelFrame(main_frame, text="📊 Hasil Proses DES")
        output_frame.pack(fill='both', expand=True, pady=5)

        # Output Konversi Biner
        ttk.Label(output_frame, text="**1. Konversi Biner Plaintext & Kunci (64-bit):**",
                  font='TkDefaultFont 10 bold').pack(fill='x', padx=5, pady=2)
        self.konversi_bin_text = scrolledtext.ScrolledText(output_frame, height=7, wrap=tk.WORD)
        self.konversi_bin_text.pack(fill='x', padx=5, pady=2)

        # Output Subkeys
        ttk.Label(output_frame, text="**2. 16 Subkey (K1 - K16) & Proses Rotasi:**", font='TkDefaultFont 10 bold').pack(
            fill='x', padx=5, pady=2)
        self.subkeys_text = scrolledtext.ScrolledText(output_frame, height=12, wrap=tk.WORD)
        self.subkeys_text.pack(fill='both', expand=True, padx=5, pady=2)

        # Output Ciphertext Biner
        ttk.Label(output_frame, text="**3. Ciphertext (Biner 64-bit Blok):**", font='TkDefaultFont 10 bold').pack(
            fill='x', padx=5, pady=2)
        self.ciphertext_bin_text = scrolledtext.ScrolledText(output_frame, height=4, wrap=tk.WORD)
        self.ciphertext_bin_text.pack(fill='x', padx=5, pady=2)

        # Output Ciphertext Heksadesimal
        ttk.Label(output_frame, text="**4. Ciphertext (Hexadesimal):**", font='TkDefaultFont 10 bold').pack(fill='x',
                                                                                                            padx=5,
                                                                                                            pady=2)
        self.ciphertext_hex_text = scrolledtext.ScrolledText(output_frame, height=2, wrap=tk.WORD)
        self.ciphertext_hex_text.pack(fill='x', padx=5, pady=2)

        # Output Ciphertext ASCII
        ttk.Label(output_frame, text="**5. Ciphertext (Kode ASCII):**", font='TkDefaultFont 10 bold').pack(fill='x',
                                                                                                           padx=5,
                                                                                                           pady=2)
        self.ciphertext_ascii_text = scrolledtext.ScrolledText(output_frame, height=2, wrap=tk.WORD)
        self.ciphertext_ascii_text.pack(fill='x', padx=5, pady=2)

    def clear_output(self):
        self.konversi_bin_text.delete(1.0, tk.END)
        self.ciphertext_bin_text.delete(1.0, tk.END)
        self.ciphertext_hex_text.delete(1.0, tk.END)
        self.ciphertext_ascii_text.delete(1.0, tk.END)
        self.subkeys_text.delete(1.0, tk.END)

    def display_output(self, subkeys, C_values, D_values, key_bin_str, pt_bin_str, pt_char_map, ciphertext_bin,
                       ciphertext_hex, key_char_map):

        # --- 1. Tampilkan Konversi Biner Plaintext dan Kunci ---
        konversi_output = "--- Konversi Kunci (64-bit) ---\n"
        konversi_output += f"Kunci Input: {self.key_var.get()[:8].ljust(8, ' ')}\n"

        konversi_output += "Detail Kunci per Karakter (8-bit):\n"
        for char, biner in key_char_map.items():
            display_char = char.split('_')[0] if '_' in char else char
            konversi_output += f"  - {display_char.ljust(15)}: {biner}\n"

        konversi_output += f"Kunci Biner Total (64-bit): {key_bin_str}\n\n"

        konversi_output += "--- Konversi Plaintext (64-bit Blok) ---\n"
        konversi_output += f"Plaintext Input: {self.plaintext_var.get()}\n"

        konversi_output += "Detail Plaintext/Padding per Karakter (8-bit):\n"
        for char, biner in pt_char_map.items():
            display_char = "PAD (00000000)" if char.startswith("PAD") else (char.split('_')[0] if '_' in char else char)
            konversi_output += f"  - {display_char.ljust(15)}: {biner}\n"

        konversi_output += f"\nPlaintext Biner Total (dengan padding): {pt_bin_str}\n"

        self.konversi_bin_text.insert(tk.END, konversi_output)

        # --- 2. Tampilkan Proses Pembentukan Kunci (Subkeys) ---
        key_output = "--- Proses Pembentukan Kunci ---\n"

        C0_str = "".join(map(str, C_values[0]))
        D0_str = "".join(map(str, D_values[0]))
        key_output += f"C0 (28-bit - hasil PC-1): {C0_str}\n"
        key_output += f"D0 (28-bit - hasil PC-1): {D0_str}\n\n"

        for i in range(16):
            Ci_str = "".join(map(str, C_values[i + 1]))
            Di_str = "".join(map(str, D_values[i + 1]))
            Ki_str = "".join(map(str, subkeys[i]))

            key_output += f"Round {i + 1} (Shift {SHIFTS[i]}): \n"
            key_output += f"  C{i + 1}: {Ci_str}\n"
            key_output += f"  D{i + 1}: {Di_str}\n"
            key_output += f"  K{i + 1} (Subkey 48-bit - PC-2): {Ki_str}\n"
            key_output += "--------------------------------------\n"

        self.subkeys_text.insert(tk.END, key_output)

        # --- 3, 4, 5. Tampilkan Ciphertext Biner, Hex, dan ASCII ---

        # Biner (format blok)
        bin_output = ""
        for i in range(0, len(ciphertext_bin), 64):
            bin_output += f"Blok {i // 64 + 1}: {ciphertext_bin[i:i + 64]}\n"
        self.ciphertext_bin_text.insert(tk.END, bin_output)

        # Heksadesimal
        self.ciphertext_hex_text.insert(tk.END, ciphertext_hex)

        # ASCII
        ascii_output = hex_to_ascii(ciphertext_hex)
        self.ciphertext_ascii_text.insert(tk.END, ascii_output)

    def process_des(self):
        self.clear_output()

        plaintext = self.plaintext_var.get()
        key = self.key_var.get()

        if not plaintext or not key:
            messagebox.showerror("Error", "Plaintext dan Kunci harus diisi.")
            return

        # 1. KONVERSI PLAINTEXT KE BINER (DENGAN PADDING)
        plaintext_binary_str, pt_char_map = text_to_binary_des(plaintext, block_size=8, pad_char='00000000')

        # 2. GENERATE SUBKEYS (Menerima 5 nilai)
        try:
            subkeys, C_values, D_values, key_bin_str, key_char_map = generate_subkeys(key)
        except Exception as e:
            messagebox.showerror("Error Key Schedule", f"Terjadi kesalahan saat membuat subkunci: {e}")
            return

        # 3. ENKRIPSI

        total_blocks = len(plaintext_binary_str) // 64
        ciphertext_total_bin = ""

        for i in range(total_blocks):
            block_start = i * 64
            block_end = (i + 1) * 64
            current_block_bin_str = plaintext_binary_str[block_start:block_end]

            block_bits_64 = [int(bit) for bit in current_block_bin_str]

            # Enkripsi blok 64-bit
            try:
                ciphertext_block_bits = encrypt_block(block_bits_64, subkeys)
            except Exception as e:
                messagebox.showerror("Error Enkripsi Blok", f"Terjadi kesalahan saat enkripsi blok {i + 1}: {e}")
                return

            ciphertext_total_bin += "".join(map(str, ciphertext_block_bits))

        # 4. MENAMPILKAN HASIL

        ciphertext_total_hex = binary_to_hex(ciphertext_total_bin)

        self.display_output(subkeys, C_values, D_values, key_bin_str, plaintext_binary_str, pt_char_map,
                            ciphertext_total_bin, ciphertext_total_hex, key_char_map)
        messagebox.showinfo("Selesai", "Proses Enkripsi DES telah selesai!")


# --- Eksekusi GUI ---
if __name__ == '__main__':
    root = tk.Tk()
    root.geometry("850x850")
    app = DESApp(root)
    root.mainloop()