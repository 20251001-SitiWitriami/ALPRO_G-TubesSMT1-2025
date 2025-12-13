def create(data):
    print("\n=== TAMBAH PESANAN ===")
    nama = input("Nama: ")

    print("\n--- MENU ZARA CAFE ---")
    print("1. cheesecake - 25000")
    print("2. strawberry shortcake - 30000")
    print("3. chocolate dubai - 28000")
    print("4. milo miles crepes - 27000")

    pilihan = input("Pilih menu [1-4]: ")

    if pilihan == "1":
        menu = "cheesecake"
        harga = 25000
    elif pilihan == "2":
        menu = "strawberry shortcake"
        harga = 30000
    elif pilihan == "3":
        menu = "chocolate dubai"
        harga = 28000
    elif pilihan == "4":
        menu = "milo miles crepes"
        harga = 27000
    else:
        print("Pilihan tidak valid! Default: cheesecake")
        menu = "cheesecake"
        harga = 25000

    jumlah = int(input("Jumlah: "))
    total = harga * jumlah

    if not data:
        id_pesan = "P001"
    else:
        last_id = data[-1][0]
        last_num = int(last_id[1:])
        id_pesan = f"P{last_num + 1:03d}"

    data.append([id_pesan, nama, menu, harga, jumlah, total, "Proses"])
    print(f"Pesanan {id_pesan} ditambah")
    return data


def read(data):
    print("\n=== DAFTAR PESANAN ===")
    if not data:
        print("Kosong")
        return
    
    for item in data:
        print(f"{item[0]} - {item[1]} - {item[2]} - Harga: {item[3]} - Jumlah: {item[4]} - Total: {item[5]} - Status: {item[6]}")


def update(data):
    print("\n=== UPDATE PESANAN ===")
    if not data:
        print("Kosong")
        return data
    
    id_cari = input("ID pesanan: ")
    for i in range(len(data)):
        if data[i][0] == id_cari:
            status = input("Status baru [Proses/Selesai]: ")
            data[i][6] = status
            print("Berhasil update")
            return data
    
    print("Tidak ditemukan")
    return data


def delete(data):
    print("\n=== HAPUS PESANAN ===")
    if not data:
        print("Kosong")
        return data
    
    id_hapus = input("ID pesanan: ")
    for i in range(len(data)):
        if data[i][0] == id_hapus:
            data.pop(i)
            print("Terhapus")
            return data
    
    print("Tidak ditemukan")
    return data


def sorting(data):
    print("\n=== SORTING PESANAN ===")
    if not data:
        print("Data kosong!")
        return

    print("1. Sort Nama (A-Z)")
    print("2. Sort Total Harga (kecil ke besar)")
    pilih = input("Pilih: ")

    if pilih == "1":
        hasil = sorted(data, key=lambda x: x[1])
        print("\n--- HASIL SORTING NAMA ---")
        for item in hasil:
            print(item)

    elif pilih == "2":
        hasil = sorted(data, key=lambda x: x[5])
        print("\n--- HASIL SORTING TOTAL HARGA ---")
        for item in hasil:
            print(item)

    else:
        print("Pilihan tidak valid!")


def searching(data):
    print("\n=== SEARCHING PESANAN ===")
    if not data:
        print("Data kosong!")
        return

    print("1. Cari berdasarkan ID")
    print("2. Cari berdasarkan Nama")
    pilih = input("Pilih: ")

    if pilih == "1":
        key = input("Masukkan ID: ")
        for item in data:
            if item[0] == key:
                print("\n--- DATA DITEMUKAN ---")
                print(item)
                return
        print("ID tidak ditemukan")

    elif pilih == "2":
        key = input("Masukkan Nama: ")
        ditemukan = False
        print("\n--- HASIL PENCARIAN ---")
        for item in data:
            if item[1].lower() == key.lower():
                print(item)
                ditemukan = True

        if not ditemukan:
            print("Nama tidak ditemukan")

    else:
        print("Pilihan tidak valid!")


def menuUtama():
    print("\n=== ZARA CAFE ===")
    print("1. Tambah Pesanan")
    print("2. Lihat Pesanan")
    print("3. Update Status")
    print("4. Hapus Pesanan")
    print("5. Sorting Pesanan")
    print("6. Searching Pesanan")
    print("7. Keluar")

    try:
        pilih = int(input("Pilih [1-7]: "))
        return pilih
    except:
        return 0


pilihan = 0
data = []

while pilihan != 7:
    pilihan = menuUtama()
    if pilihan == 1:
        data = create(data)
    elif pilihan == 2:
        read(data)
    elif pilihan == 3:
        data = update(data)
    elif pilihan == 4:
        data = delete(data)
    elif pilihan == 5:
        sorting(data)
    elif pilihan == 6:
        searching(data)

print("Terima kasih!")
