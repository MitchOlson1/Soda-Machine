import unittest


class validate_main_menu(unittest.TestCase):

    def test_number_pass(self):
        """Pass in each number 1-4, ensure the tuple of (True, number) is returned"""

    def test_ensure_false(self):
        """ Pass in a different number, ensure (False, None) is returned"""

class try_parse_int(unittest.TestCase):

    def test_pass_10(self):
        """Pass in “10”, ensure the int value 10 is returned"""

    def test_pass_hello(self):
        """Pass in “hello”, ensure 0 is returned"""

class get_unique_can_names(unittest.TestCase):

    def test_pass_list(self):
        """Instantiate 6 cans (two of each type) and append them to a list. Pass the list into this 
function, ensure the returned list only contains 3 names"""

    def test_empty_list(self):
        """ Pass in an empty list. Ensure an empty list is returned"""

class display_payment_value(unittest.TestCase):

    def test_ensure_returned_values(self):
        """Instantiate each of the 4 coin types and append them to a list. Pass the list into this 
function, ensure the returned values is .41"""

    def test_value_0(self):
        """Pass in an empty list. Ensure the returned value is 0."""

class validate_coin_selection(unittest.TestCase):

    def test_int(self):
        """Pass in each int 1-5, ensure the appropriate tuple is returned."""

    def test_different_number(self):
        """ Pass in a different number, ensure (False, None) is returned."""

if __name__ == '__main__':
    unittest.main()
  

        