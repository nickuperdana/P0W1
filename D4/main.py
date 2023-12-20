from dog import Dog, DogHouse # cara mengimpor kelas `Dog` dari file python `dog` (dog.py) yang ada dalam satu direktori file ini

chanel = Dog('Chanel', 'Pug', 'Pink')

chanelli = Dog('Chan', 'Pu', 'Pik')

# chanel.introduction()

happyDog = DogHouse()

happyDog.dogs_adopted.append(chanel)
happyDog.dogs_adopted.append(chanelli)

print(happyDog.dogs_adopted)