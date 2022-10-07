user = [
    {
        "id": 0,
        "username": "user1",
        "password": "password",
        "role": "user",
        "booked_book_id": []
    },
    {
        "id": 1,
        "username": "user2",
        "password": "password",
        "role": "user",
        "booked_book_id": [1,2]

    },
    {
        "id": 2,
        "username": "admin",
        "password": "password",
        "role": "admin",
        "booked_book_id": []

    },
]

rak_buku = {
    1:{
        "book_name": "Marmut Merah Jambu",
        "penulis": "Radit",
        "published_date": "2020",
        "is_booked": False,
        "booked_by" : -1
    },
    2:{
        "book_name": "Penyu",
        "penulis": "Radit",
        "published_date": "2020",
        "is_booked": False,
        "booked_by" : -1
    },
    3:{
        "book_name": "Laskar Pelangi",
        "penulis": "Radit",
        "published_date": "2020",
        "is_booked": False,
        "booked_by" : -1
    },
}

def loginPage(loginOrRegist):
    if(loginOrRegist == "login"):
        print("== Login ==")
        login(input("Username: "), input("Password: "))
    else:
        print("== Register user ==")
        login(input("Username: "), input("Password: "))
    
def login(username, password):
    for data in user:
        if(data["username"] == username and data["password"] == password):
            return data
    return None
def register(username, password):
    user.append({
        "id": len(user),
        "username": username,
        "password": password,
        "role": "user"
    })
    return user[len(user)]

def pinjamBuku(bookId, userId):
    if(bookId < 0 or bookId > len(rak_buku)):
        print("Buku Tidak ada di rak buku")
        return False
    if(rak_buku[bookId]["is_booked"]):
       print("Buku Tidak dapat dipinjam, [Sedang dipinjam oleh user lain]")
       return False
    rak_buku[bookId]["is_booked"] = "True"
    rak_buku[bookId]["booked_by"] = userId
    user[userId]["booked_book_id"].append(bookId)

def pinjamBukuPage(userId):
    print("== Pinjam Buku ==")
    listAvailableBook()
    pinjamBuku(int(input("Masukkan id Buku: ")), userId)

def listAvailableBook():
    print("ID | Judul Buku")
    for id, data in rak_buku.items():
        if data["is_booked"] == False:
            print(id,  " | ", data["book_name"])

def listAllBook():
    print("== List Semua Buku ==")
    for id, data in rak_buku.items():
        print(id, ". ", data["book_name"])
        print("Author : ", data["penulis"])
        print("Tahun Terbit: : ", data["published_date"])
        print("")

def listBukuDipinjam(userId):
    print("ID | Judul Buku")
    for id in user[userId]["booked_book_id"]:
        print(id, " | ", rak_buku[id]["book_name"])
            
def tambahBuku():
    print("== Tambah Buku ==")
    bookName = input("\nNama buku: ")
    authorName = input("Author: ")
    publishedDate = input("Tahun di publis: ")
    rak_buku[len(rak_buku)+1] = {
            "book_name": bookName,
            "penulis": authorName,
            "published_date": publishedDate,
            "booked": False,
            "booked_by": "",
        }

def kembalikanBukuPage(userId):
    print("== Pilih buku untuk dikembalikan: ==")
    listBukuDipinjam(userId)
    kembalikanBuku(int(input("Pilihan anda: ")), userId)

def kembalikanBuku(bookId, userId):
    if(rak_buku[bookId]['booked_by'] == userId):
        rak_buku[bookId]['booked_by'] = -1
        rak_buku[bookId]['is_booked'] = False
        user[userId]["booked_book_id"].remove(bookId)
    
def printMenuUser():
    print("""
        == MyPerpus ==
        Silahkan pilih menu berikut:
        1. Pinjam Buku
        2. Kembalikan Buku
        3. Tampilkan Buku saya
        4. keluar
        """)
def printMenuAdmin():
    print("""
        == MyPerpus ==
        Silahkan pilih menu berikut:
        1. Pinjam Buku
        2. Tampil Semua Buku
        3. Logout
        4. Exit Program
        """)

def menu(userRole, userId):
    if userRole == "user":
        printMenuUser()
    else:
        printMenuAdmin();

    menuInput = int(input("Pilihan Saya: "))

    if userRole == "admin":
        match menuInput:
            case 1:
                tambahBuku()
            case 2:
                listAllBook()
            case 3: 
                return False
            case 4:
                exit()                
            case default:
                print("Salah salah")
    elif userRole == "user":
        match menuInput:
            case 1:
                pinjamBukuPage(userId)
            case 2:
                kembalikanBukuPage(userId)
            case 3: 
                listBukuDipinjam(userId)
            case 4:
                return False
            case default:
                print("Salah salah")
    else: 
        print("Salah Input")
    return True
        
while True:
    currentUser = login(input("Username: "), input("Password: "))

    if currentUser != None:

        userRole = currentUser["role"]
        userId = currentUser["id"]

        print("current User:", userRole)
        session = True
        while session:
            session = menu(userRole, userId)
        current_user_id = None
    




