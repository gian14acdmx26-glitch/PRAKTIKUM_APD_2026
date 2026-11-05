import os
from colorama import Fore
from prettytable import PrettyTable
from data import data_konser, data_transaksi


def bersihkan_layar():
    os.system("cls" if os.name == "nt" else "clear")


def jeda():
    input("\nTekan Enter untuk melanjutkan...")


def pesan_sukses(teks):
    print(Fore.GREEN + teks)


def pesan_error(teks):
    print(Fore.RED + teks)


def pesan_info(teks):
    print(Fore.YELLOW + teks)


def judul(teks):
    print(Fore.CYAN + "\n=== " + teks + " ===")


def tampilkan_konser():
    judul("DAFTAR KONSER")
    if len(data_konser) == 0:
        pesan_info("Belum ada data konser.")
        return
    tabel = PrettyTable()
    tabel.field_names = ["ID", "Nama", "Kota", "Harga (Rp)", "Stok"]
    for id_konser, konser in data_konser.items():
        tabel.add_row([id_konser, konser["nama"], konser["kota"],
                       konser["harga"], konser["stok"]])
    tabel.align["Nama"] = "l"
    tabel.align["Kota"] = "l"
    tabel.align["Harga (Rp)"] = "r"
    tabel.align["Stok"] = "r"
    print(Fore.BLUE + str(tabel))


def tampilkan_riwayat(username):
    judul("RIWAYAT TRANSAKSI")
    tabel = PrettyTable()
    tabel.field_names = ["No", "Waktu", "Konser", "Jumlah", "Total (Rp)"]
    no = 1
    for transaksi in data_transaksi.values():
        if transaksi["username"] == username:
            tabel.add_row([no, transaksi["waktu"], transaksi["konser"],
                           transaksi["jumlah"], transaksi["total"]])
            no += 1
    if no == 1:
        pesan_info("Belum ada transaksi.")
        return
    tabel.align["Konser"] = "l"
    tabel.align["Total (Rp)"] = "r"
    print(Fore.BLUE + str(tabel))


def tampilkan_detail_pembelian(nama, jumlah, harga, total):
    tabel = PrettyTable()
    tabel.field_names = ["Konser", "Jumlah", "Harga (Rp)", "Total (Rp)"]
    tabel.add_row([nama, jumlah, harga, total])
    tabel.align["Konser"] = "l"
    print(Fore.BLUE + str(tabel))


def tampilkan_menu(judul_menu, daftar):
    """daftar: list string pilihan menu, ditampilkan sebagai tabel."""
    judul(judul_menu)
    tabel = PrettyTable()
    tabel.field_names = ["No", "Menu"]
    for i, teks in enumerate(daftar, start=1):
        tabel.add_row([i, teks])
    tabel.align["Menu"] = "l"
    print(Fore.BLUE + str(tabel))
