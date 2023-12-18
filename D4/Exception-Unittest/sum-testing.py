import unittest


def sum(a, b):
    if(not isinstance(a, int) or not isinstance(b, int)):
        raise ValueError('Hanya boleh angka')
    return a + b

class SumTesting(unittest.TestCase):
    def test_sum_8_10(self):
        result = sum(8, 10)
        self.assertEqual(18, result)
    
    def test_sum_15_15(self):
        result = sum(15, 15)
        self.assertEqual(30, result)

if __name__ == '__main__':
    unittest.main()