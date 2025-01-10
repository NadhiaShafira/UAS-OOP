from prettytable import PrettyTable


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