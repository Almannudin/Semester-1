from os import system

class ProgramStok:
    def __init__(self):
        self.d_produk = []
        self.d_harga = []
        self.d_stok = []

    def judul(self):
        print('=====================================')
        print('|  SISTEM PEMBELIAN DAN PENJUALAN STOK  |')
        print('=====================================')

    def menu(self):
        self.judul()
        print('|                                   |')
        print('|      1. Pembelian | 2. Penjualan      |')
        print('|                                   |')
        print('=====================================')
        print('*ketik 3 untuk keluar')
        print('-------------------------------------')
        menupilih = input('Pilih Menu : ')

        if menupilih == '1':
            self.pembelian()
        elif menupilih == '2':
            self.penjualan()
        elif menupilih == '3':
            exit()
        else:
            system('cls')
            self.menu()

    def pembelian(self):
        system('cls')
        self.judul()
        print('=====================================')
        print('Data Pembelian'.center(40))
        print('=====================================')

        nama_produk = input('Nama Produk: ')
        self.d_produk.append(nama_produk)

        harga_produk = float(input('Harga Produk: '))
        self.d_harga.append(harga_produk)

        stok_produk = int(input('Stok Awal: '))
        self.d_stok.append(stok_produk)

        print(f"\nData Produk '{nama_produk}' berhasil ditambahkan.")
        kembali = input('\nKembali [Enter]')
        self.menu()

    def penjualan(self):
        system('cls')
        self.judul()
        print('=====================================')
        print('Data Penjualan'.center(40))
        print('=====================================')

        if not self.d_produk:
            print('Belum ada produk yang dimasukkan. Silakan tambahkan produk terlebih dahulu.')
            kembali = input('\nKembali [Enter]')
            self.menu()

        # Menampilkan data produk
        print('\nDaftar Produk:')
        for i, produk in enumerate(self.d_produk, start=1):
            print(f"{i}. {produk} - Harga: {self.d_harga[i-1]} - Stok: {self.d_stok[i-1]}")

        # Pemilihan produk untuk penjualan
        pilihan_produk = int(input('\nPilih produk yang ingin dijual (masukkan nomor produk): '))

        if 1 <= pilihan_produk <= len(self.d_produk):
            stok_tersedia = self.d_stok[pilihan_produk - 1]
            if stok_tersedia > 0:
                jumlah_penjualan = int(input('Jumlah yang ingin dibeli: '))
                if jumlah_penjualan <= stok_tersedia:
                    total_harga = jumlah_penjualan * self.d_harga[pilihan_produk - 1]
                    self.d_stok[pilihan_produk - 1] -= jumlah_penjualan
                    print(f"\nPenjualan {self.d_produk[pilihan_produk - 1]} sebanyak {jumlah_penjualan} berhasil.")
                    print(f"Total Harga: {total_harga}")
                else:
                    print('Stok tidak mencukupi.')
            else:
                print('Stok produk habis.')
        else:
            print('Pilihan tidak valid.')

        kembali = input('\nKembali [Enter]')
        self.menu()

# Program Utama
program_stok = ProgramStok()
program_stok.menu()
