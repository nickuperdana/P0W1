class Dog:
    def __init__(self, name, breed, furColor):
        self.name = name
        self.breed = breed
        self.furColor = furColor

    
    def woof(self):
        # print('woof woof woof')
        return 'woof woof woof'


    def introduction(self):
        print(f'Hello my name is {self.name} {self.woof()}')

    def __str__(self):
        return f'The dog name is {self.name} with the breed is {self.breed} and the fur color is {self.furColor}'


class DogHouse:
    def __init__(self, name):
        self.name = name
        self.dogs_adopted = []



if __name__ == '__main__':

    james = Dog('James', 'Chihuahua', 'Dark Brown')
    hermes = Dog('Hermes', 'Bulldog', 'Black')

    print(james)
    print(hermes)
    # print(james.name)
    # james.woof()
    # james.introduction()
    # hermes.introduction()
    # print(james.woof())


    happyDog = DogHouse('Happy Dog')

    happyDog.dogs_adopted.append(james)
    happyDog.dogs_adopted.append(hermes)

    print(happyDog.dogs_adopted[0].name)

    # print(len(happyDog.dogs_adopted))