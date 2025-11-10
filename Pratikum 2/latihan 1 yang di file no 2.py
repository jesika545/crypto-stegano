import operator

ops = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv,
}

a = float(input("Masukkan nilai a: "))
b = float(input("Masukkan nilai b: "))
c = input("Masukkan operator (+, -, *, /): ")

try:
    hasil = ops[c](a, b)
    print(f"Hasil dari {a} {c} {b} = {hasil}")
except KeyError:
    print("Operator tidak valid.")
except ZeroDivisionError:
    print("Pembagian dengan nol tidak diperbolehkan.")
