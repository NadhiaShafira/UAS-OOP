from Data.Data import Data
from View.View import View
from Process.Process import Process


def main():
    data = Data()
    process = Process(data)
    view = View()

    process.proses_pembelian()
    total_harga = process.hitung_total()
    view.tampilkan_pembelian(data.get_gamis(), total_harga)


if __name__ == "__main__":
    main()