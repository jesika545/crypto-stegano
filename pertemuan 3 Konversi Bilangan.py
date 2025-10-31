def konversi_dari_desimal():
    desimal = int(input("Masukkan bilangan desimal: "))
    print(f"Biner        : {bin(desimal)[2:]}")
    print(f"Oktal        : {oct(desimal)[2:]}")
    print(f"Heksadesimal : {hex(desimal)[2:].upper()}")
    print()


def konversi_dari_biner():
    biner = input("Masukkan bilangan biner: ")
    try:
        desimal = int(biner, 2)
        print(f"Desimal      : {desimal}")
        print(f"Heksadesimal : {hex(desimal)[2:].upper()}")
    except ValueError:
        print("Input tidak valid! Hanya boleh berisi 0 dan 1.")
    print()


def konversi_dari_oktal():
    oktal = input("Masukkan bilangan oktal: ")
    try:
        desimal = int(oktal, 8)
        print(f"Desimal      : {desimal}")
        print(f"Biner        : {bin(desimal)[2:]}")
        print(f"Heksadesimal : {hex(desimal)[2:].upper()}")
    except ValueError:
        print("Input tidak valid! Pastikan hanya angka 0-7.")
    print()


def konversi_dari_heksadesimal():
    heksa = input("Masukkan bilangan heksadesimal: ")
    try:
        desimal = int(heksa, 16)
        print(f"Desimal : {desimal}")
        print(f"Biner   : {bin(desimal)[2:]}")
        print(f"Oktal   : {oct(desimal)[2:]}")
    except ValueError:
        print("Input tidak valid! Gunakan angka 0-9 atau huruf A-F.")
    print()


def main():
    while True:
        print("=== KONVERSI BILANGAN ===")
        print("1. Desimal ke Biner, Oktal, Heksadesimal")
        print("2. Biner ke Desimal dan Heksadesimal")
        print("3. Oktal ke Desimal, Biner, Heksadesimal")
        print("4. Heksadesimal ke Desimal, Biner, Oktal")
        print("5. Keluar")

        pilihan = input("Pilih menu (1-5): ")
        print()

        if pilihan == "1":
            konversi_dari_desimal()
        elif pilihan == "2":
            konversi_dari_biner()
        elif pilihan == "3":
            konversi_dari_oktal()
        elif pilihan == "4":
            konversi_dari_heksadesimal()
        elif pilihan == "5":
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid, coba lagi.\n")


# Jalankan program
main()
