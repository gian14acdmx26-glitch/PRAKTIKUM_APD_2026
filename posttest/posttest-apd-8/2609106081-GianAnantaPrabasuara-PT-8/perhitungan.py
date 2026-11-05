from data import counter


def buat_id_konser():
    counter["konser"] += 1
    return counter["konser"]


def buat_id_transaksi():
    counter["transaksi"] += 1
    return counter["transaksi"]


def hitung_total(jumlah, harga):
    return jumlah * harga
