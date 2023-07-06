import unittest
import os

from backup_integrity.crawler import list_files

class TestListFiles(unittest.TestCase):
    def test_list_correctly(self):
        testdata_root = os.path.dirname(__file__)

        backup_dir = os.path.join(testdata_root, "test_data/main_backup")
        res = list_files(backup_dir)
        
        expected = {
            "text/text_1",
            "text/text_2",
            "text/text_3",
            "binary_1",
            "py_logo.png",
            "unique.webp",
        }
        self.assertSetEqual(expected, res)