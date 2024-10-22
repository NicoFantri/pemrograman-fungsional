# Data penginapan dengan nama customer berupa pemain bola Real Madrid tahun 2017
data_penginapan = [
    {"room_id": "RM101", "cust_name": "Cristiano Ronaldo", "expenses": 250000, "jumlah_hari": 3, "tanggal": "2024-10-01"},
    {"room_id": "RM102", "cust_name": "Sergio Ramos", "expenses": 230000, "jumlah_hari": 2, "tanggal": "2024-10-01"},
    {"room_id": "RM103", "cust_name": "Luka Modric", "expenses": 200000, "jumlah_hari": 4, "tanggal": "2024-10-01"},
    {"room_id": "RM104", "cust_name": "Karim Benzema", "expenses": 240000, "jumlah_hari": 1, "tanggal": "2024-10-01"},
    
    {"room_id": "RM201", "cust_name": "Toni Kroos", "expenses": 220000, "jumlah_hari": 2, "tanggal": "2024-09-25"},
    {"room_id": "RM202", "cust_name": "Marcelo", "expenses": 215000, "jumlah_hari": 3, "tanggal": "2024-09-25"},
    {"room_id": "RM203", "cust_name": "Keylor Navas", "expenses": 210000, "jumlah_hari": 1, "tanggal": "2024-09-25"},
    {"room_id": "RM204", "cust_name": "Isco", "expenses": 225000, "jumlah_hari": 4, "tanggal": "2024-09-25"},
    
    {"room_id": "RM301", "cust_name": "Raphael Varane", "expenses": 205000, "jumlah_hari": 3, "tanggal": "2024-09-15"},
    {"room_id": "RM302", "cust_name": "Casemiro", "expenses": 190000, "jumlah_hari": 2, "tanggal": "2024-09-15"},
    {"room_id": "RM303", "cust_name": "Mateo Kovacic", "expenses": 185000, "jumlah_hari": 4, "tanggal": "2024-09-15"},
    {"room_id": "RM304", "cust_name": "Nacho Fernandez", "expenses": 195000, "jumlah_hari": 1, "tanggal": "2024-09-15"}
]

# Fungsi untuk mencari customer berdasarkan nama dan menghitung total tagihan (pure function)
def cari_customer(data_penginapan, nama_customer):
    hasil = [customer for customer in data_penginapan if customer["cust_name"].lower() == nama_customer.lower()]
    if hasil:
        total_tagihan = sum(customer["expenses"] for customer in hasil)
        return hasil, f"Total yang harus dibayar: Rp {total_tagihan}"
    else:
        return None, f"Maaf, customer bernama '{nama_customer}' tidak ditemukan dalam sistem."

# Fungsi untuk menjalankan proses pencarian customer (non-pure function untuk interaksi I/O)
def menu_cari_customer(data_penginapan):
    while True:
        try:
            nama_customer = input("Masukkan nama customer: ")
            customer_info, pesan = cari_customer(data_penginapan, nama_customer)

            if customer_info:
                for info in customer_info:
                    print(f"\nDetail Reservasi Pelanggan:")
                    print(f"Nomor Kamar    : {info['room_id']}")
                    print(f"Nama Pelanggan : {info['cust_name']}")
                    print(f"Total Biaya    : Rp {info['expenses']}")
                    print(f"Jumlah Hari    : {info['jumlah_hari']} hari")
                    print(f"Tanggal Masuk  : {info['tanggal']}")
                    print(f"{pesan}\n")
                    print("===========================")
            else:
                print(f"\n{pesan}\n")

            pilihan = input("Cari customer lain? (y/n): ").lower()
            if pilihan != 'y':
                break
        except Exception as e:
            print(f"Terjadi kesalahan: {e}")

# Fungsi login (pure function)
def login(data_pengguna, nim, password):
    if nim in data_pengguna and data_pengguna[nim]["password"] == password:
        return nim, data_pengguna[nim]["role"]
    return None, None

# Fungsi menu admin (non-pure function untuk interaksi I/O)
def menu_admin(data_penginapan):
    while True:
        print("\nMenu Admin:")
        print("1. Tambah Data Penginapan")
        print("2. Cari Data Customer")
        print("3. Keluar")

        pilihan = input("Pilih menu admin (1/2/3): ")

        if pilihan == "1":
            room_id = input("Masukkan Nomor Kamar: ")
            customer_name = input("Masukkan Nama Customer: ")
            try:
                expenses = int(input("Masukkan Jumlah Biaya: Rp "))
                jumlah_hari = int(input("Masukkan Jumlah Hari: "))
                tanggal_menginap = input("Masukkan Tanggal Menginap (YYYY-MM-DD): ")

                data_penginapan.append({
                    "room_id": room_id,
                    "cust_name": customer_name,
                    "expenses": expenses,
                    "jumlah_hari": jumlah_hari,
                    "tanggal": tanggal_menginap
                })
                print("\nData Penginapan Berhasil Ditambahkan.")
            except ValueError:
                print("Masukkan biaya dan jumlah hari dengan benar.")
        elif pilihan == "2":
            menu_cari_customer(data_penginapan)
        elif pilihan == "3":
            break
        else:
            print("Pilihan tidak valid. Silakan coba lagi.")

# Fungsi menu utama (non-pure function untuk interaksi I/O)
def menu_utama(data_penginapan, data_pengguna):
    while True:
        print("\nMenu Utama:")
        print("1. Login")
        print("2. Keluar")

        pilihan = input("Pilih menu (1/2): ")

        if pilihan == "1":
            nim = input("Masukkan Username: ")
            password = input("Masukkan Password: ")
            nim, role = login(data_pengguna, nim, password)
            if nim:
                if role == "admin":
                    menu_admin(data_penginapan)
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

# Memulai program
menu_utama(data_penginapan, data_pengguna)
