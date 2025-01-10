class Process:
    def __init__(self, data):
        self.data = data

    def hitung_total(self):
        total_harga = sum(gamis['harga'] for gamis in self.data.get_gamis())
        return total_harga

    def proses_pembelian(self):
        while True:
            nama_gamis = input("Masukkan nama gamis (atau ketik 'selesai' untuk mengakhiri): ")
            if nama_gamis.lower() == 'selesai':
                break
            harga_gamis = int(input("Masukkan harga gamis: "))
            self.data.tambah_gamis(nama_gamis, harga_gamis)