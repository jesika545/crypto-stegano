def bin_to_decimal_steps(bstr):
    b = bstr.strip()
    steps = []
    total = 0
    n = len(b)
    for i, bit in enumerate(reversed(b)):
        val = int(bit) * (2 ** i)
        steps.append(f"{bit} × 2^{i} = {val}")
        total += val
    # build formula left-to-right
    formula = " + ".join([f"{b[j]}×2^{n-j-1}" for j in range(n)])
    full_steps = "Langkah (Biner -> Desimal):\n" + "\n".join(reversed(steps)) + f"\n\nRumus: {formula}\nTotal = {total}"
    return total, full_steps

def decimal_to_hex_steps(dec):
    if dec == 0:
        return "0", "Langkah (Desimal -> Hexa):\n0"
    simbol = "0123456789ABCDEF"
    n = dec
    steps = []
    hasil = ""
    while n > 0:
        q = n // 16
        r = n % 16
        steps.append(f"{n} ÷ 16 = {q} sisa {r} -> '{simbol[r]}'")
        hasil = simbol[r] + hasil
        n = q
    full = "Langkah (Desimal -> Hexa):\n" + "\n".join(steps) + f"\nHasil Hexa = {hasil}"
    return hasil, full

def bin_to_hex_steps(bstr):
    dec, steps_dec = bin_to_decimal_steps(bstr)
    hexa, steps_hex = decimal_to_hex_steps(dec)
    full = steps_dec + "\n\n" + steps_hex
    return hexa, full

def oct_to_decimal_steps(ostr):
    o = ostr.strip()
    steps = []
    total = 0
    n = len(o)
    for i, digit in enumerate(reversed(o)):
        val = int(digit) * (8 ** i)
        steps.append(f"{digit} × 8^{i} = {val}")
        total += val
    formula = " + ".join([f"{o[j]}×8^{n-j-1}" for j in range(n)])
    full_steps = "Langkah (Oktal -> Desimal):\n" + "\n".join(reversed(steps)) + f"\n\nRumus: {formula}\nTotal = {total}"
    return total, full_steps

def decimal_to_bin_steps(dec):
    if dec == 0:
        return "0", "Langkah (Desimal -> Biner):\n0"
    n = dec
    steps = []
    bits = ""
    while n > 0:
        q = n // 2
        r = n % 2
        steps.append(f"{n} ÷ 2 = {q} sisa {r}")
        bits = str(r) + bits
        n = q
    full = "Langkah (Desimal -> Biner):\n" + "\n".join(steps) + f"\nHasil Biner = {bits}"
    return bits, full

def oct_to_hex_steps(ostr):
    dec, step_dec = oct_to_decimal_steps(ostr)
    hexa, step_hex = decimal_to_hex_steps(dec)
    full = step_dec + "\n\n" + step_hex
    return hexa, full

def hex_to_decimal_steps(hstr):
    s = hstr.strip().upper()
    simbol = "0123456789ABCDEF"
    steps = []
    total = 0
    n = len(s)
    for i, ch in enumerate(reversed(s)):
        val_digit = simbol.index(ch)
        val = val_digit * (16 ** i)
        steps.append(f"{ch} × 16^{i} = {val} (digit value {val_digit})")
        total += val
    formula = " + ".join([f"{s[j]}×16^{n-j-1}" for j in range(n)])
    full_steps = "Langkah (Hexa -> Desimal):\n" + "\n".join(reversed(steps)) + f"\n\nRumus: {formula}\nTotal = {total}"
    return total, full_steps

def hex_to_bin_steps(hstr):
    dec, step_dec = hex_to_decimal_steps(hstr)
    bstr, step_bin = decimal_to_bin_steps(dec)
    full = step_dec + "\n\n" + step_bin
    return bstr, full

def hex_to_oct_steps(hstr):
    dec, step_dec = hex_to_decimal_steps(hstr)
    # Decimal -> Octal steps (division by 8)
    if dec == 0:
        return "0", step_dec + "\n\nLangkah (Desimal -> Oktal):\n0"
    n = dec
    steps = []
    digs = ""
    while n > 0:
        q = n // 8
        r = n % 8
        steps.append(f"{n} ÷ 8 = {q} sisa {r}")
        digs = str(r) + digs
        n = q
    full = step_dec + "\n\nLangkah (Desimal -> Oktal):\n" + "\n".join(steps) + f"\nHasil Oktal = {digs}"
    return digs, full

