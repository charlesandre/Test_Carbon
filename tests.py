import unittest
import filecmp
from sources import io
from sources import map_info
from sources import move
import run

class TestStringMethods(unittest.TestCase):

##  Test for io

    def test_map_size(self):
        input_file = 'data/tests/test_input.txt'
        result = io.read_size_map(input_file)
        self.assertEquals([3, 4], result)

    def test_mountains_read(self):
        input_file = 'data/tests/test_input.txt'
        result = io.read_all_mountains(input_file)
        self.assertEqual([[1,0],[2,1]], result)

    def test_treasures_read(self):
        input_file = 'data/tests/test_input.txt'
        result = io.read_all_treasures(input_file)
        self.assertEqual([[0,3,2],[1,3,3]], result)

    def test_characters_read(self):
        input_file = 'data/tests/test_input.txt'
        result = io.read_all_characters(input_file)
        expected_characters = [
            ['Lara',1,1,'S','AADADAGGA', 0]
        ]
        self.assertEqual(expected_characters, result)

    def test_general_input(self):
        input_file = 'data/tests/test_input.txt'
        result = io.read_all_input(input_file)
        expect_result = {
            'map_size':[3, 4],
            'moutains':[[1,0],[2,1]],
            'treasures':[[0,3,2],[1,3,3]],
            'characters':[
                ['Lara',1,1,'S','AADADAGGA', 0]
            ]
        }
        self.assertEqual(expect_result, result)

    def test_valid_map(self):
        test_data = {
            'map_size':[3, 4],
            'moutains':[[1,0],[2,1]],
            'treasures':[[0,4,2],[1,3,3]],
            'characters':[
                ['Toto',2,1,'E','AADADAGGA', 0],
                ['Lara',1,1,'S','AADADAGGA', 0]
            ]
        }
        result = map_info.is_map_valid(test_data)
        self.assertEqual(result[0], False)

## Test for io

    def test_format_output(self):
        test_data = {
            'map_size':[3, 4],
            'moutains':[[1,0]],
            'treasures':[[0,3,2]],
            'characters':[
                ['Lara',1,1,'S','AADADAGGA', 3]
            ]
        }
        result = io.format_data(test_data)
        self.assertEqual("C - 3 - 4\nM - 1 - 0\nT - 0 - 3 - 2\nA - Lara - 1 - 1 - S - 3\n", result)

    def test_output_file(self):
        test_data = "C - 3 - 4\nM - 1 - 0\nT - 0 - 3 - 2\nA - Lara - 1 - 1 - S - 3\n"
        output_file = 'data/tests/output.txt'
        result = io.output_data(test_data, output_file)
        file1 = "data/tests/output.txt"
        file2 = "data/tests/expected_output.txt"
        self.assertEqual(filecmp.cmp(file1, file2), True)

