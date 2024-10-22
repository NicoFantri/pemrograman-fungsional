# Fungsi penjumlahan
def addition(x, y):
    return x + y
# Mengembalikan hasil penjumlahan dari x dan y

# Fungsi pengurangan
def subtraction(a, b):
    return a - b
# Mengembalikan hasil pengurangan a dengan b

# Fungsi perkalian
def multiplication(x, y):
    return x * y
# Mengembalikan hasil perkalian dari x dan y

# Fungsi pembagian
def division(x, y):
    if y == 0:
        return "Error: Division by zero"
    return x / y
# Jika y sama dengan 0, mengembalikan pesan kesalahan, 
# jika tidak, mengembalikan hasil pembagian x dengan y

# Fungsi utama untuk menjalankan contoh operasi
def main():
    a = 10
    b = 5
    print("Addition:", addition(a, b))
    print("Subtraction:", subtraction(a, b))
    print("Multiplication:", multiplication(a, b))
    print("Division:", division(a, b))
# Mendefinisikan variabel a dan b, 
# dan mencetak hasil dari operasi aritmatika menggunakan fungsi yang telah didefinisikan

if __name__ == "__main__":
    main()
# Memastikan bahwa fungsi main hanya dijalankan 
# jika file ini dieksekusi sebagai program utama
