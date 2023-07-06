import unittest
import os

from backup_integrity.controller import Controller

class TestController(unittest.TestCase):
    def test_controller_report(self):
        testdata_root = os.path.dirname(__file__)

        root_a = os.path.join(testdata_root, "test_data/main_backup")
        root_b = os.path.join(testdata_root, "test_data/secondary_backup")
        root_c = os.path.join(testdata_root, "test_data/tertiary_backup")

        ctrl = Controller([root_a, root_b, root_c])
        out = ctrl.verify_file_integrity()
    
        self.assertCountEqual(['py_logo.png', 'text/text_1', 'binary_1'],out.valid)
        self.assertDictEqual({
            'text/text_3': [root_b],
            'unique.webp': [root_b, root_c],
        }, out.missing)
        self.assertDictEqual({
            'text/text_2': [(root_a, root_c)]
        }, out.invalid)