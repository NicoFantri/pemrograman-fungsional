def login(username_input, password_input):
    # Data user yang valid
    valid_username = "admin"  # Username yang valid
    valid_password = "1234"    # Password yang valid

    # Memeriksa username dan password
    if username_input == valid_username and password_input == valid_password:
        print("Berhasil login")  # Menampilkan pesan jika login berhasil
    else:
        print("Username atau password salah")  # Menampilkan pesan jika login gagal

# Contoh penggunaan fungsi login
username = input("Masukkan username: ")  # Meminta input username dari pengguna
password = input("Masukkan password: ")   # Meminta input password dari pengguna
login(username, password)  # Memanggil fungsi login dengan username dan password yang dimasukkan
