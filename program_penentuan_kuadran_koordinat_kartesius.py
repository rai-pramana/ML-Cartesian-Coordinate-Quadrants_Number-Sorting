import validasi

def tentukan_kuadran(x, y):
    if x > 0 and y > 0:
        return f"Kuadran I (sudut 0° hingga 90°), karena x ({x}) dan y ({y}) bernilai positif."
    elif x < 0 and y > 0:
        return f"Kuadran II (sudut 90° hingga 180°), karena x ({x}) bernilai negatif dan y ({y}) bernilai positif."
    elif x < 0 and y < 0:
        return f"Kuadran III (sudut 180° hingga 270°), karena x ({x}) dan y ({y}) bernilai negatif."
    elif x > 0 and y < 0:
        return f"Kuadran IV (sudut 270° hingga 0° atau 360°), karena x ({x}) bernilai positif dan y ({y}) bernilai negatif."
    elif x == 0 and y == 0:
        return "Titik pusat."
    elif x == 0:
        return "Sumbu y."
    elif y == 0:
        return "Sumbu x."
    else:
        return "Tidak dapat ditentukan."

def program_penentuan_kuadran_koordinat_kartesius():
    x_input = input("Masukkan nilai x: ")
    x = validasi.validasi_input(x_input)
    while x is None:
        x_input = input("Masukkan nilai x: ")
        x = validasi.validasi_input(x_input)

    y_input = input("\nMasukkan nilai y: ")
    y = validasi.validasi_input(y_input)
    while y is None:
        y_input = input("Masukkan nilai y: ")
        y = validasi.validasi_input(y_input)

    print(f"\nTitik ({x}, {y}) berada di: {tentukan_kuadran(x, y)}")
