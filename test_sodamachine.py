import unittest
from unittest.case import TestCase
from soda_machine import SodaMachine
import coins

class fill_register(unittest.TestCase):
    """Test soda machine fill register function"""
    def setUp(self):
        self.register = SodaMachine()

    def test_register_list_length(self):
        """Instantiate a SodaMachine object, test that its register list has a len of 88"""
        length = len(self.register.register)
        self.assertEqual(length,88)
        

class fill_inventory(unittest.TestCase):
    """Test soda machine fill inventory function"""

    def setUp(self):
        self.inventory = SodaMachine()

    def test_inventory_list_length(self):
        """Instantiate a SodaMachine object, test that its inventory list has a len of 30"""
        length = len(self.inventory.inventory)
        self.assertEqual(length,30)


class get_coin_from_register(unittest.TestCase):
    """Test soda machine get coin from register function"""

    def setUp(self):
        self.get_coin_from_register = SodaMachine()

    def test_return_coin_quarter(self):
        """Test each type of coin can be returned from register"""
        coin = self.get_coin_from_register.get_coin_from_register('Quarter')
        self.assertEqual('Quarter',coin.name)

    def test_return_coin_dime(self):
        coin = self.get_coin_from_register.get_coin_from_register('Dime')
        self.assertEqual('Dime',coin.name)

    def test_return_coin_nickel(self):
        coin = self.get_coin_from_register.get_coin_from_register('Nickel')
        self.assertEqual('Nickel',coin.name)

    def test_return_coin_penny(self):
        coin = self.get_coin_from_register.get_coin_from_register('Penny')
        self.assertEqual('Penny',coin.name)


    def test_invalid_coin(self):
        """Test that passing in a string that is not a valid coin name will return None"""
        coin = self.get_coin_from_register.get_coin_from_register('Dollar')
        self.assertIsNone(None)
        

class test_register_has_coin(unittest.TestCase):
    """Test soda machine test register has coin function"""
    
    def setUp(self):
        self.register_has_coin = SodaMachine()
   
    def test_each_coin_quarter(self):
        """Test that each type of coin will return True"""
        result = self.register_has_coin.register_has_coin('Quarter')
        self.assertTrue(result) 

    def test_each_coin_dime(self):
        result = self.register_has_coin.register_has_coin('Dime')
        self.assertTrue(result) 

    
    def test_each_coin_nickel(self):
        result = self.register_has_coin.register_has_coin('Nickel')
        self.assertTrue(result) 

    def test_each_coin_penny(self):
        result = self.register_has_coin.register_has_coin('Penny')
        self.assertTrue(result) 
    
    
    
    def test_invalid_coin(self):
        """Test that a non-valid coin name will return False"""
     
    def test_invalid_coin(self):
        coin = self.register_has_coin.register_has_coin('Dollar')
        self.assertFalse(None)

    
    
class determine_change_value(unittest.TestCase):
    """Test soda machine determine change value function"""
    
    def setUp(self):
        self.

    def test_payment_higer(self):
        """Test with total payment higher"""

    def test_soda_price(self):
        """Test with select_soda_price_higher"""

    def test_equal_values(self):
        """Test with two eqaul values"""

class caculate_coin_value(unittest.TestCase):
    """Test soda machine caculate coin value function"""
    
    def setUp(self):
        pass

    def test_coin_value_check(self):
        """Instantiate each of the 4 coin types and append them to a list. Pass the list into this function, ensure the returned values is .41"""

    def test_empty_list(self):
       """ Pass in an empty list. Ensure the returned value is 0.""" 

class get_inventory_soda(unittest._TestCase):
    """test soda machine get inventory soda functiion"""
    
    def setUp(self):
        pass
    
    def test_equal_name(self):
        """Pass in each of the 3 soda names, ensure the returned can has the same name"""

    def test_mountain_dew(self):
        """Pass in Mountain Dew and ensure None is returned"""

class return_inventory(unittest.TestCase):
    """Test soda machine return inventory function"""
    
    def setUp(self):
        pass
    
    def test_inventory_length(self):
        """Instantiate a can and pass it into the method. Test that the len of self.inventory is now 31"""

class deposit_coins_into_register(unittest.TestCase):
    """Test soda machine deposit coins into register function"""
    
    def setUp(self):
        pass

    def test_register_len(self):
        """Instantiate each of the 4 coins and append them to a list. Pass the list into the function, ensure the len of self.register is 92"""

if __name__ == '__main__':
    unittest.main()






    


