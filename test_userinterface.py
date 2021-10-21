import unittest
from coins import Coin, Dime, Nickel, Penny, Quarter
import user_interface
from cans import Can, Cola, OrangeSoda, RootBeer



class test_validate_main_menu(unittest.TestCase):

    def test_number_pass_one(self):
        """Pass in each number 1-4, ensure the tuple of (True, number) is returned"""
        number_one = user_interface.validate_main_menu(1)
        self.assertEqual(number_one,(True,1))
    
    def test_number_pass_two(self):
        number_two = user_interface.validate_main_menu(2)
        self.assertEqual(number_two,(True,2))

    
    def test_number_pass_three(self):
        number_three = user_interface.validate_main_menu(3)
        self.assertEqual(number_three,(True,3))

    
    def test_number_pass_four(self):
        number_four = user_interface.validate_main_menu(4)
        self.assertEqual(number_four,(True,4))
    

    def test_ensure_false(self):
        """ Pass in a different number, ensure (False, None) is returned"""
        number_nine = user_interface.validate_main_menu(9)
        self.assertEqual(number_nine,(False,None))

class test_try_parse_int(unittest.TestCase):

    def test_pass_10(self):
        """Pass in “10”, ensure the int value 10 is returned"""
        result = user_interface.try_parse_int(10)
        self.assertEqual(result,10)

    def test_pass_hello(self):
        """Pass in “hello”, ensure 0 is returned"""
        result = user_interface.try_parse_int('hello')
        self.assertEqual(result,0)


class test_get_unique_can_names(unittest.TestCase):

    def test_pass_list(self):
        """Instantiate 6 cans (two of each type) and append them to a list. Pass the list into this 
function, ensure the returned list only contains 3 names"""
        cola = Cola()
        Orange_soda = OrangeSoda()
        Root_beer = RootBeer()
        List = [cola,cola,Orange_soda,Orange_soda,Root_beer,Root_beer]
        unique_can_names = user_interface.get_unique_can_names(List)
        self.assertEqual(len(unique_can_names),3)

        

    def test_empty_list(self):
        """ Pass in an empty list. Ensure an empty list is returned"""
        List = []
        unique_can_names = user_interface.get_unique_can_names(List)
        self.assertEqual(len(unique_can_names),0)

class test_display_payment_value(unittest.TestCase):

    def test_ensure_returned_values(self):
        """Instantiate each of the 4 coin types and append them to a list. Pass the list into this 
function, ensure the returned values is .41"""
        quarter = Quarter()
        dime = Dime()
        nickel = Nickel()
        penny = Penny()
        Money = [quarter,dime,nickel,penny]
        value = user_interface.display_payment_value(Money)
        self.assertEqual(value,.41)


    def test_value_0(self):
        """Pass in an empty list. Ensure the returned value is 0."""
        Money = []
        value = user_interface.display_payment_value(Money)
        self.assertEqual(value,0)


class test_validate_coin_selection(unittest.TestCase):

    def test_int_1(self):
        """Pass in each int 1-5, ensure the appropriate tuple is returned."""
        result = user_interface.validate_coin_selection(1)
        self.assertEqual(result,(True,'Quarter'))

    def test_int_2(self):
        result = user_interface.validate_coin_selection(2)
        self.assertEqual(result,(True,'Dime')) 

    def test_int_3(self):
        result = user_interface.validate_coin_selection(3)
        self.assertEqual(result,(True,'Nickel'))

    def test_int_4(self):
        result = user_interface.validate_coin_selection(4)
        self.assertEqual(result,(True,'Penny'))

    def test_int_5(self):
        result = user_interface.validate_coin_selection(5)
        self.assertEqual(result,(True,"Done"))
# 
    
    def test_different_number_random(self):
        """ Pass in a different number, ensure (False, None) is returned."""
        result = user_interface.validate_coin_selection(6)
        self.assertEqual(result,(False,None))
    
    
    
if __name__ == '__main__':
    unittest.main()
  

        