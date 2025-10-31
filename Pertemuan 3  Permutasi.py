import itertools
import math

# ==========================
# 1. PERMUTASI MENYELURUH
# ==========================
def permutasi_menyeluruh(arr):
    return list(itertools.permutations(arr))

# ==========================
# 2. PERMUTASI SEBAGIAN
# ==========================
def permutasi_sebagian(arr, k):
    return list(itertools.permutations(arr, k))

# ==========================
# 3. PERMUTASI KELILING
# ==========================
def permutasi_keliling(arr):
    if len(arr) <= 1:
        return [arr]
    pertama = arr[0]
    permutasi_penuh = list(itertools.permutations(arr[1:]))
    return [[pertama] + list(perm) for perm in permutasi_penuh]

# ==========================
# 4. PERMUTASI BERKELOMPOK
# ==========================
def permutasi_berkelompok(grup):
    hasil = [[]]
    for kelompok in grup:
        hasil_baru = []
        for hsl in hasil:
            for perm in itertools.permutations(kelompok):
                hasil_baru.append(hsl + list(perm))
        hasil = hasil_baru
    return hasil

# ==========================
# 5. MENGHITUNG CARA MENGATUR n BUKU DI r RAK
# ==========================
def hitung_buku_dan_rak(n, r):
    total = r ** n  # Setiap buku bisa ditempatkan di salah satu dari r rak
    print(f"Ada {total} cara untuk mengatur {n} buku di {r} rak.")
    return total


# ==========================
# MENU UTAMA
# ==========================
def main():
    while True:
        print("\n=== PROGRAM PERMUTASI PYTHON ===")
        print("1. Permutasi Menyeluruh")
        print("2. Permutasi Sebagian")
        print("3. Permutasi Keliling")
        print("4. Permutasi Berkelompok")
        print("5. Hitung Cara Menyusun Buku di Rak")
        print("6. Keluar")

        pilihan = input("Pilih menu (1-6): ")
        print()

        if pilihan == "1":
            data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
            hasil = permutasi_menyeluruh(data)
            print("\nHasil Permutasi Menyeluruh:")
            for p in hasil:
                print(p)
            print(f"\nTotal: {len(hasil)} permutasi.")

        elif pilihan == "2":
            data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
            k = int(input("Masukkan jumlah elemen yang diambil (k): "))
            hasil = permutasi_sebagian(data, k)
            print("\nHasil Permutasi Sebagian:")
            for p in hasil:
                print(p)
            print(f"\nTotal: {len(hasil)} permutasi.")

        elif pilihan == "3":
            data = input("Masukkan elemen (pisahkan dengan spasi): ").split()
            hasil = permutasi_keliling(data)
            print("\nHasil Permutasi Keliling:")
            for p in hasil:
                print(p)
            print(f"\nTotal: {len(hasil)} permutasi.")

        elif pilihan == "4":
            jumlah = int(input("Masukkan jumlah kelompok: "))
            grup = []
            for i in range(jumlah):
                data = input(f"Masukkan elemen untuk kelompok {i+1} (pisahkan spasi): ").split()
                grup.append(data)
            hasil = permutasi_berkelompok(grup)
            print("\nHasil Permutasi Berkelompok:")
            for p in hasil:
                print(p)
            print(f"\nTotal: {len(hasil)} permutasi.")

        elif pilihan == "5":
            n = int(input("Masukkan jumlah buku (n): "))
            r = int(input("Masukkan jumlah rak (r): "))
            hitung_buku_dan_rak(n, r)

        elif pilihan == "6":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")


# Jalankan program
main()
