## 💻 Program Dengan Input Plaintext

def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    # Memastikan teks yang diproses adalah huruf kapital agar sesuai dengan aturan
    for char in plaintext.upper():
        # Memeriksa apakah karakter ada dalam aturan substitusi
        if char in aturan:
            # Mengganti karakter dengan nilai substitusinya
            ciphertext += aturan[char]
        else:
            # Jika tidak ada dalam aturan, karakter tetap sama
            ciphertext += char
    return ciphertext

# Aturan substitusi (sebagai dictionary)
aturan_substitusi = {
    'U': 'K',
    'N': 'N',
    'I': 'I',
    'K': 'K',
    'A': 'B'
}

# Meminta input plaintext dari pengguna dan langsung mengubahnya menjadi huruf kapital
plaintext = input("Masukkan plaintext: ").upper()

# Melakukan enkripsi
ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

# Menampilkan hasil
print(f'Plaintext: {plaintext}')
print(f'Ciphertext: {ciphertext}')