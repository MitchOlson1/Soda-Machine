import unittest
from soda_machine import SodaMachine

class fill_register(unittest.TestCase):
    """"""

    def setUp(self):
        pass

    def test_register_list_length(self):
        """Instantiate a SodaMachine object, test that its register list has a len of 88"""
        pass

class fill_inventory(unittest.TestCase):
    """"""

    def setUp(self):
        pass

    def test_inventory_list_length(self):
        """Instantiate a SodaMachine object, test that its inventory list has a len of 30"""
        pass

class get_coin_from_register(unittest.TestCase):
    """"""

    def setUp(self):
        pass

    def test_return_coin(self):
        """Test each type of coin can be returned from register"""
        pass

    def test_invalid_coin(self):
        """Test that passing in a string that is not a valid coin name will return None"""
        pass

    """"""
    """"""
class test_register_has_coin(unittest.TestCase):
    
    def setUp(self):
        pass
   
    def test_each_coin(self):
        """Test that each type of coin will return True"""
    
    def test_invalid_coin(self):
        """Test that a non-valid coin name will return False"""

    
    
class determine_change_value(unittest.TestCase):

    def setUp(self):
        pass

    def test_payment_higer(self):
        """Test with total payment higher"""

    def test_soda_price(self):
        """Test with select_soda_price_higher"""

    def test_equal_values(self):
        """Test with two eqaul values"""


