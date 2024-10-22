from functools import reduce

# Data buku
books = [
    {"title": "Python Programming", "author": "John Smith", "pages": 250},
    {"title": "Data Structures", "author": "Jane Doe", "pages": 180},
    {"title": "Kalkulus Dasar", "author": "Ali Ahmad", "pages": 310},
    {"title": "Kimia Organik", "author": "Budi Pratama", "pages": 225},
    {"title": "Komputer Graphics", "author": "Michael Johnson", "pages": 150},
]

# 1. Buku berawalan huruf 'K' menggunakan list comprehension
k_books = [book for book in books if book["title"].startswith('K')]
print("1. Buku berawalan huruf 'K':")
for book in k_books:
    print(f"- {book['title']}")

# Fungsi untuk mendapatkan judul buku
def get_title(book):
    """Mengambil judul dari dictionary buku"""
    return book["title"]

# 2. Daftar judul buku menggunakan map()
titles = list(map(get_title, books))
print("\n2. Daftar judul buku:")
for title in titles:
    print(f"- {title}")

# Fungsi untuk mengecek jumlah halaman
def is_long_book(book):
    """Mengecek apakah buku memiliki lebih dari 200 halaman"""
    return book["pages"] > 200

# 3. Buku dengan halaman > 200 menggunakan filter()
long_books = list(filter(is_long_book, books))
print("\n3. Buku dengan halaman > 200:")
for book in long_books:
    print(f"- {book['title']} ({book['pages']} halaman)")

# Fungsi untuk menjumlahkan halaman
def sum_pages(acc, book):
    """Menjumlahkan halaman buku"""
    return acc + book["pages"]

# 4. Total halaman menggunakan reduce()
total_pages = reduce(sum_pages, books, 0)
print(f"\n4. Total jumlah halaman semua buku: {total_pages}")