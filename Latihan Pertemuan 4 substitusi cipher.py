def substitusi_cipher(plaintext, aturan):
    """
    Fungsi ini digunakan untuk melakukan proses enkripsi menggunakan metode Substitusi Cipher.
    Setiap huruf pada plaintext akan diganti dengan huruf lain berdasarkan aturan yang telah dibuat.
    """
    ciphertext = ''  # Variabel untuk menampung hasil enkripsi

    # Mengubah seluruh huruf menjadi huruf besar agar sesuai dengan aturan substitusi
    for char in plaintext.upper():
        # Jika huruf ditemukan dalam aturan, ganti sesuai pasangan
        if char in aturan:
            ciphertext += aturan[char]
        else:
            # Jika huruf tidak ada dalam aturan (misalnya spasi atau tanda baca), tetap ditampilkan apa adanya
            ciphertext += char
    return ciphertext


def buat_aturan_substitusi():
    """
    Fungsi ini digunakan untuk membuat aturan substitusi secara manual.
    Pengguna akan memasukkan pasangan huruf satu per satu.
    """
    aturan = {}  # Menyimpan pasangan huruf substitusi
    print("\n=== PEMBUATAN ATURAN SUBSTITUSI ===")
    print("Masukkan pasangan huruf satu per satu.")
    print("Ketik 'selesai' jika sudah selesai membuat aturan.\n")

    while True:
        # Memasukkan huruf asli (plaintext)
        p_char = input("Masukkan huruf asli (Plaintext): ").upper()
        if p_char == 'SELESAI':
            break

        # Validasi agar hanya satu huruf alfabet yang dimasukkan
        if len(p_char) != 1 or not p_char.isalpha():
            print("⚠️ Masukkan hanya satu huruf alfabet.")
            continue

        # Memasukkan huruf pengganti (ciphertext)
        c_char = input(f"Gantikan '{p_char}' dengan huruf: ").upper()

        # Validasi huruf pengganti
        if len(c_char) != 1 or not c_char.isalpha():
            print("⚠️ Masukkan hanya satu huruf alfabet.")
            continue

        # Menyimpan aturan substitusi ke dalam dictionary
        aturan[p_char] = c_char
        print(f"✅ Aturan ditambahkan: {p_char} → {c_char}\n")

    return aturan


# ==========================
# PROGRAM UTAMA
# ==========================

print("========================================")
print("     PROGRAM ENKRIPSI SUBSTITUSI CIPHER")
print("========================================")

# 1. Membuat aturan substitusi
aturan_substitusi = buat_aturan_substitusi()

# 2. Jika tidak ada aturan yang dibuat, hentikan program
if not aturan_substitusi:
    print("\nTidak ada aturan yang dibuat. Program dihentikan.")
else:
    # 3. Input teks yang akan dienkripsi
    print("\n=== PROSES ENKRIPSI ===")
    plaintext = input("Masukkan teks yang ingin dienkripsi: ")

    # 4. Melakukan proses enkripsi
    ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

    # 5. Menampilkan hasil enkripsi
    print("\n=== HASIL ENKRIPSI ===")
    print(f"Teks Asli        : {plaintext}")
    print(f"Teks (Uppercase) : {plaintext.upper()}")
    print(f"Hasil Enkripsi   : {ciphertext}")

    # 6. Menampilkan aturan yang digunakan
    print("\nAturan Substitusi yang Digunakan:")
    for huruf_asli, huruf_ganti in aturan_substitusi.items():
        print(f"{huruf_asli} → {huruf_ganti}")
