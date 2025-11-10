import itertools

# Fungsi faktorial
def faktorial(x):
    if x == 0 or x == 1:
        return 1
    hasil = 1
    for i in range(2, x + 1):
        hasil *= i
    return hasil

# Fungsi kombinasi (menghitung jumlah)
def kombinasi(n, r):
    if r > n:
        return 0
    faktorial_n = faktorial(n)
    faktorial_r = faktorial(r)
    faktorial_n_r = faktorial(n - r)
    return faktorial_n // (faktorial_r * faktorial_n_r)

# Program utama
def main():
    print("=== PROGRAM KOMBINASI DENGAN HASIL ===")
    # Input data dari pengguna
    data = input("Masukkan huruf/inisial elemen (pisahkan dengan spasi): ").split()
    n = len(data)
    r = int(input("Masukkan jumlah elemen yang dipilih (r): "))

    # Hitung jumlah kombinasi
    jumlah = kombinasi(n, r)
    print(f"\nJumlah kombinasi C({n}, {r}) = {jumlah}")

    # Tampilkan semua kombinasi yang mungkin
    print("\nDaftar kombinasi yang mungkin:")
    hasil = list(itertools.combinations(data, r))
    for i, combo in enumerate(hasil, start=1):
        print(f"{i}. {combo}")

# Jalankan program
main()
