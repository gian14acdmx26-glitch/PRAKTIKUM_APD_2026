from datetime import datetime
from data import data_konser, data_transaksi
from validasi import input_angka
from perhitungan import buat_id_transaksi, hitung_total
from tampilan import (bersihkan_layar, jeda, tampilkan_konser, tampilkan_riwayat,
                      tampilkan_detail_pembelian, tampilkan_menu,
                      pesan_sukses, pesan_error, pesan_info)


def beli_tiket(username):
    tampilkan_konser()
    try:
        id_beli = int(input("Masukkan ID konser: "))
        konser = data_konser[id_beli]
    except ValueError:
        pesan_error("ID harus berupa angka.")
        return
    except KeyError:
        pesan_error("ID konser tidak ditemukan.")
        return

    if konser["stok"] <= 0:
        pesan_error("Tiket sudah habis.")
        return

    jumlah = input_angka("Jumlah tiket: ", 1)
    if jumlah > konser["stok"]:
        pesan_error("Stok tiket tidak mencukupi.")
        return

    total = hitung_total(jumlah, konser["harga"])
    tampilkan_detail_pembelian(konser["nama"], jumlah, konser["harga"], total)
    konfirmasi = input("Konfirmasi pembelian? (y/n): ")
    if konfirmasi.lower() == "y":
        konser["stok"] -= jumlah
        data_transaksi[buat_id_transaksi()] = {
            "username": username,
            "konser": konser["nama"],
            "jumlah": jumlah,
            "total": total,
            "waktu": datetime.now().strftime("%d/%m/%Y %H:%M"),
        }
        pesan_sukses("Pembelian berhasil.")
    else:
        pesan_info("Pembelian dibatalkan.")


def menu_pengguna(username):
    while True:
        bersihkan_layar()
        tampilkan_menu("MENU PENGGUNA | " + username, [
            "Lihat Daftar Konser", "Beli Tiket", "Riwayat Transaksi", "Logout",
        ])
        pilihan = input("Pilih menu: ")
        if pilihan == "1":
            tampilkan_konser()
        elif pilihan == "2":
            beli_tiket(username)
        elif pilihan == "3":
            tampilkan_riwayat(username)
        elif pilihan == "4":
            pesan_sukses("Logout berhasil.")
            break
        else:
            pesan_error("Pilihan tidak tersedia.")
        jeda()
