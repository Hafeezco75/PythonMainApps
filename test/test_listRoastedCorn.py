import random
import unittest

from listRoastedCorn import create_list, lengthoflist, even_elements_in_list, odd_elements_in_list, average_elements_in_list, largest_elements_in_list, smallest_elements_in_list, sum_elements_at_oddpositions_in_tuple, sum_elements_at_evenpositions_in_tuple, add_elements_to_tuple, create_tuple, unpack_first_five_elements_in_tuple, create_dictionary, populate_dictionary, sort_dictionary_by_key, sort_dictionary_by_value

class MyTestCase(unittest.TestCase):
    def test_that_number_returns_ten_same_random_numbers(self):
        self.assertEqual(create_list(random.seed), [40, 17, 48, 23, 45, 48, 42, 34, 2, 30])  # add assertion here

    def test_that_returns_length_of_list(self):
        self.assertEqual(lengthoflist(random.seed), 10)

    def test_that_adds_list_of_all_even_numbers(self):
        self.assertEqual(even_elements_in_list(random.seed), 244)

    def test_that_adds_list_of_odd_numbers(self):
        self.assertEqual(odd_elements_in_list(random.seed), 85)

    def test_that_calculate_the_average_of_all_numbers(self):
        self.assertEqual(average_elements_in_list(random.seed), 32.9)

    def test_that_returns_the_largest_number_in_list(self):
        self.assertEqual(largest_elements_in_list(random.seed), 48)

    def test_that_returns_the_smallest_number_in_list(self):
        self.assertEqual(smallest_elements_in_list(random.seed), 4)

    def test_that_create_new_tuple(self):
        self.assertEqual(create_tuple(), None)
    def test_that_add_integers_to_tuple(self):
        self.assertEqual(add_elements_to_tuple(), (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20))

    def test_that_sum_even_positions_in_tuple(self):
        self.assertEqual(sum_elements_at_evenpositions_in_tuple(), 110)

    def test_that_sum_odd_positions_in_tuple(self):
        self.assertEqual(sum_elements_at_oddpositions_in_tuple(), 100)

    def test_that_returns_first_five_elements_in_tuple(self):
        self.assertEqual(unpack_first_five_elements_in_tuple(), (1, 2, 3, 4, 5))

    def test_that_create_an_empty_dictionary(self):
        self.assertEqual(create_dictionary(), None)

    def test_that_sort_dictionary_by_key(self):
        self.assertEqual(sort_dictionary_by_key(), ['Bola Ige', 'Esther Chukwu', 'Ade Badmus', 'Smart Uzor', 'David Adeleye', 'Alonge Stella', 'Bisola Mariam', 'Francis kennedy', 'Mba Chineye', 'Victor Ikpeba'])

    def test_that_sort_dictionary_by_value(self):
        self.assertEqual(sort_dictionary_by_value(), [15, 20, 23, 18, 22, 21, 19, 17, 18, 22])

    def test_that_populate_dictionary(self):
        self.assertEqual(populate_dictionary(), {'Bola Ige': 15, 'Esther Chukwu': 20, 'Ade Badmus': 23, 'Smart Uzor': 18, 'David Adeleye': 22, 'Alonge Stella': 21, 'Bisola Mariam': 19, 'Francis kennedy': 17, 'Mba Chineye': 18, 'Victor Ikpeba': 22}
)

if __name__ == '__main__':
    unittest.main()
