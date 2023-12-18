class Cat:
    def __init__(self, name, kind, furColor, gender):
        self.name = name
        self.kind = kind
        self.furColor = furColor
        self.gender = gender
    
    def meow(self):
        print('meow meow meow')
    
    def profile(self):
        return f'Halo nama saya {self.name}, saya adalah kucing {self.kind}, warna kulit saya {self.furColor} saya juga adalah kucing {self.gender}'
    
    # __str__ akan ke trigger ketika object di print
    def __str__(self):
        return f'saya kucing {self.kind} dengan nama {self.name}'


class Persia(Cat):
    def __init__(self, name, furColor, gender, horn):
        Cat.__init__(self, name, 'Persia', furColor, gender)
        self.horn = horn

kittyPersia = Persia('Kitty', 'Grey', 'Male', 2)

print(kittyPersia)
kittyPersia.meow()
print(kittyPersia.horn)