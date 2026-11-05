from colorama import init
from tampilan import bersihkan_layar, jeda, tampilkan_menu, pesan_sukses, pesan_error
from auth import proses_login, proses_registrasi
from admin import menu_admin
from pengguna import menu_pengguna


def main():
    while True:
        bersihkan_layar()
        tampilkan_menu("SISTEM PENJUALAN TIKET KONSER LANY",
                       ["Login", "Registrasi", "Keluar"])
        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            username, peran = proses_login()
            if peran == "admin":
                jeda()
                menu_admin()
            elif peran == "user":
                jeda()
                menu_pengguna(username)
        elif pilihan == "2":
            proses_registrasi()
        elif pilihan == "3":
            pesan_sukses("Terima kasih telah menggunakan program.")
            break
        else:
            pesan_error("Pilihan tidak tersedia.")
        jeda()


if __name__ == "__main__":
    init(autoreset=True)  # colorama: warna otomatis reset & jalan di Windows
    try:
        main()
    except (KeyboardInterrupt, EOFError):
        print("\nProgram dihentikan paksa.")
