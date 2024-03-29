import program_penentuan_kuadran_koordinat_kartesius
import program_pengurutan_bilangan
import os

def main():
    while True:
        print("Tugas Machine Learning - Program Python untuk Menentukan Kuadran Koordinat Kartesius dan Pengurutan Bilangan")
        print("[1] Program Penentuan Kuadran Koordinat Kartesius")
        print("[2] Program Pengurutan Bilangan")
        print("[3] Keluar Program")
        pilihan = input("Silakan pilih (1-3): ")

        os.system('cls')

        if pilihan == '1':
            program_penentuan_kuadran_koordinat_kartesius.program_penentuan_kuadran_koordinat_kartesius()
        elif pilihan == '2':
            program_pengurutan_bilangan.program_pengurutan_bilangan()
        elif pilihan == '3':
            print("Terima kasih telah menggunakan program.")
            break
        else:
            print("Pilihan tidak valid. Silakan masukkan '1', '2', atau '3'.\n")
            continue

        while True:
            ulangi = input("\nApakah Anda ingin mengulang program? (y/n): ").lower()
            if ulangi == 'y':
                os.system('cls')
                break
            elif ulangi == 'n':
                os.system('cls')
                print("Terima kasih telah menggunakan program.")
                return  # Menghentikan eksekusi fungsi main() dan keluar dari program
            else:
                print("\nInput tidak valid. Silakan masukkan 'y' atau 'n'.")

if __name__ == "__main__":
    main()
