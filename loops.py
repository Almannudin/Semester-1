# Tugas 2 Looping operator
print('========== GEROBAK FRIED CHICKEN =============')

# Daftar harga ayam
harga_ayam = {
    'D': {'JenisPotong': 'Dada', 'Harga': 2500},
    'P': {'JenisPotong': 'Paha', 'Harga': 2000},
    'S': {'JenisPotong': 'Sayap', 'Harga': 1500}
}

# Inisialisasi variabel total_bayar dan pajak
total_bayar = 0
pajak = 0

# Input banyak jenis yang akan dibeli
banyak_jenis = int(input("Banyak Jenis: "))

# Inisialisasi daftar transaksi
transaksi = []

# Loop untuk memproses setiap jenis ayam yang akan dibeli
for i in range(1, banyak_jenis + 1):
    print(f"Jenis Ke-{i}")
    print("Kode Potong [D/P/S]: ")
    kode_potong = input()
    
    # Memeriksa apakah kode potong valid
    if kode_potong not in harga_ayam:
        print("Kode Potong tidak valid. Coba lagi.")
        continue
    
    jenis_potong = harga_ayam[kode_potong]['JenisPotong']
    harga_satuan = harga_ayam[kode_potong]['Harga']
    
    print(f"Banyak Potong {jenis_potong}: ")
    banyak_potong = int(input())
    
    # Menghitung subtotal untuk jenis ayam saat ini
    subtotal = harga_satuan * banyak_potong
    
    # Menambahkan subtotal ke total_bayar
    total_bayar += subtotal
    
    # Menambahkan transaksi ke daftar transaksi
    transaksi.append({
        'No.': i,
        'Jenis Potong': jenis_potong,
        'Harga Satuan': harga_satuan,
        'Banyak Beli': banyak_potong,
        'Harga': subtotal
    })

# Menghitung pajak
pajak = 0.1 * total_bayar

# Menampilkan output
print("\nLayar Keluaran")
print("GEROBAK FRIED CHICKEN")
print("-" * 50)
print("{:<4} {:<10} {:<6} {:<10}".format("No.", "Jenis Potong", "Harga", "Banyak Beli"))
for trans in transaksi:
    print("{:<4} {:<10} {:<6} {:<10}".format(trans['No.'], trans['Jenis Potong'], f"Rp {trans['Harga Satuan']}", trans['Banyak Beli']))
print("-" * 50)
print("Jumlah Bayar: Rp", total_bayar)
print("Pajak 10%: Rp", pajak)
print("Total Bayar: Rp", total_bayar + pajak)
