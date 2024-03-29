import validasi

def bubble_sort(arr, urutan='descending'):
    arr_terurut = arr[:]  # Membuat salinan array input
    n = len(arr_terurut)
    for i in range(n):
        for j in range(0, n-i-1):
            if urutan == 'ascending':
                if arr_terurut[j] > arr_terurut[j+1]:
                    arr_terurut[j], arr_terurut[j+1] = arr_terurut[j+1], arr_terurut[j]
            elif urutan == 'descending':
                if arr_terurut[j] < arr_terurut[j+1]:
                    arr_terurut[j], arr_terurut[j+1] = arr_terurut[j+1], arr_terurut[j]
            else:
                print("Inputan tidak valid.")
                return None  # Mengembalikan None jika input tidak valid
    return arr_terurut  # Mengembalikan array yang sudah diurutkan

def input_data():
    print("Pilih data yang akan diurutkan")
    print("[1] Menggunakan nilai default (5, 2, 9, 3, 8, 4)")
    print("[2] Memasukkan data sendiri")
    data_input = input("Silahkan pilih (1-2): ")
    if data_input == '1':
        return [5, 2, 9, 3, 8, 4]
    elif data_input == '2':
        data = input("\nMasukkan bilangan yang akan diurutkan (pisahkan dengan spasi): ").split()
        data = [validasi.validasi_input(x) for x in data]
        while None in data:
            data = input("Masukkan bilangan yang akan diurutkan (pisahkan dengan spasi): ").split()
            data = [validasi.validasi_input(x) for x in data]
        return data
    else:
        print("\nPilihan tidak valid. Silakan masukkan '1' atau '2'.\n")
        return input_data()

def input_urutan():
    print("\nPilih urutan pengurutan: ")
    print("[1] Descending")
    print("[2] Ascending")
    urutan = input("Silahkan pilih (1-2): ")
    if urutan == '1':
        return 'descending'
    elif urutan == '2':
        return 'ascending'
    else:
        print("\nPilihan tidak valid. Silakan masukkan '1' atau '2'.")
        return input_urutan()

def program_pengurutan_bilangan():
    # Meminta pengguna untuk memasukkan data atau menggunakan nilai default
    data = input_data()

    # Meminta pengguna untuk memilih urutan
    urutan = input_urutan()

    # Melakukan pengurutan sesuai dengan pilihan pengguna
    data_terurut = bubble_sort(data, urutan)

    # Menampilkan data awal
    print("\nData awal:", data)

    # Menampilkan hasil pengurutan
    print(f"Hasil pengurutan secara {urutan}: {data_terurut}")
