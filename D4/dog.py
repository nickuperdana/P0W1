# Alt + Z untuk wrap code


class Dog: # [Dog] adalah kelasnya
    def __init__(self, name, breed, furColor):  # __init__ untuk menyimpan data, kepanjangan dari `initialize`; [self] adalah convention term/bloat code untuk mereferensikan dog; [name, breed, furColor, leg] adalah argumen
        # `self` wajib di awal, karena argumen pertama gak diiitung
        self.name = name
        self.breed = breed
        self.furColor = furColor
    # kalau mau tambahkan fungsi, buat def baru, pisahkan 2 enter
    
        #fungsi untuk 
    def woof(self):
        print('woof, woof, woof') # kalau mau menghasilkan ini sebagai output, gunakan `return 'woof, woof, woof'`; menampilkan = print, mengembalikan nilai = return
        
    def introduction(self):
        print(f"Hello, my name is {self.name} woof, woof, woof.")
    
    
    # # kode ini untuk membuat fungsi string, yang mana objek direpresentasikan sebagai string
    def __str__(self):
        print(f"The dog name is {self.name} with the breed is {self.breed} and the fur color is {self.furColor}")
# class dan kode dipisahkan dengan 2 enter





# print(james) # <__main__.Dog object at 0x0000020118651410>

# print(james.name) # print nama dari Dog, akan error kalau nama belum di assign

# james.woof() # melakukan fungsi `woof` untuk kelas `dog` yang diassign di `james`




class DogHouse: # nama kelas pakai PascalCase
    def __init__(self, name):
        self.name = name
        self.dogs_adopted = [] # untuk menyimpan list nama-nama anjing yang bakal diisi nanti oleh user, gunakan argumen dengan list kosong (plural), atau `None` (singular); `*args` itu dipakai untuk mengisi list
        pass #Biasakan pakai ini dulu sebelum selesaikan semuanya/coba satu-satu






# print(happyDog.dogs_adopted[0].james)

# print(len(happyDog.dogs_adopted)) # menampilkan jumlah terbaru data yang telah di-append

if __name__ == "__main__": # untuk memastikan output yang hanya akan berlaku ketika me-run script ini saja, dalam kasus kalau class ini akan diimpor ke dalam file lain
    james = Dog('James', 'Chihuahua', 'Dark Brown') # isikan argumen dengan urutan yang sama dengan yang ada di def 
    # assign argument dalam kelas di atas, name==`James`, breed=`chihuahua`
    james.introduction()

    hermes = Dog('Hermes', 'Bulldog', 'Black')
    # data baru, bisa disimpan secara terpisah

    hermes.introduction()
    happyDog = DogHouse('Happy Dog')

    # ingin menampung `James` dan `Hermes`
    happyDog.dogs_adopted.append(james)
    happyDog.dogs_adopted.append(hermes)
