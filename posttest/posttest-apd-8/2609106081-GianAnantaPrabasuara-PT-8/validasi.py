from data import data_user


def input_angka(pesan, minimal=0):
    """Meminta angka bulat >= minimal. Ulangi sampai valid."""
    while True:
        try:
            nilai = int(input(pesan))
            if nilai < minimal:
                raise ValueError
            return nilai
        except ValueError:
            print("Input harus berupa angka bulat minimal " + str(minimal) + "!")


def input_teks(pesan):
    """Meminta teks yang tidak boleh kosong."""
    while True:
        teks = input(pesan).strip()
        if teks != "":
            return teks
        print("Input tidak boleh kosong!")


def cek_username_tersedia(username):
    return username not in data_user
