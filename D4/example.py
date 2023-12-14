# Day 4 PM

# Contoh 1

# for i in [1,2,3,'four','5']:
#   try:
#     print(f'current value i: {i}')
#     print(float(i))
#   except:
#     print(f'error with value: {i}') # Logging
#     pass



# Contoh 2

# divider = [10, 9, 8, 7, 6, 5, 4, 3, 2 ,1, 0, 'satu']

# for i in divider:
#     try:
#         print(f'100/{i} = {100/i}')
#     except ZeroDivisionError:
#         print('Dalam matematika, angka tidak bisa dibagi dengan 0')
#     except:
#         print(f'error ketika pembagi "{i}" {type(i)}') # kalau ada error selain `zerodivisionerror`
    
#     print("Program sudah selesai")


# contoh 3

student_score = [80, 54, 78, 23, 87, 120, 98, 66, 47]

for score in student_score:
    try:
        if score < 0 or score > 100:
            raise ValueError("Nilai tidak valid")
        if score >= 85:
            print('A')
        elif score > 70:
            print('B')
        elif score > 60:
            print('C')
        elif score > 50:
            print('D')
        else:
            print("E")
    except Exception as E:
        print(E)


        