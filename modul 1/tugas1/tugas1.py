import getpass
from datetime import datetime, timedelta

# Struktur Data
users = {}  # Dictionary: {nim: (password, nama, email)}
books = []  # List of tuples: [(id, judul, penulis, jumlah)]
loans = {}  # Dictionary: {id_pinjam: (nim, id_buku, tanggal_pinjam, tanggal_kembali)}

# Fungsi Pembantu
def generate_loan_id():
    """Menghasilkan ID pinjaman baru"""
    return max(loans.keys() or [0]) + 1

def get_book_by_id(book_id):
    """Mencari buku berdasarkan ID"""
    return next((book for book in books if book[0] == book_id), None)

# Operasi CRUD untuk Pengguna
def create_user(nim, password, name, email):
    """Membuat pengguna baru"""
    if nim not in users:
        users[nim] = (password, name, email)
        return True
    return False

def read_user(nim):
    """Membaca data pengguna"""
    return users.get(nim)

def update_user(nim, name, email):
    """Memperbarui data pengguna"""
    if nim in users:
        password = users[nim][0]
        users[nim] = (password, name, email)
        return True
    return False

def delete_user(nim):
    """Menghapus pengguna"""
    if nim in users:
        del users[nim]
        return True
    return False

# Operasi CRUD untuk Buku
def create_book(title, author, qty):
    """Menambahkan buku baru"""
    book_id = len(books) + 1
    books.append((book_id, title, author, qty))
    return book_id

def read_book(book_id):
    """Membaca data buku"""
    return get_book_by_id(book_id)

def update_book(book_id, title, author, qty):
    """Memperbarui data buku"""
    for i, book in enumerate(books):
        if book[0] == book_id:
            books[i] = (book_id, title, author, qty)
            return True
    return False

def delete_book(book_id):
    """Menghapus buku"""
    global books
    books = [book for book in books if book[0] != book_id]

# Operasi CRUD untuk Peminjaman
def create_loan(nim, book_id):
    """Membuat peminjaman baru"""
    book = get_book_by_id(book_id)
    if book and book[3] > 0:
        loan_id = generate_loan_id()
        loan_date = datetime.now()
        return_date = loan_date + timedelta(days=14)
        loans[loan_id] = (nim, book_id, loan_date, return_date)
        update_book(book_id, book[1], book[2], book[3] - 1)
        return loan_id
    return None

def read_loan(loan_id):
    """Membaca data peminjaman"""
    return loans.get(loan_id)

def update_loan(loan_id, return_date):
    """Memperbarui tanggal kembali peminjaman"""
    if loan_id in loans:
        nim, book_id, loan_date, _ = loans[loan_id]
        loans[loan_id] = (nim, book_id, loan_date, return_date)
        return True
    return False

def delete_loan(loan_id):
    """Menghapus peminjaman (mengembalikan buku)"""
    if loan_id in loans:
        _, book_id, _, _ = loans[loan_id]
        book = get_book_by_id(book_id)
        update_book(book_id, book[1], book[2], book[3] + 1)
        del loans[loan_id]
        return True
    return False

# Antarmuka Pengguna
def register():
    """Fungsi untuk registrasi pengguna baru"""
    nim = input("Masukkan NIM: ")
    if nim in users:
        print("NIM sudah terdaftar.")
        return
    password = getpass.getpass("Masukkan password: ")
    
    # Fitur "Skip" pada pengisian nama
    name = input("Masukkan nama (atau ketik 'skip' untuk melewati): ")
    if name.lower() == 'skip':
        name = "Nama Tidak Diberikan"  # Atau bisa diatur sesuai kebutuhan
        
    email = input("Masukkan email: ")
    
    if create_user(nim, password, name, email):
        print("Registrasi berhasil.")
    else:
        print("Registrasi gagal.")

def login():
    """Fungsi untuk login pengguna"""
    nim = input("Masukkan NIM: ")
    password = getpass.getpass("Masukkan password: ")
    user = read_user(nim)
    if user and user[0] == password:
        print(f"Selamat datang, {user[1]}!")
        return nim
    else:
        print("Login gagal.")
        return None

