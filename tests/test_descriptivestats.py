import unittest
import sys
import os

current_dir = os.path.dirname(os.path.abspath(__file__))
parent_dir = os.path.abspath(os.path.join(current_dir, ".."))
sys.path.insert(0, parent_dir)

from src.DescriptiveStatistics import describe_data as dd

class TestImportDataFunction(unittest.TestCase):

    def test_correct_data_type(self):
        # This should not raise an error
        try:
            dd("testdata.csv")
        except TypeError:
            self.fail("TypeError raised for correct data type")

    def test_incorrect_data_type(self):
        # This should raise a TypeError
        with self.assertRaises(TypeError):
            dd(42)

    def test_unknown_file(self):
        # This should raise a FileNotFoundError
        with self.assertRaises(FileNotFoundError):
            dd("fake_data.csv")

if __name__ == '__main__':
    unittest.main()