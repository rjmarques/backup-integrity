import unittest
import os

from backup_integrity.integrity import compare

class TestCompare(unittest.TestCase):
    def test_same_contents(self):        
        testdata_root = os.path.dirname(__file__)

        file_a = os.path.join(testdata_root, "test_data/main_backup/binary_1")
        file_b = os.path.join(testdata_root, "test_data/secondary_backup/binary_1")

        self.assertTrue(compare(file_a, file_b))

    def test_different_files(self):        
        testdata_root = os.path.dirname(__file__)

        file_a = os.path.join(testdata_root, "test_data/main_backup/binary_1")
        file_b = os.path.join(testdata_root, "test_data/secondary_backup/py_logo.png")

        self.assertFalse(compare(file_a, file_b))
    
    def test_same_filename_different_content(self):        
        testdata_root = os.path.dirname(__file__)

        file_a = os.path.join(testdata_root, "test_data/main_backup/text/text_2")
        file_b = os.path.join(testdata_root, "test_data/tertiary_backup/text/text_2")

        self.assertFalse(compare(file_a, file_b))