# Projek UAS

Nama : Nadhia Shafira

NIM : 312410498

Kelas : TI.24.A.5

Mata Kuliah : Bahasa Pemograman

# Daftar Link Youtube

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
* self.gamis_list = [] : Di dalam metode `__init__,` terdapat baris `self.gamis_list = []`. Ini berarti bahwa setiap kali Anda membuat objek dari kelas `Data`, atribut `gamis_list` akan diinisialisasi sebagai sebuah list kosong `([])`. `self` adalah referensi ke objek yang sedang dibuat. `self.gamis_list`, kita mendefinisikan atribut `gamis_list` yang akan menjadi bagian dari objek tersebut.
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

