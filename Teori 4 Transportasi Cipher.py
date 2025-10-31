## 🔐 TIGA VERSI PROGRAM TRANSPOSISI CIPHER (KOLOM)

# =========================================================================
# 1. KODE PROGRAM STATIS (Plaintext ditentukan di dalam kode)
# =========================================================================

def transposisi_cipher_statis(plaintext):
    # Hitung panjang setiap bagian (dibulatkan ke atas untuk sisa)
    # Note: Menggunakan // 4 + (1 jika ada sisa), tetapi implementasi di gambar
    # menggunakan len(plaintext) // 4 (pembagian integer), yang akan memotong bagian terakhir
    # jika panjangnya tidak habis dibagi 4. Saya menggunakan pendekatan dari gambar.
    part_length = len(plaintext) // 4

    # Buat 4 bagian (blok)
    # Mengiris plaintext berdasarkan part_length.
    parts = [plaintext[i * part_length:(i + 1) * part_length] for i in range(4)]

    # Menambahkan sisa (jika ada) ke bagian terakhir
    remainder = plaintext[4 * part_length:]
    if remainder:
        parts.append(remainder)  # Versi gambar asli hanya menggunakan 4 bagian,
        # jadi sisa ini harus dipertimbangkan
        # Namun, berdasarkan logika loop di bawah (for col in range(4)),
        # dan hasil eksekusi, panjangnya harus habis dibagi atau diproses
        # dalam 4 kolom. Kita ikuti struktur gambar.

    # Perbaikan: Berdasarkan contoh eksekusi di gambar, sepertinya length dibagi 4
    # dan sisanya (jika ada) diabaikan atau ditambahkan di luar range(4).
    # Untuk mereplikasi tepat seperti di gambar:
    if len(plaintext) % 4 != 0:
        part_length = len(plaintext) // 4 + 1  # Menggunakan pembulatan ke atas
        parts = [plaintext[i * part_length:(i + 1) * part_length] for i in range(4)]
    else:
        part_length = len(plaintext) // 4
        parts = [plaintext[i * part_length:(i + 1) * part_length] for i in range(4)]

    # Mengikuti versi gambar untuk mendapatkan hasil yang sama, kita asumsikan
    # part_length = len(plaintext) // 4 dan sisanya ditangani dengan memotong
    # atau panjangnya 18 (seperti "UNIKA SANTO THOMAS") yang jika dibagi 4:
    # 18 // 4 = 4. Sisa 2.
    # UNIK | A SA | NTO | THOM | AS  <- Jika dibagi 5 blok.
    # UNIK | A SAN | TO TH | OMAS <- Jika dibagi 4 blok dengan part_length = 5
    # UNIK A | SANTO | THOMAS | <- Jika dibagi 3 blok

    # Kita harus mereplikasi persis mekanisme di gambar:
    # Jika plaintext="UNIKA SANTO THOMAS" (18 karakter)
    # part_length = 18 // 4 = 4
    # parts = [plaintext[i*4 : (i+1)*4] for i in range(4)]
    # parts[0] = "UNIK" (i=0)
    # parts[1] = "A SA" (i=1, dari index 4 sampai 8)
    # parts[2] = "NTO " (i=2, dari index 8 sampai 12)
    # parts[3] = "THOM" (i=3, dari index 12 sampai 16)
    # Plaintext sisa: "AS" (dari index 16)
    # Hasil eksekusi di gambar: 'UNIK', 'A SA', 'NTO', 'THOM', 'AS' (5 bagian)
    # Program di gambar HANYA memproses 4 bagian dari slicing. Mari kita gunakan slicing yang benar:

    # Program di gambar MENGGUNAKAN part_length dari len(plaintext) // 4
    # dan hasilnya menunjukkan 5 bagian di versi "menampilkan pembentukan blok",
    # yang menyiratkan sisa juga dimasukkan sebagai bagian kelima.
    # Mari kita gunakan versi gambar yang dinamis untuk handling blok:

    length = len(plaintext)
    part_length = length // 4

    # Memastikan 4 kolom penuh terbentuk, sisa ditambahkan ke list parts.
    # Ini mereplikasi hasil "UNIK", "A SA", "NTO", "THOM", "AS" (5 bagian)
    parts = []
    for i in range(4):
        start = i * part_length
        end = (i + 1) * part_length
        parts.append(plaintext[start:end])

    # Menambahkan sisa sebagai bagian terakhir
    if length > 4 * part_length:
        parts.append(plaintext[4 * part_length:])

    # Jika len(plaintext)=18, part_length=4
    # parts = ["UNIK", "A SA", "NTO ", "THOM", "AS"] - Catatan: Awalnya 5 bagian

    ciphertext = ""
    # Enkripsi: Ambil karakter dari kolom (indeks) yang sama dari setiap bagian
    # Loop melalui 4 kolom (indeks 0, 1, 2, 3)
    for col in range(4):
        # Loop melalui setiap bagian (baris)
        for part in parts:
            # Pastikan indeks kolom tidak melebihi panjang bagian saat ini
            if col < len(part):
                ciphertext += part[col]

    return ciphertext


