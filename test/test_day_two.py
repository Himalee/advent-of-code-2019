from lib.day_two import DayTwo

INPUT = [1,0,0,3,1,1,2,3,1,3,4,3,1,5,0,3,2,1,6,19,1,9,19,23,2,23,10,27,1,27,5,31,1,31,6,35,1,6,35,39,2,39,13,43,1,9,43,47,2,9,47,51,1,51,6,55,2,55,10,59,1,59,5,63,2,10,63,67,2,9,67,71,1,71,5,75,2,10,75,79,1,79,6,83,2,10,83,87,1,5,87,91,2,9,91,95,1,95,5,99,1,99,2,103,1,103,13,0,99,2,14,0,0]

def test_find_correct_numbers_and_add():
    day_two = DayTwo()
    assert day_two.op_one([1, 2, 3, 4, 5, 3, 7, 8]) == [1, 2, 3, 4, 7, 3, 7, 8]

def test_find_correct_number_and_multiply():
    day_two = DayTwo()
    assert day_two.op_two([2, 2, 1, 4, 5, 3, 7, 8]) == [2, 2, 1, 4, 2, 3, 7, 8]

def test_find_sub_array_starting_with_one():
    day_two = DayTwo()
    assert day_two.find_sub_array([2, 9, 1, 4, 5, 3, 7, 8]) == [1, 4, 5, 3]

def test_find_sub_array_starting_with_two():
    day_two = DayTwo()
    assert day_two.find_sub_array([2, 9, 1, 4, 5, 3, 7, 8]) == [2, 9, 1, 4]

