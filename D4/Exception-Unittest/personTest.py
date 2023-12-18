# from person import Person
from person import Person
import unittest

class PersonTest(unittest.TestCase):
    '''
        this class is develop to test Person class 
        it's function and attribute functionality need to check invidually
        you can run the test in terminal with
        python -m unittest personTest.PersonTest
        or
        python personTest
    '''

    def test_attribute(self):
        ersapta = Person('Ersapta Aristo', 25, 1000000)
        self.assertEqual('Ersapta Aristo', ersapta.name)
        self.assertEqual(25, ersapta.age)
        self.assertEqual(1000000, ersapta.get_balance())
    
    def test_increaseAge(self):
        ersapta = Person('Ersapta Aristo', 25, 1000000)
        self.assertEqual(ersapta.age, 25)

        ersapta.increaseAge()

        print(ersapta.age)

        self.assertEqual(ersapta.age, 26)

    def test_addBalance(self):
        ersapta = Person('Ersapta Aristo', 25, 1000000)
        self.assertEqual(ersapta.get_balance(), 1000000)

        ersapta.addBalance(1000000)

        self.assertEqual(ersapta.get_balance(), 2000000)
    
    def test_payItem_enough_balance(self):
        ersapta = Person('Ersapta Aristo', 25, 1000000)
        self.assertEqual(ersapta.get_balance(), 1000000)

        result = ersapta.payItem('Laptop SNSV', 1000000)

        self.assertDictEqual(result, {
            'itemName': 'Laptop SNSV',
            'itemPrice': '1000000',
            'currentBalance': 0
        })
    
    def test_payItem_enough_balance(self):
        ersapta = Person('Ersapta Aristo', 25, 1000000)
        self.assertEqual(ersapta.get_balance(), 1000000)

        with self.assertRaises(ValueError) as e:
            ersapta.payItem('Hp weihua', 1000001)

        self.assertEqual(str(e.exception), 'Not enough balance')

if __name__ == '__main__':
    # verbosity ditambahkan agar hasilnya lebih lengkap
    Person()
    unittest.main(verbosity=2)
    
    Person()