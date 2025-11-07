import tkinter as tk
from tkinter import ttk, messagebox


# ===============================
# Class Vigenere Cipher (OOP)
# ===============================
class VigenereCipher:
    def __init__(self, text, key):
        self.text = text.upper()
        self.key = key.upper()

    def _format_key(self):
        key_repeated = ""
        key_index = 0
        for char in self.text:
            if char.isalpha():
                key_repeated += self.key[key_index % len(self.key)]
                key_index += 1
            else:
                key_repeated += char
        return key_repeated

    def encrypt(self):
        result = ""
        key_repeated = self._format_key()
        detail = []
        for i, char in enumerate(self.text):
            if char.isalpha():
                value = (ord(char) - 65 + ord(key_repeated[i]) - 65) % 26
                encrypted_char = chr(value + 65)
                result += encrypted_char
                detail.append(f"{char} + {key_repeated[i]} = {encrypted_char}")
            else:
                result += char
        return result, "\n".join(detail)

    def decrypt(self):
        result = ""
        key_repeated = self._format_key()
        detail = []
        for i, char in enumerate(self.text):
            if char.isalpha():
                value = (ord(char) - ord(key_repeated[i]) + 26) % 26
                decrypted_char = chr(value + 65)
                result += decrypted_char
                detail.append(f"{char} - {key_repeated[i]} = {decrypted_char}")
            else:
                result += char
        return result, "\n".join(detail)


# ===============================
# Class GUI Interface (OOP)
# ===============================
class CipherApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🔐 Vigenère Cipher - Enkripsi & Deskripsi")
        self.root.geometry("700x500")
        self.root.resizable(False, False)

        self.create_widgets()

    def create_widgets(self):
        ttk.Label(self.root, text="VIGENÈRE CIPHER", font=("Helvetica", 18, "bold")).pack(pady=10)

        frame = ttk.Frame(self.root)
        frame.pack(pady=10)

        # Input teks dan key
        ttk.Label(frame, text="Masukkan Teks:").grid(row=0, column=0, sticky="w")
        self.entry_text = ttk.Entry(frame, width=50)
        self.entry_text.grid(row=0, column=1, padx=10, pady=5)

        ttk.Label(frame, text="Masukkan Kunci:").grid(row=1, column=0, sticky="w")
        self.entry_key = ttk.Entry(frame, width=50)
        self.entry_key.grid(row=1, column=1, padx=10, pady=5)

        # Tombol aksi
        ttk.Button(frame, text="🔒 Enkripsi", command=self.encrypt_text).grid(row=2, column=0, pady=10)
        ttk.Button(frame, text="🔓 Deskripsi", command=self.decrypt_text).grid(row=2, column=1, pady=10)

        # Output
        ttk.Label(self.root, text="Hasil Proses:").pack()
        self.text_output = tk.Text(self.root, height=15, width=80, wrap="word", bg="#f0f0f0")
        self.text_output.pack(pady=5)

    def encrypt_text(self):
        text = self.entry_text.get()
        key = self.entry_key.get()
        if not text or not key:
            messagebox.showwarning("Peringatan", "Harap isi teks dan kunci!")
            return
        cipher = VigenereCipher(text, key)
        result, detail = cipher.encrypt()
        self.display_output(result, detail, "ENKRIPSI")

    def decrypt_text(self):
        text = self.entry_text.get()
        key = self.entry_key.get()
        if not text or not key:
            messagebox.showwarning("Peringatan", "Harap isi teks dan kunci!")
            return
        cipher = VigenereCipher(text, key)
        result, detail = cipher.decrypt()
        self.display_output(result, detail, "DESKRIPSI")

    def display_output(self, result, detail, mode):
        self.text_output.delete("1.0", tk.END)
        self.text_output.insert(tk.END, f"=== HASIL {mode} ===\n")
        self.text_output.insert(tk.END, f"Teks Hasil: {result}\n\n")
        self.text_output.insert(tk.END, f"=== DETAIL PROSES ===\n{detail}")


# ===============================
# Main Program
# ===============================
if __name__ == "__main__":
    root = tk.Tk()
    app = CipherApp(root)
    root.mainloop()
