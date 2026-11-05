from data import data_konser
from validasi import input_angka, input_teks
from perhitungan import buat_id_konser
from tampilan import (bersihkan_layar, jeda, tampilkan_konser, tampilkan_menu,
                      pesan_sukses, pesan_error)


def tambah_konser():
    nama = input_teks("Nama konser: ")
    kota = input_teks("Kota konser: ")
    harga = input_angka("Harga tiket: ")
    stok = input_angka("Jumlah tiket: ")
    id_baru = buat_id_konser()
    data_konser[id_baru] = {"nama": nama, "kota": kota, "harga": harga, "stok": stok}
    pesan_sukses("Konser berhasil ditambahkan.")


def ubah_konser():
    tampilkan_konser()
    try:
        id_edit = int(input("Masukkan ID konser yang diubah: "))
        if id_edit not in data_konser:
            raise KeyError(id_edit)
    except ValueError:
        pesan_error("ID harus berupa angka.")
        return
    except KeyError:
        pesan_error("ID konser tidak ditemukan.")
        return
    nama = input_teks("Nama konser baru: ")
    kota = input_teks("Kota baru: ")
    harga = input_angka("Harga baru: ")
    stok = input_angka("Stok baru: ")
    data_konser[id_edit] = {"nama": nama, "kota": kota, "harga": harga, "stok": stok}
    pesan_sukses("Data konser berhasil diubah.")


def hapus_konser():
    tampilkan_konser()
    try:
        id_hapus = int(input("Masukkan ID konser yang dihapus: "))
        del data_konser[id_hapus]
        pesan_sukses("Konser berhasil dihapus.")
    except ValueError:
        pesan_error("ID harus berupa angka.")
    except KeyError:
        pesan_error("ID konser tidak ditemukan.")


def menu_admin():
    while True:
        bersihkan_layar()
        tampilkan_menu("MENU ADMIN", [
            "Lihat Data Konser", "Tambah Konser", "Ubah Data Konser",
            "Hapus Konser", "Logout",
        ])
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tampilkan_konser()
        elif pilihan == "2":
            tambah_konser()
        elif pilihan == "3":
            ubah_konser()
        elif pilihan == "4":
            hapus_konser()
        elif pilihan == "5":
            pesan_sukses("Logout berhasil.")
            break
        else:
            pesan_error("Pilihan tidak tersedia.")
        jeda()
