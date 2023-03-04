from read_csv import csv_search
import unittest

class readCSVTest(unittest.TestCase):
    def test_no_input(self):
        self.assertEqual(csv_search(""), "No results found for ", "Expected csv_search('') to return 'No results found for'")

    def test_process_not_found(self):
        self.assertEqual(csv_search("NGO777"), "No results found for NGO777", "Expected csv_search('ngo777') to return 'No results found for NGO777")

    def test_process_found(self):
        self.assertEqual(csv_search("NGO101"), "{'NGO101': {'Controller': 'Tony', 'Backup': 'Bob', 'ENV': '6.5.1'}}", "Expected csv_search('NGO101') to return {'NGO101': {'Controller': 'Tony', 'Backup': 'Bob', 'ENV': '6.5.1'}}")

    def test_capitalizes_input(self):
        self.assertEqual(csv_search("ngo777"), "No results found for NGO777", "Expected csv_search('ngo777') to return 'No results found for NGO777")

    #function should find 101 among NGO101, ABC101, etc.
    def test_search_missing_input(self):
        self.assertEqual(csv_search("101"), "{'NGO101': {'Controller': 'Tony', 'Backup': 'Bob', 'ENV': '6.5.1'}}", "Expected csv_search('NGO101') to return {'NGO101': {'Controller': 'Tony', 'Backup': 'Bob', 'ENV': '6.5.1'}}")

unittest.main()