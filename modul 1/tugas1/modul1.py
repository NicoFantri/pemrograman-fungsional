class SistemAkademik:
    def __init__(self):
        self.users = {}
        self.profiles = {}
        self.friends = {}

    def register(self):
        nim = input("Masukkan NIM: ")
        password = input("Masukkan password: ")
        if nim not in self.users:
            self.users[nim] = password
            self.profiles[nim] = {}
            self.friends[nim] = []
            print("Register berhasil!")
            self.isi_biodata(nim)
        else:
            print("NIM sudah terdaftar!")

    def login(self):
        nim = input("Masukkan NIM: ")
        password = input("Masukkan password: ")
        if nim in self.users and self.users[nim] == password:
            print("Login berhasil!")
            self.menu(nim)
        else:
            print("NIM atau password salah!")

    def isi_biodata(self, nim):
        print("Isi biodata profil:")
        nama = input("Nama: ")
        jurusan = input("Jurusan: ")
        self.profiles[nim] = {"nama": nama, "jurusan": jurusan}
        print("Biodata berhasil disimpan!")
        self.tambah_friends(nim)

    def tambah_friends(self, nim):
        while True:
            print("Tambahkan teman:")
            print("1. Tambahkan teman")
            print("2. Skip")
            pilihan = input("Pilihan: ")
            if pilihan == "1":
                friend_nim = input("NIM teman: ")
                if friend_nim not in self.friends[nim]:
                    self.friends[nim].append(friend_nim)
                    print("Teman berhasil ditambahkan!")
                else:
                    print("Teman sudah ada!")
            elif pilihan == "2":
                break
            else:
                print("Pilihan salah!")

    def menu(self, nim):
        while True:
            print("Menu:")
            print("1. Lihat profil")
            print("2. Tambahkan data profil")
            print("3. Edit data profil")
            print("4. Hapus data profil")
            print("5. Tambahkan teman")
            print("6. Edit teman")
            print("7. Hapus teman")
            print("8. Logout")
            pilihan = input("Pilihan: ")
            if pilihan == "1":
                self.lihat_profil(nim)
            elif pilihan == "2":
                self.tambah_data_profil(nim)
            elif pilihan == "3":
                self.edit_data_profil(nim)
            elif pilihan == "4":
                self.hapus_data_profil(nim)
            elif pilihan == "5":
                self.tambah_friends(nim)
            elif pilihan == "6":
                self.edit_friends(nim)
            elif pilihan == "7":
                self.hapus_friends(nim)
            elif pilihan == "8":
                break
            else:
                print("Pilihan salah!")

    def lihat_profil(self, nim):
        print("Profil:")
        print("NIM:", nim)
        print("Nama:", self.profiles[nim]["nama"])
        print("Jurusan:", self.profiles[nim]["jurusan"])
        print("Teman:", self.friends[nim])

    def tambah_data_profil(self, nim):
        print("Tambahkan data profil:")
        key = input("Key: ")
        value = input("Value: ")
        self.profiles[nim][key] = value
        print("Data profil berhasil ditambahkan!")

    def edit_data_profil(self, nim):
        print("Edit data profil:")
        key = input("Key: ")
        value = input("Value: ")
        if key in self.profiles[nim]:
            self.profiles[nim][key] = value
            print("Data profil berhasil diedit!")
        else:
            print("Key tidak ada!")

    def hapus_data_profil(self, nim):
        print("Hapus data profil:")
        key = input("Key: ")
        if key in self.profiles[nim]:
            del self.profiles[nim][key]
            print("Data profil berhasil dihapus!")
        else:
            print("Key tidak ada!")

    def edit_friends(self, nim):
        print("Edit teman:")
        friend_nim = input("NIM teman: ")
        if friend_nim in self.friends[nim]:
            new_friend_nim = input("NIM teman baru: ")
            self.friends[nim][self.friends[nim].index(friend_nim)] = new_friend_nim
            print("Teman berhasil diedit!")
        else:
            print("Teman tidak ada!")

    def hapus_friends(self, nim):
        print("Hapus teman :")
        friend_nim = input("NIM teman: ")
        if friend_nim in self.friends[nim]:
            self.friends[nim].remove(friend_nim)
            print("Teman berhasil dihapus!")
        else:
            print("Teman tidak ada!")

sistem_akademik = SistemAkademik()
while True:
    print("Menu:")
    print("1. Register")
    print("2. Login")
    print("3. Exit")
    pilihan = input("Pilihan: ")
    if pilihan == "1":
        sistem_akademik.register()
    elif pilihan == "2":
        sistem_akademik.login()
    elif pilihan == "3":
        break
    else:
        print("Pilihan salah!")