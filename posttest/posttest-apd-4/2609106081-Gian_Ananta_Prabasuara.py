USERNAME_BENAR = "giann"
PIN_BENAR = "081"
MAX_PERCOBAAN = 3

login_berhasil = False

for percobaan in range(MAX_PERCOBAAN):
    print("=== LOGIN ATM ===")
    username = input("Username : ")
    pin = input("PIN      : ")

    if username == USERNAME_BENAR and pin == PIN_BENAR:
        print("Login Berhasil!\n")
        login_berhasil = True
        break

    sisa = MAX_PERCOBAAN - (percobaan + 1)
    print(f"Login Gagal! Sisa percobaan: {sisa}\n")

if not login_berhasil:
    print("Akun Anda Terblokir!")
    exit()

saldo = 1000000
lanjut = "ya"

while lanjut == "ya":
    print("=== MENU ATM ===")
    print("[1] Cek Saldo")
    print("[2] Tarik Tunai")
    print("[3] Setor Tunai")
    print("[4] Keluar")
    pilihan = input("Pilih menu (1-4): ")

    if pilihan not in ["1", "2", "3", "4"]:
        print("Pilihan tidak valid, pilih 1-4.\n")
        continue

    if pilihan == "1":
        print(f"\nSaldo Anda saat ini: Rp{saldo}\n")

    elif pilihan == "2":
        nominal = int(input("Masukkan nominal penarikan: Rp"))
        if nominal % 50000 != 0:
            print("\nNominal harus kelipatan 50.000!\n")
            continue
        saldo -= nominal
        print(f"\nNominal ditarik : Rp{nominal}")
        print(f"Sisa saldo      : Rp{saldo}\n")

    elif pilihan == "3":
        nominal = int(input("Masukkan nominal setoran: Rp"))
        if nominal % 50000 != 0:
            print("\nNominal harus kelipatan 50.000!\n")
            continue
        saldo += nominal
        print(f"\nNominal disetor : Rp{nominal}")
        print(f"Total saldo     : Rp{saldo}\n")

    elif pilihan == "4":
        print("\nTerima kasih telah menggunakan layanan ATM kami!")
        lanjut = "tidak"