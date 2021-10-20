import unittest
from wallet import Wallet

class fill_wallet(unittest.TestCase):
    """Test wallet fill wallet function"""

    def setUp(self):
        self.wallet = Wallet()


    def test_money_length(self):
        """Instantiate a Wallet object, test that its money list has a length of 88"""
        length = len(self.wallet.money)
        self.assertEqual(length, 88)



if __name__ == '__main__':
    unittest.main()