## Test move element
    # Change direction
    def test_move_action_1(self):
        raw_data  = {
            'map_size':[3, 4],
            'moutains':[[1,0],[2,1]],
            'treasures':[[0,3,2],[1,3,3]],
            'characters':[
                ['Toto',3,2,'E','AADADAGGA', 0],
                ['Lara',1,1,'S','DADADAGGA', 0]
            ]
        }
        result_data = move.move(raw_data, 'Lara')
        self.assertEqual(result_data, {
            'map_size':[3, 4],
            'moutains':[[1,0],[2,1]],
            'treasures':[[0,3,2],[1,3,3]],
            'characters':[
                ['Toto',3,2,'E','AADADAGGA', 0],
                ['Lara',1,1,'O','ADADAGGA', 0]
            ]
        })

        # Can't move beacause outside of bounds

    def test_move_action_2(self):
        raw_data  = {
            'map_size':[2, 2],
            'moutains':[[1,0],[2,1]],
            'treasures':[[0,3,2],[1,3,3]],
            'characters':[
                ['Toto',2,2,'E','AADADAGGA', 0],
                ['Lara',1,1,'S','DADADAGGA', 0]
            ]
        }
        result_data = move.move(raw_data, 'Toto')
        self.assertEqual(result_data,{
            'map_size':[2, 2],
            'moutains':[[1,0],[2,1]],
            'treasures':[[0,3,2],[1,3,3]],
            'characters':[
                ['Toto',2,2,'E','ADADAGGA', 0],
                ['Lara',1,1,'S','DADADAGGA', 0]
            ]
        })

        #Can move but into a treasure

    def test_move_action_3(self):
        raw_data  = {
            'map_size':[4, 4],
            'moutains':[[1,0]],
            'treasures':[[0,2,1],[1,2,3]],
            'characters':[
                ['Toto',1,1,'S','AADADAGGA', 0],
                ['Lara',1,1,'S','DADADAGGA', 0]
            ]
        }
        result_data = move.move(raw_data, 'Toto')
        self.assertEqual(result_data,{
            'map_size':[4, 4],
            'moutains':[[1,0]],
            'treasures':[[0,2,1],[1,2,2]],
            'characters':[
                ['Toto',1,2,'S','ADADAGGA', 1],
                ['Lara',1,1,'S','DADADAGGA', 0]
            ]
        })

        #Can move to an empty space

    def test_move_action_4(self):
        raw_data  = {
            'map_size':[4, 4],
            'moutains':[[1,0],[2,1]],
            'treasures':[[0,3,2]],
            'characters':[
                ['Toto',1,1,'S','AADADAGGA', 0]
            ]
        }
        result_data = move.move(raw_data, 'Toto')
        self.assertEqual(result_data,{
            'map_size':[4, 4],
            'moutains':[[1,0],[2,1]],
            'treasures':[[0,3,2]],
            'characters':[
                ['Toto',1,2,'S','ADADAGGA', 0]
            ]
        })

    def test_modify_dir(self):
        test_char = ['Toto',3,2,'E','DADADAGGA', 0]
        result = move.modify_direction(test_char)
        self.assertEqual(result, ['Toto',3,2,'S','DADADAGGA', 0])

    def test_element_case(self):
        test_data = {
            'map_size':[3, 4],
            'moutains':[[1,0],[2,1]],
            'treasures':[[0,3,2],[1,3,3]],
            'characters':[
                ['Toto',3,2,'E','AADADAGGA', 0],
                ['Lara',1,1,'S','AADADAGGA', 0]
            ]
        }
        result = map_info.info_case(test_data, 1, 3)
        self.assertEqual(result, 1)

    def test_remove_last_move(self):
        test_char = ['Toto',3,2,'E','AADADAGGA', 0]
        result_char = move.remove_last_move(test_char)
        self.assertEqual(result_char, ['Toto',3,2,'E','ADADAGGA', 0])

    def test_remove_treasure(self):
        test_data = {
            'map_size':[3, 4],
            'moutains':[[1,0],[2,1]],
            'treasures':[[0,3,2],[1,3,3]],
            'characters':[
                ['Toto',3,2,'E','AADADAGGA', 0],
                ['Lara',1,1,'S','DADADAGGA', 0]
            ]
        }
        result = move.remove_one_treasure(test_data, 0, 3)
        self.assertEqual(result, {
            'map_size':[3, 4],
            'moutains':[[1,0],[2,1]],
            'treasures':[[0,3,1],[1,3,3]],
            'characters':[
                ['Toto',3,2,'E','AADADAGGA', 0],
                ['Lara',1,1,'S','DADADAGGA', 0]
            ]
        })

    def test_add_point(self):
        test_char = ['Toto',1,1,'S','AADADAGGA', 0]
        result = move.add_one_point(test_char)
        self.assertEqual(result, ['Toto',1,1,'S','AADADAGGA', 1])

    def test_general(self):
        input_file = "data/tests/test_input.txt"
        target = "data/tests/test_result.txt"
        expected_result = "data/tests/test_expected_result.txt"
        result = run.run(input_file, target)
        if result:
            self.assertEqual(filecmp.cmp(target, expected_result), True)



if __name__ == '__main__':
    unittest.main()
