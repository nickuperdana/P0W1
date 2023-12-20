class Catalog:
    def __init__(self, title, author, uniqueId):
        self.title = title
        self.author = author
        self.uniqueID = uniqueId

class Interaction:
    def __init__(self):
        self.catalog = []
    
    def addItems(self, titleAdd, authorAdd, uniqueIdAdd):
        
        self.titleAdd = titleAdd
        self.authorAdd = authorAdd
        self.uniqueIdAdd = uniqueIdAdd
        
        addingEntry = Catalog(title=self.titleAdd, author= self.authorAdd, uniqueId=self.uniqueIdAdd)
        
        self.catalog.append(addingEntry)
        print(f'Buku {self.titleAdd} karya {self.authorAdd} (ID: {self.uniqueIdAdd}) berhasil ditambahkan')

    def searchItem(self):
        pass
    
    def removingItem(entry):
        pass
    
    def listBooks(self):
        pass
    

while True:
    print('''
Menu:
1. Tambah buku ke dalam katalog
2. Cari buku di dalam katalog
3. Hapus buku dari katalog
4. Lihat daftar buku
5. Keluar
''')
    
    try:
        inputUser = int(input("Pilih menu: "))
        
        if inputUser == 1:
            print("PASS")
            break
    except:
        print("error")