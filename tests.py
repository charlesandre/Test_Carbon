import unittest
import numpy as np
import sys
sys.path.insert(0, './sources')
import reader


class TestStringMethods(unittest.TestCase):

    def test_map_size(self):
        input_file = 'sources/test_input.txt'
        result = reader.read_size_map(input_file)
        self.assertEquals([3, 4], result)

    def test_mountains_read(self):
        input_file = 'sources/test_input.txt'
        result = reader.read_all_mountains(input_file)
        self.assertEqual([(1,0),(2,1)], result)
        
    def test_treasures_read(self):
        input_file = 'sources/test_input.txt'
        result = reader.read_all_treasures(input_file)
        self.assertEqual([(0,3,2),(1,3,3)], result)

    def test_characters_read(self):
        input_file = 'sources/test_input.txt'
        result = reader.read_all_characters(input_file)
        expected_characters = [
            ['Lara',1,1,'S','AADADAGGA'],
            ['Toto',3,2,'E','AADADAGGA']
        ]
        self.assertEqual(expected_characters, result)

if __name__ == '__main__':
    unittest.main()