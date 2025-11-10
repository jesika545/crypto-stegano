# Program: Substitusi + Transposisi Cipher Lengkap (Input aturan via keyboard)
# Author: Jeviera
# Deskripsi:
# a) Input plaintext dari keyboard
# b) Substitusi Cipher (aturan ditentukan user)
# c) Transposisi Cipher (4 blok, baca kolom per kolom)
# d) Menampilkan hasil berurutan:
#    1. Plaintext
#    2. Ciphertext hasil Substitusi Cipher
#    3. Ciphertext hasil Substitusi + Transposisi Cipher
#    + menampilkan proses pembentukan blok dan pengisian ciphertext

def buat_aturan_substitusi():
    aturan = {}
    print("\n=== Masukkan Aturan Substitusi ===")
    print("Contoh input:")
    print("  Huruf Plaintext: A")
    print("  Huruf Pengganti: X")
    print("Ketik 'selesai' untuk berhenti.\n")

    while True:
        p = input("Masukkan huruf plaintext (atau 'selesai'): ").strip().upper()
        if p == "SELESAI":
            break
        if len(p) != 1 or not p.isalpha():
            print("Masukkan satu huruf alfabet saja!")
            continue

        c = input(f"Masukkan huruf pengganti untuk '{p}': ").strip().upper()
        if len(c) != 1 or not c.isalpha():
            print("Masukkan satu huruf alfabet saja!")
            continue

        aturan[p] = c
        print(f"  Aturan tersimpan: {p} → {c}\n")

    if not aturan:
        print("Tidak ada aturan yang dimasukkan, teks tidak akan berubah.")
    return aturan


def substitusi_cipher(plaintext, aturan):
    hasil = ""
    for huruf in plaintext:
        if huruf in aturan:
            hasil += aturan[huruf]
        else:
            hasil += huruf
    return hasil


def transposisi_cipher(teks):
    print("\n=== Pembentukan Blok Transposisi ===")
    blok_ukuran = 4
    panjang = len(teks)
    blok = []

    # Bagi teks menjadi blok 4 karakter
    for i in range(0, panjang, blok_ukuran):
        potongan = teks[i:i + blok_ukuran]
        potongan = potongan.ljust(blok_ukuran)
        blok.append(potongan)

    # Tampilkan isi blok
    for i, b in enumerate(blok):
        print(f"Bagian {i + 1}: '{b}'")

    print("\n=== Proses Transposisi (baca kolom per kolom) ===")
    ciphertext = ""
    for kolom in range(blok_ukuran):
        for baris in range(len(blok)):
            huruf = blok[baris][kolom]
            ciphertext += huruf
            print(f"Menambahkan '{huruf}' dari Bagian {baris + 1} ke ciphertext.")
    return ciphertext.strip()


# --- Program Utama ---
print("=== Program Substitusi + Transposisi Cipher ===")
plaintext = input("Masukkan plaintext: ").upper()

# Tahap 1: Aturan Substitusi
aturan = buat_aturan_substitusi()

# Tahap 2: Substitusi Cipher
substitusi = substitusi_cipher(plaintext, aturan)
print("\nHasil Substitusi Cipher :", substitusi)

# Tahap 3: Transposisi Cipher
ciphertext_final = transposisi_cipher(substitusi)

# --- Tampilkan hasil akhir sesuai urutan soal ---
print("\n=== HASIL AKHIR ===")
print(f"1️ Plaintext Asli : {plaintext}")
print(f"2️ Hasil Substitusi Cipher : {substitusi}")
print(f"3️ Hasil Substitusi + Transposisi Cipher : {ciphertext_final}")
