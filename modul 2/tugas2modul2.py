# Fungsi untuk mencari customer berdasarkan nama dan menghitung total tagihan (pure function)
def cari_customer(data_pemain, nama_pemain):
    hasil = [pemain for pemain in data_pemain if pemain["name"].lower() == nama_pemain.lower()]
    if hasil:
        total_value = sum(pemain["value"] for pemain in hasil)
        return hasil, f"Total market value: € {total_value}M"
    else:
        return None, f"Maaf, pemain bernama '{nama_pemain}' tidak ditemukan dalam tim."

# Fungsi untuk menjalankan proses pencarian customer (non-pure function untuk interaksi I/O)
def menu_cari_customer(data_pemain):
    while True:
        try:
            nama_pemain = input("Masukkan nama pemain: ")
            pemain_info, pesan = cari_customer(data_pemain, nama_pemain)

            if pemain_info:
                for info in pemain_info:
                    print(f"\nDetail Pemain:")
                    print(f"Nomor Punggung : {info['number']}")
                    print(f"Nama Pemain    : {info['name']}")
                    print(f"Posisi         : {info['position']}")
                    print(f"Market Value   : € {info['value']}M")
                    print(f"Tanggal Lahir  : {info['birth_date']}")
                    print(f"{pesan}\n")
                    print("===========================")
            else:
                print(f"\n{pesan}\n")

            pilihan = input("Cari pemain lain? (y/n): ").lower()
            if pilihan != 'y':
                break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

# Fungsi login (pure function)
def login(data_pengguna, username, password):
    if username in data_pengguna and data_pengguna[username]["password"] == password:
        return username, data_pengguna[username]["role"]
    return None, None

# Fungsi menu admin (non-pure function untuk interaksi I/O)
def menu_admin(data_pemain):
    while True:
        print("\nMenu Admin:")
        print("1. Tambah Data Pemain")
        print("2. Cari Data Pemain")
        print("3. Keluar")

        pilihan = input("Pilih menu admin (1/2/3): ")

        if pilihan == "1":
            number = input("Masukkan Nomor Punggung: ")
            name = input("Masukkan Nama Pemain: ")
            try:
                value = int(input("Masukkan Market Value (€ juta): "))
                position = input("Masukkan Posisi: ")
                birth_date = input("Masukkan Tanggal Lahir (YYYY-MM-DD): ")

                data_pemain.append({
                    "number": number,
                    "name": name,
                    "value": value,
                    "position": position,
                    "birth_date": birth_date
                })
                print("\nData Pemain Berhasil Ditambahkan.")
            except ValueError:
                print("Masukkan market value dengan benar.")
        elif pilihan == "2":
            menu_cari_customer(data_pemain)
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi menu utama (non-pure function untuk interaksi I/O)
def menu_utama(data_pemain, data_pengguna):
    while True:
        print("\nMenu Utama:")
        print("1. Login")
        print("2. Keluar")

        pilihan = input("Pilih menu (1/2): ")

        if pilihan == "1":
            username = input("Masukkan Username: ")
            password = input("Masukkan Password: ")
            username, role = login(data_pengguna, username, password)
            if username:
                if role == "admin":
                    menu_admin(data_pemain)
            else:
                print("Login gagal. Username atau password salah.")
        elif pilihan == "2":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Data pengguna untuk login
data_pengguna = {
    "admin": {"password": "admin", "role": "admin"}
}

# Data pemain Real Madrid tahun 2017
data_pemain = [
    {"number": "7", "name": "Ronaldo", "value": 120, "position": "Forward", "birth_date": "1985-02-05"},
    {"number": "9", "name": "Karim Benzema", "value": 80, "position": "Forward", "birth_date": "1987-12-19"},
    {"number": "11", "name": "Gareth Bale", "value": 90, "position": "Forward", "birth_date": "1989-07-16"},
    {"number": "4", "name": "Sergio Ramos", "value": 60, "position": "Defender", "birth_date": "1986-03-30"},
    {"number": "1", "name": "Keylor Navas", "value": 20, "position": "Goalkeeper", "birth_date": "1986-12-15"},
    {"number": "10", "name": "Luka Modric", "value": 50, "position": "Midfielder", "birth_date": "1985-09-09"},
    {"number": "8", "name": "Toni Kroos", "value": 70, "position": "Midfielder", "birth_date": "1990-01-04"},
    {"number": "12", "name": "Marcelo", "value": 40, "position": "Defender", "birth_date": "1988-05-12"},
    {"number": "5", "name": "Raphaël Varane", "value": 55, "position": "Defender", "birth_date": "1993-04-25"},
    {"number": "6", "name": "Nacho", "value": 30, "position": "Defender", "birth_date": "1990-01-18"}
]

# Memulai program
menu_utama(data_pemain, data_pengguna)
