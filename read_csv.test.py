import read_csv
import unittest

class readCSVTest(unittest.TestCase):
    def test_no_input(self):
        search = ""
        self.assertEqual(read_csv.csv_search(search), "No results found for ", "Expected csv_search('') to return 'No results found for'")

    def test_process_not_found(self):
        search = "NGO777"
        self.assertEqual(read_csv.csv_search(search), "No results found for NGO777", "Expected csv_search('ngo777') to return 'No results found for NGO777")

    def test_process_found(self):
        search = "NGO101"
        self.assertEqual(read_csv.csv_search(search), "{'NGO101': {'Controller': 'Tony', 'Backup': 'Bob', 'ENV': '6.5.1'}}", "Expected csv_search('NGO101') to return {'NGO101': {'Controller': 'Tony', 'Backup': 'Bob', 'ENV': '6.5.1'}}")

    def test_capitalizes_input(self):
        search = "ngo777"
        self.assertEqual(read_csv.csv_search(search), "No results found for NGO777", "Expected csv_search('ngo777') to return 'No results found for NGO777")

    #function should find 101 among NGO101, ABC101, etc.
    def test_search_missing_input(self):
        search = "101"
        self.assertEqual(read_csv.csv_search(search), "{'NGO101': {'Controller': 'Tony', 'Backup': 'Bob', 'ENV': '6.5.1'}}", "Expected csv_search('NGO101') to return {'NGO101': {'Controller': 'Tony', 'Backup': 'Bob', 'ENV': '6.5.1'}}")

unittest.main()