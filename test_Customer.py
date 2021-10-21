import unittest
from backpack import Backpack
from customer import Customer
from cans import Cola



class test_get_wallet_coin(unittest.TestCase):
    """Test for customers get wallet function"""

    def setUp(self):
        self.customer = Customer()

    def test_coin_return_quarter(self):
        """Test each type of coin can be returned from wallet"""
        test_coin_return = self.customer.get_wallet_coin('Quarter')
        self.assertEqual(test_coin_return.value,.25)
        
    def test_coin_return_dime(self):
       test_coin_return = self.customer.get_wallet_coin('Dime')
       self.assertEqual(test_coin_return.value,.10)

    def test_coin_return_nickel(self):
       test_coin_return = self.customer.get_wallet_coin('Nickel')
       self.assertEqual(test_coin_return.value,.05)

    def test_coin_return_penny(self):
       test_coin_return = self.customer.get_wallet_coin('Penny')
       self.assertEqual(test_coin_return.value,.01)

    
    
    def test_not_valid_coin(self):
        """Test that passing in a string that is not a valid coin name will return None"""
        test_coin_return = self.customer.get_wallet_coin('Dollar')
        self.assertIsNone(None)






class test_add_coins_to_wallet(unittest.TestCase):
    """Test for customers add coins to wallet function"""

    def setUp(self):
        self.customer = Customer()

    
    
    def test_wallet_length(self):
        """Pass in a list of 3 coins, test that then len of the customer's wallet money list went up by 3"""
        coins = ["Quarter", "Dime", "Nickel"]
        self.customer.add_coins_to_wallet(coins)
        length = len(self.customer.wallet.money)
        self.assertEqual(length,91)


    def test_empty_list(self):
        """Pass in an empty list, test that the len of money list remained the same"""
        coins = []
        self.customer.add_coins_to_wallet(coins)
        length = len(self.customer.wallet.money)
        self.assertEqual(length,88)

    
        
class test_add_can_to_backpack(unittest.TestCase):
    """Test for customers add can to backpack function"""

    def setUp(self):
        self.customer = Customer()
        self.backpack = Backpack()

    def test_add_can(self):
        """Pass in a Cola object, test that the len of the customer's backpack's purchased_case list went up by 1""" 
        cola = Cola()
        self.customer.add_can_to_backpack(cola)
        length = len(self.customer.backpack.purchased_cans)
        self.assertEqual(length,1)



if __name__ == '__main__':
    unittest.main() 