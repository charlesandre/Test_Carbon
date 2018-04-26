import unittest
import numpy as np
import sys
sys.path.insert(0, './sources')
import reader
import writer
import move
import map_info

class TestStringMethods(unittest.TestCase):

##  Test for reader

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
            ['Toto',3,2,'E','AADADAGGA', 0],
            ['Lara',1,1,'S','AADADAGGA', 0]
        ]
        self.assertEqual(expected_characters, result)

    def test_general_input(self):
        input_file = 'sources/test_input.txt'
        result = reader.read_all_input(input_file)
        expect_result = {
            'map_size':[3, 4],
            'moutains':[(1,0),(2,1)],
            'treasures':[(0,3,2),(1,3,3)],
            'characters':[
                ['Toto',3,2,'E','AADADAGGA', 0],
                ['Lara',1,1,'S','AADADAGGA', 0]
            ]
        }
        self.assertEqual(expect_result, result)


## Test for writer

    def test_format_output(self):
        test_data = {
            'map_size':[3, 4],
            'moutains':[(1,0)],
            'treasures':[(0,3,2)],
            'characters':[
                ['Lara',1,1,'S','AADADAGGA', 3]
            ]
        }
        result = writer.format_data(test_data)
        self.assertEqual("C - 3 - 4\nM - 1 - 0\nT - 0 - 3 - 2\nA - Lara - 1 - 1 - S - 3\n", result)


## Test move element

    def test_move_action(self):
        raw_data  = {
            'map_size':[3, 4],
            'moutains':[(1,0),(2,1)],
            'treasures':[(0,3,2),(1,3,3)],
            'characters':[
                ['Toto',3,2,'E','AADADAGGA', 0],
                ['Lara',1,1,'S','DADADAGGA', 0]
            ]
        }
        result_data = move.move(raw_data, 'Lara')
        self.assertEqual(result_data, {
            'map_size':[3, 4],
            'moutains':[(1,0),(2,1)],
            'treasures':[(0,3,2),(1,3,3)],
            'characters':[
                ['Toto',3,2,'E','AADADAGGA', 0],
                ['Lara',1,1,'O','ADADAGGA', 0]
            ]
        })


    def test_modify_dir(self):
        test_char = ['Toto',3,2,'E','DADADAGGA', 0]
        result = move.modify_direction(test_char)
        self.assertEqual(result, ['Toto',3,2,'S','ADADAGGA', 0])


    def test_element_case(self):
        test_data = {
            'map_size':[3, 4],
            'moutains':[(1,0),(2,1)],
            'treasures':[(0,3,2),(1,3,3)],
            'characters':[
                ['Toto',3,2,'E','AADADAGGA', 0],
                ['Lara',1,1,'S','AADADAGGA', 0]
            ]
        }
        result = map_info.info_case(test_data, 1, 3)
        self.assertEqual(result, 1)


if __name__ == '__main__':
    unittest.main()