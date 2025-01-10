from prettytable import PrettyTable

class Data:
    def __init__(self):
        self.gamis_list = [] 

    def tambah_gamis(self, nama, harga):
        self.gamis_list.append({'nama': nama, 'harga': harga})

    def get_gamis(self):
        return self.gamis_list
