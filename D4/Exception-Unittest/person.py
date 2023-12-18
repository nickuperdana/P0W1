class Person:
    def __init__(self, name, age, balance = 0):
        self.name = name
        self.age = age
        self.__balance = balance


    def increaseAge(self):
        '''
        
        '''
        self.age += 1
    
    def addBalance(self, amount):
        self.__balance += amount

    def payItem(self, itemName, itemPrice):
        if self.__balance < itemPrice:
            raise ValueError('Not enough balance')
        self.__balance -= itemPrice
        return {
            'itemName': itemName,
            'itemPrice': itemPrice,
            'currentBalance': self.__balance
        }
    
    def get_balance(self):
        return self.__balance
    

if __name__ == '__main__':
    ersaptaObj = Person('Ersapta', 12, 10000000)
    ersaptaObj.increaseAge()
    print(ersaptaObj.age)