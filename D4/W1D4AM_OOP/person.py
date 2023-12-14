class Person:
    def __init__(self, name, age):
        # self.name disini membuat atribut name
        self.name = name
        # self.age disini membuat atribut age
        self.age = age
    
    # membuat function checkName yang bisa dipanggil oleh object
    def checkName(self):
        # print string diawali dengan f digunakan untuk formatting dimana kita bisa print variable didalam string dengan cara di apit kurang kurawal
        print(f'ini dari dalam class, value name dari object yang dipanggil ialah: {self.name}')

# membuat object alice
aliceObj = Person('Alice', 25)
aliceObj.checkName()

# membuat object rian
rianObj = Person('Rian', 17)
rianObj.checkName()

aliceObj.name = 'Ganti Nama'
aliceObj.checkName()
rianObj.checkName()

print(f'halo nama saya adalah {rianObj.name}')