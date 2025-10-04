# Program Penentuan Kuadran Koordinat Kartesius dan Program Pengurutan Bilangan

![Python](https://img.shields.io/badge/Python-3.x-blue.svg)
![License](https://img.shields.io/badge/License-MIT-green.svg)
![Status](https://img.shields.io/badge/Status-Complete-brightgreen.svg)

## 📋 Informasi Project

-   **Nama**: I Kadek Rai Pramana
-   **NIM**: 2105551094
-   **Mata Kuliah**: Machine Learning (C)
-   **Dosen Pengampu**: Gusti Made Arya Sasmita, ST., MT.
-   **Tanggal**: 28 Maret 2024
-   **Versi**: 1.0

## 📝 Deskripsi

Project ini merupakan program Python yang terdiri dari dua fitur utama:

1. **Program Penentuan Kuadran Koordinat Kartesius** - Menentukan kuadran dari titik koordinat (x,y) pada sistem koordinat kartesius
2. **Program Pengurutan Bilangan** - Mengurutkan sekumpulan bilangan menggunakan algoritma Bubble Sort

## ✨ Fitur

### 🔍 Program Penentuan Kuadran Koordinat Kartesius

-   Menentukan kuadran I, II, III, atau IV berdasarkan koordinat (x,y)
-   Mendeteksi posisi khusus (titik pusat, sumbu x, sumbu y)
-   Validasi input untuk memastikan nilai yang dimasukkan adalah angka
-   Penjelasan detail mengapa titik berada di kuadran tertentu

### 📊 Program Pengurutan Bilangan

-   Implementasi algoritma Bubble Sort
-   Pilihan urutan: Ascending (naik) atau Descending (turun)
-   Opsi menggunakan data default atau input manual
-   Menampilkan data sebelum dan sesudah pengurutan
-   Validasi input untuk memastikan semua data adalah angka

## 🚀 Cara Menjalankan

### Prerequisites

-   Python 3.x terinstall di sistem

### Langkah-langkah

1. **Clone atau download repository**

    ```bash
    git clone https://github.com/rai-pramana/ML-Cartesian-Coordinate-Quadrants_Number-Sorting.git
    cd ML-Cartesian-Coordinate-Quadrants_Number-Sorting
    ```

2. **Jalankan program utama**

    ```bash
    python main.py
    ```

3. **Pilih menu yang diinginkan**
    - Ketik `1` untuk Program Penentuan Kuadran Koordinat Kartesius
    - Ketik `2` untuk Program Pengurutan Bilangan
    - Ketik `3` untuk keluar dari program

## 📖 Panduan Penggunaan

### Program Penentuan Kuadran Koordinat Kartesius

1. Pilih menu `[1]` dari menu utama
2. Masukkan nilai x (koordinat horizontal)
3. Masukkan nilai y (koordinat vertikal)
4. Program akan menampilkan kuadran tempat titik tersebut berada

**Contoh:**

```
Masukkan nilai x: 3
Masukkan nilai y: 4

Titik (3.0, 4.0) berada di: Kuadran I (sudut 0° hingga 90°), karena x (3.0) dan y (4.0) bernilai positif.
```

### Program Pengurutan Bilangan

1. Pilih menu `[2]` dari menu utama
2. Pilih sumber data:
    - `[1]` Menggunakan data default: (5, 2, 9, 3, 8, 4)
    - `[2]` Memasukkan data sendiri (pisahkan dengan spasi)
3. Pilih urutan pengurutan:
    - `[1]` Descending (besar ke kecil)
    - `[2]` Ascending (kecil ke besar)
4. Program akan menampilkan data awal dan hasil pengurutan

**Contoh:**

```
Data awal: [5, 2, 9, 3, 8, 4]
Hasil pengurutan secara descending: [9, 8, 5, 4, 3, 2]
```

## 🗂️ Struktur File

```
ML-Cartesian-Coordinate-Quadrants_Number-Sorting/
│
├── main.py                                        # File utama untuk menjalankan program
├── program_penentuan_kuadran_koordinat_kartesius.py # Modul penentuan kuadran
├── program_pengurutan_bilangan.py                 # Modul pengurutan bilangan
├── validasi.py                                     # Modul validasi input
└── README.md                                       # Dokumentasi project
```

## 🧮 Algoritma dan Logika

### Penentuan Kuadran Koordinat Kartesius

Kuadran ditentukan berdasarkan tanda nilai x dan y:

| Kuadran | Kondisi x   | Kondisi y   | Sudut       |
| ------- | ----------- | ----------- | ----------- |
| I       | Positif (+) | Positif (+) | 0° - 90°    |
| II      | Negatif (-) | Positif (+) | 90° - 180°  |
| III     | Negatif (-) | Negatif (-) | 180° - 270° |
| IV      | Positif (+) | Negatif (-) | 270° - 360° |

**Kasus Khusus:**

-   x = 0, y = 0: Titik pusat
-   x = 0, y ≠ 0: Sumbu y
-   x ≠ 0, y = 0: Sumbu x

### Algoritma Bubble Sort

Bubble Sort adalah algoritma pengurutan sederhana yang bekerja dengan:

1. Membandingkan elemen bersebelahan dalam array
2. Menukar posisi jika tidak sesuai urutan yang diinginkan
3. Mengulangi proses hingga tidak ada lagi pertukaran yang diperlukan

**Kompleksitas Waktu:** O(n²)

## 🔧 Validasi Input

Program dilengkapi dengan sistem validasi yang:

-   Memastikan input berupa angka (integer atau float)
-   Memberikan pesan error yang jelas jika input tidak valid
-   Meminta input ulang hingga valid

## 🎯 Tujuan Pembelajaran

Project ini bertujuan untuk:

1. Memahami konsep sistem koordinat kartesius
2. Implementasi algoritma pengurutan sederhana
3. Praktik modularisasi kode Python
4. Penerapan validasi input dan error handling
5. Pengembangan interface console yang user-friendly

## 📞 Kontak

-   **Developer**: I Kadek Rai Pramana
-   **GitHub**: [rai-pramana](https://github.com/rai-pramana)

## 📄 Lisensi

Project ini menggunakan lisensi MIT. Silakan lihat file `LICENSE` untuk detail lebih lanjut.

---

_Dibuat sebagai tugas mata kuliah Machine Learning - Universitas [Nama Universitas]_