# Validasi helper
def is_valid_binary(s):
    return all(ch in "01" for ch in s) and s != ""

def is_valid_octal(s):
    return all(ch in "01234567" for ch in s) and s != ""

def is_valid_hex(s):
    s = s.strip()
    if s == "":
        return False
    s = s.upper()
    return all(ch in "0123456789ABCDEF" for ch in s)

# Menu sesuai permintaan dosen
def main_menu():
    while True:
        print("\n=== MENU KONVERSI ===")
        print("1) Konversi bilangan Biner ke Desimal, Hexadesimal")
        print("2) Konversi bilangan Oktal ke Desimal, Biner dan Hexadesimal")
        print("3) Konversi bilangan Hexadesimal ke Desimal, Biner dan Oktal")
        print("4) Keluar")
        pilih = input("Pilih menu (1-4): ").strip()

        if pilih == "1":
            b = input("Masukkan bilangan Biner: ").strip()
            if not is_valid_binary(b):
                print("Input tidak valid. Masukkan hanya karakter 0 dan 1.")
                continue
            # Biner -> Desimal
            dec, step_dec = bin_to_decimal_steps(b)
            print(f"\nHasil (Biner -> Desimal): {dec}")
            lihat = input("Lihat proses manual (Desimal)? (y/n): ").strip().lower()
            if lihat == "y":
                print("\n" + step_dec)

            # Biner -> Hexadesimal
            hexa, step_hex = bin_to_hex_steps(b)
            print(f"\nHasil (Biner -> Hexadesimal): {hexa}")
            lihat2 = input("Lihat proses manual (Hexa)? (y/n): ").strip().lower()
            if lihat2 == "y":
                print("\n" + step_hex)

        elif pilih == "2":
            o = input("Masukkan bilangan Oktal: ").strip()
            if not is_valid_octal(o):
                print("Input tidak valid. Oktal hanya mengandung digit 0-7.")
                continue
            # Oktal -> Desimal
            dec, step_dec = oct_to_decimal_steps(o)
            print(f"\nHasil (Oktal -> Desimal): {dec}")
            if input("Lihat proses manual (Desimal)? (y/n): ").strip().lower() == "y":
                print("\n" + step_dec)

            # Oktal -> Biner (via desimal)
            biner, step_bin = decimal_to_bin_steps(dec)
            print(f"\nHasil (Oktal -> Biner): {biner}")
            if input("Lihat proses manual (Biner)? (y/n): ").strip().lower() == "y":
                # show both: oct->dec steps + dec->bin steps for clarity
                print("\n-- Konversi Oktal -> Desimal --\n" + step_dec)
                print("\n-- Konversi Desimal -> Biner --\n" + step_bin)

            # Oktal -> Hexa (via desimal)
            hexa, step_hex = oct_to_hex_steps(o)
            print(f"\nHasil (Oktal -> Hexadesimal): {hexa}")
            if input("Lihat proses manual (Hexa)? (y/n): ").strip().lower() == "y":
                print("\n" + step_hex)

        elif pilih == "3":
            h = input("Masukkan bilangan Hexadesimal: ").strip()
            if not is_valid_hex(h):
                print("Input tidak valid. Hexa hanya mengandung 0-9 dan A-F (atau a-f).")
                continue
            # Hexa -> Desimal
            dec, step_dec = hex_to_decimal_steps(h)
            print(f"\nHasil (Hexa -> Desimal): {dec}")
            if input("Lihat proses manual (Desimal)? (y/n): ").strip().lower() == "y":
                print("\n" + step_dec)

            # Hexa -> Biner (via desimal)
            biner, step_bin = hex_to_bin_steps(h)
            print(f"\nHasil (Hexa -> Biner): {biner}")
            if input("Lihat proses manual (Biner)? (y/n): ").strip().lower() == "y":
                print("\n-- Konversi Hexa -> Desimal --\n" + step_dec)
                print("\n-- Konversi Desimal -> Biner --\n" + step_bin)

            # Hexa -> Oktal (via desimal)
            okt, step_okt = hex_to_oct_steps(h)
            print(f"\nHasil (Hexa -> Oktal): {okt}")
            if input("Lihat proses manual (Oktal)? (y/n): ").strip().lower() == "y":
                print("\n" + step_okt)

        elif pilih == "4":
            print("Selesai. Terima kasih!")
            break
        else:
            print("Pilihan tidak valid. Coba lagi.")

if __name__ == "__main__":
    main_menu()
