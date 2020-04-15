import unittest
from name_function import get_formatted_name


class NamesTestCase(unittest.TestCase):

    def test_first_last_name(self):
        formatted_name = get_formatted_name('janis', 'joplin')
        self.assertEqual(formatted_name, 'Janis Joplin')

    def test_first_middle_last_name(self):
        formatted_name = get_formatted_name('Alo', 'tim', 'rex')
        self.assertEqual(formatted_name, 'Alo Rex Tim')


unittest.main()
