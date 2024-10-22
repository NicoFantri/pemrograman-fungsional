from functools import reduce
from datetime import datetime, timedelta
import getpass

# Tipe data immutable
User = tuple
Book = tuple
Loan = tuple

# Fungsi pembantu
def generate_id(items):
    return max(items.keys() or [0]) + 1

def find_by_id(items, item_id):
    return next((item for item in items.values() if item[0] == item_id), None)

# Operasi CRUD untuk User
def create_user(users, nim, password, name, email):
    return {**users, nim: User((nim, password, name, email))}

def update_user(users, nim, name, email):
    
    return {**users, nim: User((nim, users[nim][1], name, email))} if nim in users else users

def delete_user(users, nim):
    return {k: v for k, v in users.items() if k != nim}

# Operasi CRUD untuk Book
def create_book(books, title, author, qty):
    book_id = generate_id(books)
    return {**books, book_id: Book((book_id, title, author, qty))}

def update_book(books, book_id, title, author, qty):
    return {**books, book_id: Book((book_id, title, author, qty))} if book_id in books else books

def delete_book(books, book_id):
    
    return {k: v for k, v in books.items() if k != book_id}

# Operasi CRUD untuk Loan
def create_loan(loans, books, nim, book_id):
    book = books.get(book_id)
    if book and book[3] > 0:
        loan_id = generate_id(loans)
        loan_date = datetime.now()
        return_date = loan_date + timedelta(days=14)
        new_loan = Loan((loan_id, nim, book_id, loan_date, return_date))
        new_loans = {**loans, loan_id: new_loan}
        new_books = update_book(books, book_id, book[1], book[2], book[3] - 1)
        return (new_loans, new_books)
    return (loans, books)

def update_loan(loans, loan_id, return_date):
    loan = loans.get(loan_id)
    return {**loans, loan_id: Loan((loan[0], loan[1], loan[2], loan[3], return_date))} if loan else loans

def delete_loan(loans, books, loan_id):
    loan = loans.get(loan_id)
    if loan:
        book = books.get(loan[2])
        new_books = update_book(books, book[0], book[1], book[2], book[3] + 1)
        new_loans = {k: v for k, v in loans.items() if k != loan_id}
        return (new_loans, new_books)
    return (loans, books)

# Fungsi UI (masih memiliki side effects karena I/O)
def get_input(prompt):
    return input(prompt)

def get_password(prompt):
    return getpass.getpass(prompt)

def print_message(message):
    print(message)

# Fungsi logika bisnis
def register_user(users):
    nim = get_input("Masukkan NIM: ")
    if nim in users:
        return (users, "NIM sudah terdaftar.")
    password = get_password("Masukkan password: ")
    name = get_input("Masukkan nama (atau ketik 'skip' untuk melewati): ")
    name = "Nama Tidak Diberikan" if name.lower() == 'skip' else name
    email = get_input("Masukkan email: ")
    new_users = create_user(users, nim, password, name, email)
    return (new_users, "Registrasi berhasil.")

def authenticate_user(users, nim, password):
    user = users.get(nim)
    return user[1] == password if user else False

def borrow_book(loans, books, nim):
    print_message("Daftar Buku:")
    for book in books.values():
        print_message(f"{book[0]}. {book[1]} oleh {book[2]} (Tersedia: {book[3]})")
    book_id = int(get_input("Masukkan ID buku yang ingin dipinjam: "))
    new_loans, new_books = create_loan(loans, books, nim, book_id)
    return (new_loans, new_books, "Buku berhasil dipinjam." if new_loans != loans else "Gagal meminjam buku.")

def return_book(loans, books):
    loan_id = int(get_input("Masukkan ID Peminjaman yang ingin dikembalikan: "))
    new_loans, new_books = delete_loan(loans, books, loan_id)
    return (new_loans, new_books, "Buku berhasil dikembalikan." if new_loans != loans else "Gagal mengembalikan buku.")

# Fungsi menu (masih menggunakan loop untuk interaksi pengguna)
def user_menu(users, books, loans, nim):
    while True:
        print_message("\n1. Lihat Profil\n2. Edit Profil\n3. Pinjam Buku\n4. Lihat Peminjaman\n5. Kembalikan Buku\n6. Logout")
        choice = get_input("Pilih menu: ")
        
        if choice == '1':
            user = users[nim]
            print_message(f"NIM: {user[0]}\nNama: {user[2]}\nEmail: {user[3]}")
        elif choice == '2':
            name = get_input("Nama baru: ")
            email = get_input("Email baru: ")
            users = update_user(users, nim, name, email)
            print_message("Profil berhasil diperbarui.")
        elif choice == '3':
            loans, books, message = borrow_book(loans, books, nim)
            print_message(message)
        elif choice == '4':
            user_loans = {k: v for k, v in loans.items() if v[1] == nim}
            if user_loans:
                for loan in user_loans.values():
                    book = books[loan[2]]
                    print_message(f"ID Peminjaman: {loan[0]}\nBuku: {book[1]}\nTanggal Pinjam: {loan[3]}\nTanggal Kembali: {loan[4]}")
            else:
                print_message("Tidak ada peminjaman aktif.")
        elif choice == '5':
            loans, books, message = return_book(loans, books)
            print_message(message)
        elif choice == '6':
            print_message("Logout berhasil.")
            break
    return (users, books, loans)

def admin_menu(books):
    while True:
        print_message("\n1. Tambah Buku\n2. Lihat Daftar Buku\n3. Edit Buku\n4. Hapus Buku\n5. Kembali")
        choice = get_input("Pilih menu: ")
        
        if choice == '1':
            title = get_input("Judul buku: ")
            author = get_input("Penulis: ")
            qty = int(get_input("Jumlah: "))
            books = create_book(books, title, author, qty)
            print_message(f"Buku berhasil ditambahkan dengan ID: {max(books.keys())}")
        elif choice == '2':
            for book in books.values():
                print_message(f"ID: {book[0]}, Judul: {book[1]}, Penulis: {book[2]}, Jumlah: {book[3]}")
        elif choice == '3':
            book_id = int(get_input("Masukkan ID buku yang ingin diedit: "))
            title = get_input("Judul baru: ")
            author = get_input("Penulis baru: ")
            qty = int(get_input("Jumlah baru: "))
            books = update_book(books, book_id, title, author, qty)
            print_message("Buku berhasil diperbarui.")
        elif choice == '4':
            book_id = int(get_input("Masukkan ID buku yang ingin dihapus: "))
            books = delete_book(books, book_id)
            print_message("Buku berhasil dihapus.")
        elif choice == '5':
            break
    return books

# Fungsi utama (masih menggunakan loop untuk interaksi pengguna)
def main():
    users, books, loans = {}, {}, {}
    while True:
        print_message("\n1. Register\n2. Login\n3. Admin Menu\n4. Keluar")
        choice = get_input("Pilih menu: ")
        
        if choice == '1':
            users, message = register_user(users)
            print_message(message)
        elif choice == '2':
            nim = get_input("Masukkan NIM: ")
            password = get_password("Masukkan password: ")
            if authenticate_user(users, nim, password):
                print_message(f"Selamat datang, {users[nim][2]}!")
                users, books, loans = user_menu(users, books, loans, nim)
            else:
                print_message("Login gagal.")
        elif choice == '3':
            books = admin_menu(books)
        elif choice == '4':
            print_message("Terima kasih! Program selesai.")
            break

if __name__ == "__main__":
    main()