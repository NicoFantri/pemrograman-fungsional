# Dictionary untuk menyimpan data pengguna
users = {
    "admin": {"password": "1234", "full_name": "Admin User"}  # Contoh pengguna yang terdaftar
}

# Fungsi untuk mengubah profil
def profile_settings(username):
    print("\n--- Profile Settings ---")
    if username is None:
        print("Anda belum login.\n")  # Pesan jika pengguna belum login
        return
    full_name = input("Masukkan nama lengkap baru: ")  # Meminta input nama lengkap baru
    users[username]["full_name"] = full_name  # Memperbarui nama lengkap pengguna di dictionary
    print("Profil berhasil diperbarui!\n")  # Konfirmasi bahwa profil berhasil diperbarui

# Fungsi utama
def main():
    current_user = "admin"  # Contoh pengguna yang sudah login
    while True:
        print("=== Menu Profile ===")
        print("1. Ubah Nama Lengkap")
        print("2. Keluar")

        choice = input("Pilih menu: ")

        if choice == "1":
            profile_settings(current_user)  # Memanggil fungsi untuk mengubah profil
        elif choice == "2":
            print("Terima kasih telah menggunakan program ini.")
            break  # Keluar dari loop dan program
        else:
            print("Pilihan tidak valid, coba lagi.\n")  # Pesan jika pilihan tidak valid

if __name__ == "__main__":
    main()
