from data import data_user
from validasi import cek_username_tersedia
from tampilan import pesan_sukses, pesan_error


def cek_login(username, password):
    if username in data_user and data_user[username]["password"] == password:
        return data_user[username]["peran"]
    return None


def proses_login():
    username = input("Username: ")
    password = input("Password: ")
    peran = cek_login(username, password)
    if peran is None:
        pesan_error("Username atau password salah.")
        return None, None
    pesan_sukses("\nLogin berhasil! Selamat datang, " + username)
    return username, peran


def proses_registrasi():
    username_baru = input("Buat username: ")
    password_baru = input("Buat password: ")
    if username_baru == "" or password_baru == "":
        pesan_error("Data tidak boleh kosong.")
    elif not cek_username_tersedia(username_baru):
        pesan_error("Username sudah digunakan.")
    else:
        data_user[username_baru] = {"password": password_baru, "peran": "user"}
        pesan_sukses("Registrasi berhasil. Silakan login.")
