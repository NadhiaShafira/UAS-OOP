# UAS-OOP
Nama : Nadhia Shafira

Kelas : TI.24.A5

Matkul : Bahasa Pemograman

1. Import Modul
python

from Data.Data import Data
from View.View import View
from Process.Process import Process

from Data.Data import Data: Ini mengimpor kelas Data dari modul Data. Kelas ini kemungkinan bertanggung jawab untuk mengelola data terkait produk, seperti informasi tentang gamis yang tersedia.
from View.View import View: Mengimpor kelas View, yang mungkin digunakan untuk menampilkan informasi kepada pengguna, seperti hasil pembelian dan total harga.
from Process.Process import Process: Mengimpor kelas Process, yang berisi logika bisnis untuk memproses pembelian, termasuk menghitung total harga dan mengelola transaksi.
3. Fungsi main()
python
def main():
    data = Data()
    process = Process(data)
    view = View()
data = Data(): Membuat instance baru dari kelas Data. Ini akan digunakan untuk menyimpan dan mengakses informasi produk yang diperlukan selama proses pembelian.
process = Process(data): Membuat instance dari kelas Process, dengan instance data sebagai argumen. Ini memungkinkan kelas Process untuk menggunakan data produk yang telah dimuat dalam objek data.
view = View(): Membuat instance dari kelas View, yang akan digunakan untuk menampilkan hasil kepada pengguna.
4. Memproses Pembelian
python
process.proses_pembelian()
process.proses_pembelian(): Memanggil metode proses_pembelian() dari objek process. Metode ini kemungkinan besar berisi logika untuk melakukan pembelian, seperti meminta input dari pengguna mengenai produk yang ingin dibeli, jumlahnya, dan mungkin juga memvalidasi input tersebut.
5. Menghitung Total Harga
python
total_harga = process.hitung_total()
total_harga = process.hitung_total(): Memanggil metode hitung_total() dari objek process. Metode ini bertugas untuk menghitung total harga berdasarkan produk yang dibeli. Total harga ini bisa jadi merupakan hasil penjumlahan harga semua item yang dipilih oleh pengguna.
6. Menampilkan Hasil Pembelian
python
view.tampilkan_pembelian(data.get_gamis(), total_harga)
view.tampilkan_pembelian(data.get_gamis(), total_harga): Memanggil metode tampilkan_pembelian() dari objek view. Metode ini bertugas untuk menampilkan informasi pembelian kepada pengguna.
data.get_gamis(): Memanggil metode get_gamis() dari objek data, yang kemungkinan mengembalikan daftar gamis yang dibeli atau informasi tentang gamis yang tersedia.
total_harga: Menyertakan total harga sebagai argumen, sehingga pengguna dapat melihat total biaya dari pembelian mereka.
7. Titik Masuk Program
python
if __name__ == "__main__":
    main()
Bagian ini memastikan bahwa fungsi main() hanya akan dijalankan jika file ini dieksekusi sebagai program utama, bukan saat diimpor sebagai modul dalam program lain. Ini adalah praktik umum dalam pemrograman Python untuk menjaga agar kode tetap terstruktur dengan baik.
Kesimpulan
Kode di atas adalah contoh sederhana dari aplikasi berbasis konsol yang menangani proses pembelian gamis. Dengan memanfaatkan prinsip pemrograman berorientasi objek, kode ini membagi tanggung jawab ke dalam tiga komponen utama: pengelolaan data (Data), logika bisnis (Process), dan antarmuka pengguna (View).
Untuk meningkatkan kode ini lebih lanjut, Anda bisa mempertimbangkan menambahkan fitur seperti:
Validasi input pengguna.
Penanganan kesalahan (error handling).
Penyimpanan data ke dalam file atau database.
Pengujian unit untuk memastikan setiap bagian berfungsi dengan baik.
Jika Anda memiliki pertanyaan lebih lanjut atau butuh penjelasan lebih mendalam tentang bagian tertentu dari kode, silakan beri tahu!
