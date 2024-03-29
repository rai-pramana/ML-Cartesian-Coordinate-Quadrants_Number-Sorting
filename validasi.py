def validasi_input(input_str):
    try:
        return float(input_str)
    except ValueError:
        print("\nPilihan tidak valid. Nilai yang dimasukkan harus berupa angka!\n")
        return None
