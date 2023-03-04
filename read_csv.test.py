from read_csv import csv_search
import unittest

class readCSVTest(unittest.TestCase):
    def test_no_input(self):
        self.assertEqual(csv_search(""), "No results found for ", "Expected csv_search('') to return 'No results found for'")

    def test_process_not_found(self):
        self.assertEqual(csv_search("ngo777"), "No results found for NGO777", "Expected csv_search('ngo777') to return 'No results found for NGO777")

# search = "NGO101"

# csv_search(search)
unittest.main()