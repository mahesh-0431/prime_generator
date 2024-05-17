import unittest
from midaas import prime,mahi

class TestPrimeGenerators(unittest.TestCase):
    def test_mahi(self):
        self.assertEqual(mahi(2,5),[2,3,5])
        self.assertEqual(mahi(1,10),[2,3,5,7])
        self.assertEqual(mahi(0,1),[])
        

    def test_prime(self):
        self.assertEqual(prime(1,10), [2,3,5,7])
        self.assertEqual(prime(10,20), [11,13,17,19])
        self.assertEqual(prime(0,1), [])

    

if __name__ == '__main__':
    unittest.main()
