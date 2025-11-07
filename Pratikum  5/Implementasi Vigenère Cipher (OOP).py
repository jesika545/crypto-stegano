# ===============================================
# Program: Implementasi Vigenere Cipher (OOP)
# Mata Kuliah: Kriptografi
# Deskripsi: Program untuk mengenkripsi dan mendekripsi teks
# menggunakan algoritma Vigenere Cipher dengan menampilkan
# proses detail setiap langkah.
# ===============================================

class VigenereCipher:
    def __init__(self, key):
        self.key = key.upper()

    def _format_key(self, text):
        """Membuat kunci agar panjangnya sama dengan teks"""
        key = self.key
        key_repeated = ""
        i = 0
        for char in text:
            if char.isalpha():
                key_repeated += key[i % len(key)]
                i += 1
            else:
                key_repeated += char
        return key_repeated

    def encrypt(self, plaintext):
        plaintext = plaintext.upper()
        key_full = self._format_key(plaintext)
        ciphertext = ""

        print("\n=== PROSES ENKRIPSI ===")
        print(f"Plaintext : {plaintext}")
        print(f"Kunci     : {self.key}")
        print(f"Kunci Full: {key_full}\n")
        print(f"{'Huruf':<10}{'Kunci':<10}{'Enkripsi':<10}")

        for p, k in zip(plaintext, key_full):
            if p.isalpha():
                p_num = ord(p) - 65
                k_num = ord(k) - 65
                c_num = (p_num + k_num) % 26
                c = chr(c_num + 65)
                ciphertext += c
                print(f"{p:<10}{k:<10}{c:<10}")
            else:
                ciphertext += p
                print(f"{p:<10}{'-':<10}{p:<10}")

        print("\nHasil Ciphertext:", ciphertext)
        return ciphertext

    def decrypt(self, ciphertext):
        ciphertext = ciphertext.upper()
        key_full = self._format_key(ciphertext)
        plaintext = ""

        print("\n=== PROSES DEKRIPSI ===")
        print(f"Ciphertext: {ciphertext}")
        print(f"Kunci     : {self.key}")
        print(f"Kunci Full: {key_full}\n")
        print(f"{'Huruf':<10}{'Kunci':<10}{'Dekripsi':<10}")

        for c, k in zip(ciphertext, key_full):
            if c.isalpha():
                c_num = ord(c) - 65
                k_num = ord(k) - 65
                p_num = (c_num - k_num) % 26
                p = chr(p_num + 65)
                plaintext += p
                print(f"{c:<10}{k:<10}{p:<10}")
            else:
                plaintext += c
                print(f"{c:<10}{'-':<10}{c:<10}")

        print("\nHasil Plaintext:", plaintext)
        return plaintext


# =================================================
# Bagian Main Program
# =================================================
if __name__ == "__main__":
    print("=== PROGRAM VIGENERE CIPHER (PBO) ===")
    key = input("Masukkan kunci (key): ")
    text = input("Masukkan teks: ")

    cipher = VigenereCipher(key)

    print("\nPilih operasi:")
    print("1. Enkripsi")
    print("2. Dekripsi")
    pilihan = input("Masukkan pilihan (1/2): ")

    if pilihan == "1":
        cipher.encrypt(text)
    elif pilihan == "2":
        cipher.decrypt(text)
    else:
        print("Pilihan tidak valid!")
