def substitusi_cipher(plaintext, aturan):
    ciphertext = ''
    for char in plaintext:
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

# Teks yang akan di-enkripsi
plaintext = "UNIKA"

# Melakukan enkripsi
ciphertext = substitusi_cipher(plaintext, aturan_substitusi)

# Menampilkan hasil
print(f'Plaintext: {plaintext}')
print(f'Ciphertext: {ciphertext}')