class Nasabah:
    def __init__(self, name, ktp, deposit):
        self.name = name
        self.ktp = ktp
        self.deposit = deposit


class Bank:
    def __init__(self, name):
        self.name = name
        self.nasabah = []

    def addNasabah(self, name, ktp, deposit):
        nasabah = Nasabah(name, ktp, deposit)
        self.nasabah.append(nasabah)

    def removeNasabah(self, ktp):
        pass

    def displayListNasabah(self):
        print('Berikut data seluruh nasabah')
        print('No|Nama|KTP|Deposit')
        for index, nasabah in enumerate(self.nasabah):
            print(f'{index + 1} | {nasabah.name} | {nasabah.ktp} | {nasabah.deposit}')

    def displayMenu(self):
        print('''
Silahkan pilih menu dari 1 - 5
1. Tambah Nasabah
2. Hapus Nasabah
3. List Nasabah
4. Total tabungan seluruh nasabah   
5. Exit           
              ''')
        

if __name__ == '__main__':
    bankSapta = Bank('Sapta')
    isRun = True

    while isRun:
        bankSapta.displayMenu()
        selectedMenu = input('Pilih Menu: ')
        if(selectedMenu == '5'):
            isRun = False

        elif selectedMenu == '1':
            name = input('Nama Nasabah: ')
            ktp = input('Nomor KTP Nasabah: ')
            deposit = input('Total Deposit Nasabah: ')
            bankSapta.addNasabah(name, ktp, deposit)

        elif selectedMenu == '3':
            bankSapta.displayListNasabah()
        
    else:
        print('Terima kasih sudah menggunakan sistem kami')