# Study kasus == Pendaftaran Mahasiswa Baru ==

print('====== PENDAFTARAN MAHASISWA BARU ======')

# Daftar harga kuliah 
harga_kuliah = {
    'SI': {'Nama Prodi': 'Sistem Informasi', 'Harga':2400000},
    'SIA': {'Nama Prodi': 'Sistem Informasi Akuntansi', 'Harga':2000000}
}

#Input data calon Mahasiswa
nis = input('NIS: ')
nama = input('Nama: ')

#Memilih jurusan 
print('Pilihan Jurusan: ')
for kode_jurusan, info_kuliah in harga_kuliah.items():
    print(f"{kode_jurusan} - {info_kuliah['Nama Prodi']}' (Harga: Rp{info_kuliah['Harga']}")

    kode_jurusan = input('Kode Jurusan: ')

    # Memeriksa apakah kode jurusan Valid
    if kode_jurusan not in harga_kuliah:
     print('Kode jurusan tidak valid, ')
    else :
       harga_kuliah_prodi = harga_kuliah[kode_jurusan]['Harga']

       # Menghitung total biaya kuliah
       total_bayar = harga_kuliah_prodi

       # Menampilkan Output
       print('\n Layar Keluaran')
       print('PENDATARAN MAHASISWA BARU')
       print("_" * 50)
       print('{:<4}{:<8}{:<15}{:<6}{:<10}'.format("No.", "NIS", "Nama", "Jurusan", "Biaya kuliah"))
       print('{:<4}{:<8}{:<15}{:<6}{:<10}'.format(1, nis, nama, harga_kuliah[kode_jurusan]['Nama Prodi'],f"{harga_kuliah_prodi}"))
       print("_" * 50)
       print('Total Bayar: Rp', total_bayar)