def user_menu(nim):
    """Menu utama untuk pengguna"""
    while True:
        print("\n1. Lihat Profil")
        print("2. Edit Profil")
        print("3. Pinjam Buku")
        print("4. Lihat Peminjaman")
        print("5. Kembalikan Buku")
        print("6. Logout")
        choice = input("Pilih menu: ")

        if choice == '1':
            user = read_user(nim)
            print(f"NIM: {nim}")
            print(f"Nama: {user[1]}")
            print(f"Email: {user[2]}")
        elif choice == '2':
            name = input("Nama baru: ")
            email = input("Email baru: ")
            if update_user(nim, name, email):
                print("Profil berhasil diperbarui.")
            else:
                print("Gagal memperbarui profil.")
        elif choice == '3':
            print("Daftar Buku:")
            for book in books:
                print(f"{book[0]}. {book[1]} oleh {book[2]} (Tersedia: {book[3]})")
            book_id = int(input("Masukkan ID buku yang ingin dipinjam: "))
            loan_id = create_loan(nim, book_id)
            if loan_id:
                print(f"Buku berhasil dipinjam. ID Peminjaman: {loan_id}")
            else:
                print("Gagal meminjam buku.")
        elif choice == '4':
            user_loans = [loan for loan in loans.items() if loan[1][0] == nim]
            if user_loans:
                for loan_id, loan_info in user_loans:
                    book = get_book_by_id(loan_info[1])
                    print(f"ID Peminjaman: {loan_id}")
                    print(f"Buku: {book[1]}")
                    print(f"Tanggal Pinjam: {loan_info[2].strftime('%Y-%m-%d')}")
                    print(f"Tanggal Kembali: {loan_info[3].strftime('%Y-%m-%d')}")
                    print()
            else:
                print("Tidak ada peminjaman aktif.")
        elif choice == '5':
            loan_id = int(input("Masukkan ID Peminjaman yang ingin dikembalikan: "))
            if delete_loan(loan_id):
                print("Buku berhasil dikembalikan.")
            else:
                print("Gagal mengembalikan buku.")
        elif choice == '6':
            print("Logout berhasil.")
            break
        else:
            print("Pilihan tidak valid.")

def admin_menu():
    """Menu untuk admin"""
    while True:
        print("\n1. Tambah Buku")
        print("2. Lihat Daftar Buku")
        print("3. Edit Buku")
        print("4. Hapus Buku")
        print("5. Kembali")
        choice = input("Pilih menu: ")

        if choice == '1':
            title = input("Judul buku: ")
            author = input("Penulis: ")
            qty = int(input("Jumlah: "))
            book_id = create_book(title, author, qty)
            print(f"Buku berhasil ditambahkan dengan ID: {book_id}")
        elif choice == '2':
            for book in books:
                print(f"ID: {book[0]}, Judul: {book[1]}, Penulis: {book[2]}, Jumlah: {book[3]}")
        elif choice == '3':
            book_id = int(input("Masukkan ID buku yang ingin diedit: "))
            title = input("Judul baru: ")
            author = input("Penulis baru: ")
            qty = int(input("Jumlah baru: "))
            if update_book(book_id, title, author, qty):
                print("Buku berhasil diperbarui.")
            else:
                print("Gagal memperbarui buku.")
        elif choice == '4':
            book_id = int(input("Masukkan ID buku yang ingin dihapus: "))
            delete_book(book_id)
            print("Buku berhasil dihapus.")
        elif choice == '5':
            break
        else:
            print("Pilihan tidak valid.")

def main():
    """Fungsi utama program"""
    while True:
        print("\n1. Register")
        print("2. Login")
        print("3. Admin Menu")
        print("4. Keluar")
        choice = input("Pilih menu: ")

        if choice == '1':
            register()
        elif choice == '2':
            nim = login()
            if nim:
                user_menu(nim)
        elif choice == '3':
            admin_menu()
        elif choice == '4':
            print("Terima kasih! Program selesai.")
            break
        else:
            print("Pilihan tidak valid.")

if __name__ == "__main__":
    main()
