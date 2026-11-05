data_konser = {
    1: {"nama": "LANY - Jakarta", "kota": "Jakarta", "harga": 850000, "stok": 100},
    2: {"nama": "LANY - Surabaya", "kota": "Surabaya", "harga": 750000, "stok": 80},
    3: {"nama": "LANY - Bali", "kota": "Bali", "harga": 900000, "stok": 60},
}

data_user = {
    "admin": {"password": "admin123", "peran": "admin"},
}

data_transaksi = {}

# Penghitung ID terakhir (dictionary agar tidak perlu 'global')
counter = {"konser": 3, "transaksi": 0}
