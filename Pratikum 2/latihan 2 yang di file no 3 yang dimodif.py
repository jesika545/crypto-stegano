# Meminta input dari pengguna
x = int(input("Masukkan nilai x: "))
y = int(input("Masukkan nilai y: "))
z = int(input("Masukkan nilai z: "))

# Mengecek apakah x berada di antara 18 dan 30
if x >= 18 and x <= 30:
    print("x berada di antara 18 dan 30")
else:
    print("x tidak berada di antara 18 dan 30")

# Mengecek apakah y berada di luar rentang 10 hingga 20
if y < 10 or y > 20:
    print("y berada di luar rentang 10 hingga 20")
else:
    print("y berada di dalam rentang 10 hingga 20")

# Mengecek apakah z sama dengan 5
if z == 5:
    print("z sama dengan 5")
else:
    print("z tidak sama dengan 5")

# Mengecek apakah x tidak sama dengan y
if x != y:
    print("x tidak sama dengan y")
else:
    print("x sama dengan y")

# Mengecek apakah x lebih besar dari y
if x > y:
    print("x lebih besar dari y")
else:
    print("x tidak lebih besar dari y")

# Mengecek apakah z lebih kecil dari y
if z < y:
    print("z lebih kecil dari y")
else:
    print("z tidak lebih kecil dari y")

# Mengecek kombinasi kondisi untuk y dan z
if y >= 15 and z <= 5:
    print("y lebih besar atau sama dengan 15, dan z lebih kecil atau sama dengan 5")
else:
    print("Kondisi untuk y dan z tidak terpenuhi")