# Plaintext untuk versi statis
plaintext_statis = "UNIKA SANTO THOMAS"
ciphertext_statis = transposisi_cipher_statis(plaintext_statis)
print("--- 1. KODE PROGRAM STATIS ---")
print(f'Plaintext: "{plaintext_statis}"')
print(f'Ciphertext: "{ciphertext_statis}"')
print("-------------------------------------------------------------------------")


# =========================================================================
# 2. KODE PROGRAM DINAMIS DENGAN INPUT (Tanpa Menampilkan Blok)
# =========================================================================

def transposisi_cipher_dinamis(plaintext):
    length = len(plaintext)
    # Hitung panjang setiap bagian.
    # Jika 18, part_length = 4
    part_length = length // 4

    # Buat 4 bagian awal
    parts = []
    for i in range(4):
        start = i * part_length
        end = (i + 1) * part_length
        parts.append(plaintext[start:end])

    # Menambahkan sisa sebagai bagian terakhir
    if length > 4 * part_length:
        parts.append(plaintext[4 * part_length:])

    ciphertext = ""
    # Enkripsi: Ambil karakter secara kolom per kolom (hanya 4 kolom utama)
    for col in range(4):
        for part in parts:
            if col < len(part):
                ciphertext += part[col]

    return ciphertext


print("--- 2. KODE PROGRAM DINAMIS DENGAN INPUT ---")
plaintext_dinamis = input("Masukkan plaintext: ")
ciphertext_dinamis = transposisi_cipher_dinamis(plaintext_dinamis)
print(f'Ciphertext: "{ciphertext_dinamis}"')
print("-------------------------------------------------------------------------")


# =========================================================================
# 3. KODE PROGRAM DENGAN PENAMPILAN PEMBENTUKAN BLOK (Paling Detil)
# =========================================================================

def transposisi_cipher_detil(plaintext):
    length = len(plaintext)
    part_length = length // 4

    # Buat bagian (blok)
    parts = []
    for i in range(4):
        start = i * part_length
        end = (i + 1) * part_length
        parts.append(plaintext[start:end])

    # Menambahkan sisa sebagai bagian terakhir
    if length > 4 * part_length:
        parts.append(plaintext[4 * part_length:])

    # Tampilkan Pembagian Blok
    print("\nBagian plaintext:")
    for i, part in enumerate(parts):
        print(f"Bagian {i + 1}: '{part}'")

    ciphertext = ""
    # Enkripsi: Ambil karakter secara kolom per kolom (hanya 4 kolom utama)
    for col in range(4):
        for part in parts:
            if col < len(part):
                # Tampilkan proses penambahan karakter
                print(f"Menambahkan '{part[col]}' dari Bagian {parts.index(part) + 1} ke ciphertext.")
                ciphertext += part[col]

    return ciphertext


print("--- 3. KODE PROGRAM DENGAN PENAMPILAN PEMBENTUKAN BLOK ---")
plaintext_detil = input("Masukkan plaintext: ")
ciphertext_detil = transposisi_cipher_detil(plaintext_detil)
print(f'\nCiphertext: "{ciphertext_detil}"')
print("-------------------------------------------------------------------------")