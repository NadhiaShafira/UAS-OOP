# Projek UAS

Nama : Nadhia Shafira

NIM : 312410498

Kelas : TI.24.A.5

Mata Kuliah : Bahasa Pemograman

# Daftar Link Youtube
- [video Tutorial](https://youtu.be/j4hMhmlo1qY?feature=shared)
  
## Kelas data
Kelas data adalah sebuah blueprint atau cetak biru dalam pemrograman yang digunakan untuk mendefinisikan struktur dan perilaku dari suatu objek
##  1. Konstruktor ```(__init__)```

```python
class Data:
    def __init__(self):
        self.gamis_list = [] 
```
* Konstruktor adalah metode khusus yang akan dipanggil secara otomatis saat objek
* class Data: Baris ini mendefinisikan sebuah kelas baru bernama Data. Kelas adalah cetak biru untuk membuat objek. Dalam konteks pemrograman berorientasi objek, kelas dapat dianggap sebagai template yang mendefinisikan atribut dan metode yang akan dimiliki oleh objek yang dibuat dari kelas tersebut.
* def __init__(self): `__init__` adalah metode khusus yang disebut konstruktor. Metode ini secara otomatis dipanggil ketika sebuah objek dari kelas `Data` dibuat. Tujuan dari metode ini adalah untuk menginisialisasi atribut objek.
* self.gamis_list = [] : Di dalam metode `__init__,` terdapat baris `self.gamis_list = []`. Ini berarti bahwa setiap kali Anda membuat objek dari kelas `Data`, atribut `gamis_list` akan diinisialisasi sebagai sebuah list kosong `([])`.
*  `self` adalah referensi ke objek yang sedang dibuat.
*  `self.gamis_list`, kita mendefinisikan atribut `gamis_list` yang akan menjadi bagian dari objek tersebut.
## 2. Metode `tambah_gamis`
```python
def tambah_gamis(self, nama, harga):
        self.gamis_list.append({'nama': nama, 'harga': harga})
```
* Metode ini didefinisikan dengan menggunakan kata kunci `def`, diikuti dengan nama metode `(tambah_gamis)` dan parameter yang diterima oleh metode tersebut (`self`, `nama`, dan `harga`).
## 3. Metode `get_gamis`
```python
def get_gamis(self):
        return self.gamis_list
```
* Metode ini mendefinisikan sebuah metode bernama get_gamis. Metode ini digunakan untuk mengambil (mengakses) data dari atribut gamis_list yang ada di dalam objek kelas.

## Penjelasan Kode: Kelas View
Kelas view adalah komponen dalam arsitektur MVC yang bertanggung jawab untuk menampilkan data kepada pengguna. Kelas ini berfungsi sebagai antarmuka pengguna (UI) yang menyajikan informasi dari model dan menerima input dari pengguna.

```python
class View:
    @staticmethod
    def tampilkan_pembelian(gamis_list, total_harga):
        # Membuat tabel menggunakan PrettyTable
        table = PrettyTable()
        table.field_names = ["Nama Gamis", "Harga"]

        for gamis in gamis_list:
            table.add_row([gamis['nama'], f"Rp {gamis['harga']}"])

        print("\nDaftar Gamis yang dibeli:")
        print(table)
        print(f"Total Harga: Rp {total_harga}")
```

* `gamis_list`: Parameter ini adalah sebuah daftar yang berisi informasi tentang gamis yang telah dibeli.
* `total_harga`: Parameter ini menyimpan total harga dari semua gamis yang dibeli. Nilai ini biasanya merupakan hasil penjumlahan dari harga-harga gamis yang ada dalam `gamis_list`.

* fungsi metode:

- Menampilkan Daftar Gamis yang Dibeli Secara terstruktur dan mudah dibaca.
- Format Tabel
- Menampilkan Total Harga

* Langkah-langkah:

1. Inisialisasi Tabel:
   * Membuat objek tabel baru menggunakan PrettyTable.
   * *Menetapkan nama kolom tabel menjadi "Nama Gamis" dan "Harga".
2. Iterasi Melalui Daftar Gamis:
   * Menggunakan loop untuk iterasi setiap elemen dalam `gamis_list.`
   * Untuk setiap gamis, menambahkan baris baru ke tabel dengan nama dan harga gamis yang diformat.
3. Menampilkan Informasi:
   * Mencetak judul "Daftar Gamis yang dibeli:".
   * Mencetak tabel yang berisi daftar gamis dan harga mereka.
   * Mencetak total harga dari semua gamis yang dibeli.

* Manfaat Kode
Kelas View berfungsi untuk memisahkan tanggung jawab antara tampilan (UI) dan logika bisnis dalam aplikasi.

## Kelas Process

Kelas Process bertanggung jawab untuk:

1. Mengelola proses pengambilan input data dari pengguna.
2. Menghubungkan data (kelas Data) dan tampilan (kelas View).
3. Mengorganisir alur kerja secara terstruktur.

## 1. Konstruktor `(__init__)`
```phython
def __init__(self, data):
        self.data = data
```
### Apa yang dilakukan?

* Konstruktor: Metode `__init__` adalah konstruktor yang dipanggil secara otomatis saat sebuah objek dari kelas dibuat. Ini digunakan untuk menginisialisasi atribut objek.
* Parameter data: Parameter ini menerima nilai yang diberikan saat objek dibuat. Nilai ini akan disimpan dalam atribut `self.data`.
* `self.data = data`: Baris ini menyimpan nilai parameter `data` ke dalam atribut instance `self.data`, sehingga nilai tersebut dapat diakses oleh metode lain dalam kelas.
### manfaat kelas proses

Kelas proses berfungsi untuk mengelola dan mengorganisir logika bisnis dalam aplikasi. Dengan memisahkan logika bisnis ke dalam kelas proses, kode menjadi lebih terstruktur dan mudah dipahami

## 2. Metode `hitung_total`
```python
def hitung_total(self):
        total_harga = sum(gamis['harga'] for gamis in self.data.get_gamis())
        return total_harga
```

* Fungsi Metode
Fungsi dari metode `hitung_total(self)` adalah untuk menghitung total harga dari semua gamis yang terdapat dalam data yang dikelola oleh objek tersebut

Detail Per Bagian

1. ```python
   def hitung_total(self):
   ```
Ini adalah definisi dari metode `hitung_total`. Metode ini adalah bagian dari sebuah kelas dan menerima parameter `self`, yang merujuk pada instance dari kelas tersebut. Ini memungkinkan metode untuk mengakses atribut dan metode lain dalam kelas.

2. ```python
total_harga = sum(gamis['harga'] for gamis in self.data.get_gamis())
```
 kode ini berfungsi untuk menghitung total harga dari semua gamis.

3. ```python
return total_harga
```
* `return total_harga`: Setelah menghitung `total harga`, metode ini mengembalikan nilai total_harga. Nilai ini dapat digunakan oleh bagian lain dari program untuk mengetahui total pengeluaran untuk semua gamis yang ada.

## 3. Metode `proses_pembelian`

```python
def proses_pembelian(self):
        while True:
            nama_gamis = input("Masukkan nama gamis (atau ketik 'selesai' untuk mengakhiri): ")
            if nama_gamis.lower() == 'selesai':
                break
            harga_gamis = int(input("Masukkan harga gamis: "))
            self.data.tambah_gamis(nama_gamis, harga_gamis)
```

* Fungsi Metode
metode ini memungkinkan pengguna untuk memasukkan informasi tentang gamis yang dibeli secara interaktif hingga mereka memilih untuk mengakhiri proses.

* Validasi

Validasi dalam kode` proses_pembelian(self)`dapat dilakukan untuk memastikan bahwa input yang diberikan oleh pengguna adalah valid dan sesuai dengan yang diharapkan.
1. Validasi Nama Gamis:
   * Pastikan nama gamis tidak kosong. Jika pengguna hanya menekan Enter tanpa memasukkan nama, program harus meminta input ulang.
2. Validasi Harga Gamis:
   * Pastikan harga yang dimasukkan adalah angka yang valid. Jika pengguna memasukkan nilai yang tidak dapat diubah menjadi integer (misalnya, huruf atau simbol), program harus       menangani kesalahan dan meminta input ulang.
3. Menangani Input 'selesai':
   * Pastikan bahwa ketika pengguna mengetik 'selesai', program keluar dari loop dengan benar tanpa meminta input lebih lanjut.

# Hasil Output
