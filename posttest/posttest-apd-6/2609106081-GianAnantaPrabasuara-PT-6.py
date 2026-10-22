data_konser = {
    1: {"nama": "LANY - Jakarta", "kota": "Jakarta", "harga": 850000, "stok": 100},
    2: {"nama": "LANY - Surabaya", "kota": "Surabaya", "harga": 750000, "stok": 80},
    3: {"nama": "LANY - Bali", "kota": "Bali", "harga": 900000, "stok": 60}
}

data_user = {
    "admin": {"password": "admin123", "peran": "admin"}
}

data_transaksi = {}

id_konser_terakhir = 3
id_transaksi_terakhir = 0


 tampilkan_konser():
    print("\n=== DAFTAR KONSER ===")
    for id_konser, konser in data_konser.items():
        print(
            "ID:", id_konser,
            "| Nama:", konser["nama"],
            "| Kota:", konser["kota"],
            "| Harga: Rp", konser["harga"],
            "| Stok:", konser["stok"]
        )


def tambah_konser():
    global id_konser_terakhir

    nama = input("Nama konser: ")
    kota = input("Kota konser: ")
    harga = input("Harga tiket: ")
    stok = input("Jumlah tiket: ")

    if harga.isdigit() and stok.isdigit():
        id_konser_terakhir += 1
        data_konser[id_konser_terakhir] = {
            "nama": nama,
            "kota": kota,
            "harga": int(harga),
            "stok": int(stok)
        }
        print("Konser berhasil ditambahkan.")
    else:
        print("Harga dan stok harus berupa angka.")


def ubah_konser():
    tampilkan_konser()
    id_edit = input("Masukkan ID konser yang diubah: ")

    if not id_edit.isdigit():
        print("ID harus berupa angka.")
    elif int(id_edit) not in data_konser:
        print("ID konser tidak ditemukan.")
    else:
        nama_baru = input("Nama konser baru: ")
        kota_baru = input("Kota baru: ")
        harga_baru = input("Harga baru: ")
        stok_baru = input("Stok baru: ")

        if harga_baru.isdigit() and stok_baru.isdigit():
            data_konser[int(id_edit)] = {
                "nama": nama_baru,
                "kota": kota_baru,
                "harga": int(harga_baru),
                "stok": int(stok_baru)
            }
            print("Data konser berhasil diubah.")
        else:
            print("Harga dan stok harus berupa angka.")


def hapus_konser():
    tampilkan_konser()
    id_hapus = input("Masukkan ID konser yang dihapus: ")

    if not id_hapus.isdigit():
        print("ID harus berupa angka.")
    elif int(id_hapus) not in data_konser:
        print("ID konser tidak ditemukan.")
    else:
        del data_konser[int(id_hapus)]
        print("Konser berhasil dihapus.")


def beli_tiket(username):
    global id_transaksi_terakhir

    tampilkan_konser()
    id_beli = input("Masukkan ID konser: ")

    if not id_beli.isdigit():
        print("ID harus berupa angka.")
    elif int(id_beli) not in data_konser:
        print("ID konser tidak ditemukan.")
    else:
        konser = data_konser[int(id_beli)]

        if konser["stok"] <= 0:
            print("Tiket sudah habis.")
        else:
            jumlah = input("Jumlah tiket: ")

            if not (jumlah.isdigit() and int(jumlah) > 0):
                print("Jumlah tiket harus berupa angka positif.")
            elif int(jumlah) > konser["stok"]:
                print("Stok tiket tidak mencukupi.")
            else:
                total = int(jumlah) * konser["harga"]

                print("Nama konser:", konser["nama"])
                print("Jumlah tiket:", int(jumlah))
                print("Total pembayaran: Rp", total)

                konfirmasi = input("Konfirmasi pembelian? (y/n): ")

                if konfirmasi.lower() == "y":
                    konser["stok"] -= int(jumlah)

                    id_transaksi_terakhir += 1
                    data_transaksi[id_transaksi_terakhir] = {
                        "username": username,
                        "konser": konser["nama"],
                        "jumlah": int(jumlah),
                        "total": total
                    }
                    print("Pembelian berhasil.")
                else:
                    print("Pembelian dibatalkan.")


def riwayat_transaksi(username):
    print("\n=== RIWAYAT TRANSAKSI ===")
    ada_transaksi = False

    for id_transaksi, transaksi in data_transaksi.items():
        if transaksi["username"] == username:
            print(
                "Konser:", transaksi["konser"],
                "| Jumlah:", transaksi["jumlah"],
                "| Total: Rp", transaksi["total"]
            )
            ada_transaksi = True

    if not ada_transaksi:
        print("Belum ada transaksi.")


def menu_admin():
    while True:
        print("\n=== MENU ADMIN ===")
        print("1. Lihat Data Konser")
        print("2. Tambah Konser")
        print("3. Ubah Data Konser")
        print("4. Hapus Konser")
        print("5. Logout")

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
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak tersedia.")


def menu_pengguna(username):
    while True:
        print("\n=== MENU PENGGUNA ===")
        print("1. Lihat Daftar Konser")
        print("2. Beli Tiket")
        print("3. Riwayat Transaksi")
        print("4. Logout")

        pilihan = input("Pilih menu: ")

        if pilihan == "1":
            tampilkan_konser()
        elif pilihan == "2":
            beli_tiket(username)
        elif pilihan == "3":
            riwayat_transaksi(username)
        elif pilihan == "4":
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak tersedia.")


def login():
    username = input("Username: ")
    password = input("Password: ")

    if username in data_user and data_user[username]["password"] == password:
        print("\nLogin berhasil!")

        if data_user[username]["peran"] == "admin":
            menu_admin()
        else:
            menu_pengguna(username)
    else:
        print("Username atau password salah.")


def registrasi():
    username_baru = input("Buat username: ")
    password_baru = input("Buat password: ")

    if username_baru in data_user:
        print("Username sudah digunakan.")
    elif username_baru == "" or password_baru == "":
        print("Data tidak boleh kosong.")
    else:
        data_user[username_baru] = {"password": password_baru, "peran": "user"}
        print("Registrasi berhasil. Silakan login.")


while True:
    print("\n=== SISTEM PENJUALAN TIKET KONSER LANY ===")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        login()
    elif pilihan == "2":
        registrasi()
    elif pilihan == "3":
        print("Terima kasih telah menggunakan program.")
        break
    else:
        print("Pilihan tidak tersedia.")