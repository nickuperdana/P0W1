# function menu 1
def for_entry(inventory):
    barang = input('masukkan nama barang: ')
    kategori = input('masukkan kategori barang: ')
    harga = input('masukkan harga barang: ')

    inventory.append([barang, kategori, harga])

    print(f'Barang {barang} berhasil ditambahkan')
    return inventory

# function menu 2
def show_entry(inventory):
    if len(inventory)==0:
        print('Inventory masih kosong')
    else:
        print('No |Barang |Kategori |Harga')
        for i, entry in enumerate(inventory):
            print(f'{i+1} |{entry[0]} |{entry[1]} |{entry[2]}')

# PROGRAM INVENTORY
inventory = []
while True:
  print('''
      ------------------------------------------
      Selamat datang, silahkan masukkan angka:

      1. Input Data
      2. Show Data
      99. exit
      ------------------------------------------
  ''')

  try:                                    # make sure input for menu in form of number
    choice = int(input('masukkan menu: '))

    if choice == 1:
      inventory = for_entry(inventory)    #func 1

    elif choice == 2:
      show_entry(inventory)               #func 2

    elif choice == 99:                    #exit
      print('terima kasih')
      break

    else:                                 #non-existed choice
      print('masukkan angka yang cocok')

  except:
    print('masukkan angka ya')