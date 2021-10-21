import unittest
from cans import Can, Cola
from soda_machine import SodaMachine
import coins

class test_fill_register(unittest.TestCase):
    """Test soda machine fill register function"""
    def setUp(self):
        self.register = SodaMachine()

    def test_register_list_length(self):
        """Instantiate a SodaMachine object, test that its register list has a len of 88"""
        length = len(self.register.register)
        self.assertEqual(length,88)
        

class test_fill_inventory(unittest.TestCase):
    """Test soda machine fill inventory function"""

    def setUp(self):
        self.inventory = SodaMachine()

    def test_inventory_list_length(self):
        """Instantiate a SodaMachine object, test that its inventory list has a len of 30"""
        length = len(self.inventory.inventory)
        self.assertEqual(length,30)


class test_get_coin_from_register(unittest.TestCase):
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

    
    
class test_determine_change_value(unittest.TestCase):
    """Test soda machine determine change value function"""
    
    def setUp(self):
        self.determine_change_value = SodaMachine()

    def test_payment_higer(self):
        """Test with total payment higher"""
        amount = self.determine_change_value.determine_change_value(5,2)
        self.assertEquals(amount,3)

    def test_soda_price(self):
        """Test with select_soda_price_higher"""
        amount = self.determine_change_value.determine_change_value(2,5)
        self.assertEquals(amount,-3)

    def test_equal_values(self):
        """Test with two eqaul values"""
        amount = self.determine_change_value.determine_change_value(2,2)
        self.assertEquals(amount,0)



class test_caculate_coin_value(unittest.TestCase):
    """Test soda machine caculate coin value function"""
    
    def setUp(self):
        self.caculate_coin_value = SodaMachine()
        

    def test_coin_value_check(self):
        """Instantiate each of the 4 coin types and append them to a list. Pass the list into this function, ensure the returned values is .41"""
        
        Quarter = coins.Quarter()
        Dime = coins.Dime()
        Nickel = coins.Nickel()
        Penny = coins.Penny()
        coinlist = [Quarter,Dime,Nickel,Penny]
        value_of_coins = self.caculate_coin_value.calculate_coin_value(coinlist)
        self.assertEquals(value_of_coins,.41)

    
    def test_empty_list(self):
       """ Pass in an empty list. Ensure the returned value is 0."""
       coinlist = []
       value_of_coins = self.caculate_coin_value.calculate_coin_value(coinlist)
       self.assertEquals(value_of_coins,0)



class test_get_inventory_soda(unittest.TestCase):
    """test soda machine get inventory soda functiion"""
    
    def setUp(self):
        self.get_inventory_soda = SodaMachine()
    
    def test_equal_name_cola(self):
        """Pass in each of the 3 soda names, ensure the returned can has the same name"""
        resultCola = self.get_inventory_soda.get_inventory_soda('Cola')
        self.assertEqual(resultCola.name,'Cola')

    
    def test_equal_name_beer(self):
        resultRootBeer = self.get_inventory_soda.get_inventory_soda('Root Beer')
        self.assertEqual(resultRootBeer.name,'Root Beer')

        
    def test_equal_name_orange(self):
        resultOrangeSoda = self.get_inventory_soda.get_inventory_soda('Orange Soda')
        self.assertEqual(resultOrangeSoda.name,'Orange Soda')


    
    def test_mountain_dew(self):
        """Pass in Mountain Dew and ensure None is returned"""
        result = self.get_inventory_soda.get_inventory_soda('Mountain Dew')
        self.assertIsNone(None)





class test_return_inventory(unittest.TestCase):
    """Test soda machine return inventory function"""
    
    def setUp(self):
        self.inventory = SodaMachine()
    
    def test_inventory_length(self):
        """Instantiate a can and pass it into the method. Test that the len of self.inventory is now 31"""
        soda = Cola 
        self.inventory.return_inventory(soda)
        length = len(self.inventory.inventory)
        self.assertEqual(length,31)



class test_deposit_coins_into_register(unittest.TestCase):
    """Test soda machine deposit coins into register function"""
    
    def setUp(self):
        self.register = SodaMachine()

    def deposit_coins_into_register(self):
        """Instantiate each of the 4 coins and append them to a list. Pass the list into the function, ensure the len of self.register is 92"""
        Quarter = coins.Quarter()
        Dime = coins.Dime()
        Nickel = coins.Nickel()
        Penny = coins.Penny()
        coinlist = [Quarter,Dime,Nickel,Penny]
        self.deposit_coins_into_register(coinlist)
        length = len(self.register.register)
        self.assertEqual(length,92)


if __name__ == '__main__':
    unittest.main()






    


