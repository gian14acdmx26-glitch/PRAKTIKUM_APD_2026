
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



def buat_id_konser():
    global id_konser_terakhir
    id_baru = id_konser_terakhir + 1      # variabel lokal
    id_konser_terakhir = id_baru
    return id_baru


def buat_id_transaksi():
    global id_transaksi_terakhir
    id_transaksi_baru = id_transaksi_terakhir + 1   # variabel lokal
    id_transaksi_terakhir = id_transaksi_baru
    return id_transaksi_baru


def hitung_total(jumlah, harga):
    total = jumlah * harga                # variabel lokal
    return total


def cek_login(username, password):
    if username in data_user and data_user[username]["password"] == password:
        peran = data_user[username]["peran"]   # variabel lokal
        return peran
    return None


def tampilkan_konser():
    print("\n=== DAFTAR KONSER ===")
    if len(data_konser) == 0:
        print("Belum ada data konser.")
        return
    for id_konser, konser in data_konser.items():   # variabel lokal
        print("ID:", id_konser, "| Nama:", konser["nama"],
              "| Kota:", konser["kota"],
              "| Harga: Rp", konser["harga"],
              "| Stok:", konser["stok"])


def tampilkan_riwayat(username):
    print("\n=== RIWAYAT TRANSAKSI ===")
    ada_transaksi = False                 # variabel lokal
    for id_transaksi, transaksi in data_transaksi.items():
        if transaksi["username"] == username:
            print("Konser:", transaksi["konser"],
                  "| Jumlah:", transaksi["jumlah"],
                  "| Total: Rp", transaksi["total"])
            ada_transaksi = True
    if not ada_transaksi:
        print("Belum ada transaksi.")


while True:
    print("\n=== SISTEM PENJUALAN TIKET KONSER LANY ===")
    print("1. Login")
    print("2. Registrasi")
    print("3. Keluar")

    pilihan = input("Pilih menu: ")

    if pilihan == "1":
        username = input("Username: ")
        password = input("Password: ")
        peran = cek_login(username, password)

        if peran is not None:
            print("\nLogin berhasil!")

            if peran == "admin":
                while True:
                    print("\n=== MENU ADMIN ===")
                    print("1. Lihat Data Konser")
                    print("2. Tambah Konser")
                    print("3. Ubah Data Konser")
                    print("4. Hapus Konser")
                    print("5. Logout")

                    menu_admin = input("Pilih menu: ")

                    if menu_admin == "1":
                        tampilkan_konser()

                    elif menu_admin == "2":
                        try:
                            nama = input("Nama konser: ")
                            kota = input("Kota konser: ")
                            harga = int(input("Harga tiket: "))
                            stok = int(input("Jumlah tiket: "))

                            if nama.strip() == "" or kota.strip() == "":
                                raise ValueError
                            if harga < 0 or stok < 0:
                                raise ValueError

                            id_konser_baru = buat_id_konser()
                            data_konser[id_konser_baru] = {
                                "nama": nama,
                                "kota": kota,
                                "harga": harga,
                                "stok": stok
                            }
                            print("Konser berhasil ditambahkan.")
                        except ValueError:
                            print("Input tidak valid. Nama dan kota tidak boleh kosong, "
                                  "harga dan stok harus berupa angka bulat tidak negatif.")

                    elif menu_admin == "3":
                        tampilkan_konser()
                        try:
                            id_edit = int(input("Masukkan ID konser yang diubah: "))
                            if id_edit not in data_konser:
                                raise KeyError(id_edit)

                            nama_baru = input("Nama konser baru: ")
                            kota_baru = input("Kota baru: ")
                            harga_baru = int(input("Harga baru: "))
                            stok_baru = int(input("Stok baru: "))

                            if nama_baru.strip() == "" or kota_baru.strip() == "":
                                raise ValueError
                            if harga_baru < 0 or stok_baru < 0:
                                raise ValueError

                            data_konser[id_edit] = {
                                "nama": nama_baru,
                                "kota": kota_baru,
                                "harga": harga_baru,
                                "stok": stok_baru
                            }
                            print("Data konser berhasil diubah.")
                        except ValueError:
                            print("Input tidak valid. Pastikan ID, harga, dan stok berupa angka "
                                  "dan nama/kota tidak kosong.")
                        except KeyError:
                            print("ID konser tidak ditemukan.")

                    elif menu_admin == "4":
                        tampilkan_konser()
                        try:
                            id_hapus = int(input("Masukkan ID konser yang dihapus: "))
                            del data_konser[id_hapus]
                            print("Konser berhasil dihapus.")
                        except ValueError:
                            print("ID harus berupa angka.")
                        except KeyError:
                            print("ID konser tidak ditemukan.")

                    elif menu_admin == "5":
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak tersedia.")

            else:
                while True:
                    print("\n=== MENU PENGGUNA ===")
                    print("1. Lihat Daftar Konser")
                    print("2. Beli Tiket")
                    print("3. Riwayat Transaksi")
                    print("4. Logout")

                    menu_user = input("Pilih menu: ")

                    if menu_user == "1":
                        tampilkan_konser()

                    elif menu_user == "2":
                        tampilkan_konser()
                        try:
                            id_beli = int(input("Masukkan ID konser: "))
                            konser = data_konser[id_beli]

                            if konser["stok"] <= 0:
                                print("Tiket sudah habis.")
                            else:
                                jumlah = int(input("Jumlah tiket: "))
                                if jumlah <= 0:
                                    raise ValueError

                                if jumlah > konser["stok"]:
                                    print("Stok tiket tidak mencukupi.")
                                else:
                                    total = hitung_total(jumlah, konser["harga"])

                                    print("Nama konser:", konser["nama"])
                                    print("Jumlah tiket:", jumlah)
                                    print("Total pembayaran: Rp", total)

                                    konfirmasi = input("Konfirmasi pembelian? (y/n): ")

                                    if konfirmasi.lower() == "y":
                                        konser["stok"] -= jumlah
                                        id_transaksi_baru = buat_id_transaksi()
                                        data_transaksi[id_transaksi_baru] = {
                                            "username": username,
                                            "konser": konser["nama"],
                                            "jumlah": jumlah,
                                            "total": total
                                        }
                                        print("Pembelian berhasil.")
                                    else:
                                        print("Pembelian dibatalkan.")
                        except ValueError:
                            print("Input tidak valid. ID dan jumlah tiket harus berupa angka bulat positif.")
                        except KeyError:
                            print("ID konser tidak ditemukan.")

                    elif menu_user == "3":
                        tampilkan_riwayat(username)

                    elif menu_user == "4":
                        print("Logout berhasil.")
                        break
                    else:
                        print("Pilihan tidak tersedia.")
        else:
            print("Username atau password salah.")

    elif pilihan == "2":
        username_baru = input("Buat username: ")
        password_baru = input("Buat password: ")

        if username_baru in data_user:
            print("Username sudah digunakan.")
        elif username_baru == "" or password_baru == "":
            print("Data tidak boleh kosong.")
        else:
            data_user[username_baru] = {"password": password_baru, "peran": "user"}
            print("Registrasi berhasil. Silakan login.")

    elif pilihan == "3":
        print("Terima kasih telah menggunakan program.")
        break
    else:
        print("Pilihan tidak tersedia.")
