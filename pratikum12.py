class Mahasiswa:
    # Class attribute
    universitas = "STITEK Bontang"

    # Constructor
    def __init__(self, nama, nim, jurusan, ipk=0.0):
        self.nama = nama
        self.nim = nim
        self.jurusan = jurusan
        self.ipk = ipk

    # Method perkenalan diri
    def perkenalan_diri(self):
        return (
            f"Nama: {self.nama}\n"
            f"NIM: {self.nim}\n"
            f"Jurusan: {self.jurusan}\n"
            f"IPK: {self.ipk}\n"
            f"Universitas: {Mahasiswa.universitas}"
        )

    # Method update IPK
    def update_ipk(self, ipk_baru):
        self.ipk = ipk_baru
        return f"IPK {self.nama} berhasil diperbarui menjadi {self.ipk}"

    # Method predikat kelulusan
    def predikat_kelulusan(self):
        if self.ipk >= 3.5:
            return "Cum Laude"
        elif self.ipk >= 3.0:
            return "Sangat Memuaskan"
        elif self.ipk >= 2.5:
            return "Memuaskan"
        elif self.ipk >= 2.0:
            return "Lulus"
        else:
            return "Belum memenuhi predikat kelulusan"


# Membuat 3 object mahasiswa
mhs1 = Mahasiswa("Andi", "TI001", "Teknik Informatika", 3.75)
mhs2 = Mahasiswa("Budi", "TI002", "Teknik Informatika", 3.20)
mhs3 = Mahasiswa("Siti", "TI003", "Teknik Informatika", 2.80)


# Demonstrasi semua method
print("=== DATA MAHASISWA 1 ===")
print(mhs1.perkenalan_diri())
print("Predikat:", mhs1.predikat_kelulusan())

print("\n=== DATA MAHASISWA 2 ===")
print(mhs2.perkenalan_diri())
print("Predikat:", mhs2.predikat_kelulusan())

print("\n=== DATA MAHASISWA 3 ===")
print(mhs3.perkenalan_diri())
print("Predikat:", mhs3.predikat_kelulusan())


# Demonstrasi update IPK
print("\n=== UPDATE IPK ===")
print(mhs2.update_ipk(3.60))

print("\n=== DATA SETELAH UPDATE ===")
print(mhs2.perkenalan_diri())
print("Predikat:", mhs2.predikat_kelulusan())