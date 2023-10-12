# Tugas 1 If Else operator 

print('============ PROGRAM HITUNG GAJI KARYAWAN ====================')
print('============ GAJI KARYAWAN PT.DINGIN DAMAI ===================')
# Input
nama_karyawan = input("Nama Karyawan: ")
golongan_jabatan = int(input("Golongan Jabatan (1/2/3): "))
pendidikan = input("Pendidikan (SMA/D1/D3/S1): ")
jumlah_jam_kerja = int(input("Jumlah jam kerja: "))

# Gaji pokok per bulan
gaji_pokok = 300000 

# Tunjangan Jabatan
if golongan_jabatan == 1:
    tunjangan_jabatan = 0.05 * gaji_pokok
elif golongan_jabatan == 2:
    tunjangan_jabatan = 0.10 * gaji_pokok
elif golongan_jabatan == 3:
    tunjangan_jabatan = 0.15 * gaji_pokok
else:
    tunjangan_jabatan = 0

# Tunjangan Pendidikan
if pendidikan == "SMA":
    tunjangan_pendidikan = 0.025 * gaji_pokok
elif pendidikan == "D1":
    tunjangan_pendidikan = 0.05 * gaji_pokok
elif pendidikan == "D3":
    tunjangan_pendidikan = 0.20 * gaji_pokok
elif pendidikan == "S1":
    tunjangan_pendidikan = 0.30 * gaji_pokok
else:
    tunjangan_pendidikan = 0

# Honor Lembur
jam_kerja_normal = 8
if jumlah_jam_kerja > jam_kerja_normal:
    lembur = (jumlah_jam_kerja - jam_kerja_normal) * 3500
else:
    lembur = 0

# Hitung total gaji
total_gaji = gaji_pokok + tunjangan_jabatan + tunjangan_pendidikan + lembur

# Output
print(f"Karyawan yang bernama {nama_karyawan}")
print(f"Honor yang diterima")
print(f"Tunjangan Jabatan Rp {tunjangan_jabatan}")
print(f"Tunjangan Pendidikan Rp {tunjangan_pendidikan}")
print(f"Honor Lembur Rp {lembur}")
print(f"Total Gaji Rp {total_gaji}")
