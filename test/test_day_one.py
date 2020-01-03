from lib.day_one import DayOne

def test_read_file():
    day_one = DayOne()
    assert day_one.read('./test/test_day_one.txt') == [1.0, 2.0, 3.0]

def test_divide_mass():
    day_one = DayOne()
    mass = 12.0
    assert day_one.divide(mass) == 4.0

def test_round_down():
    day_one = DayOne()
    divided_mass = 4.9
    assert day_one.round_down(divided_mass) == 4

def test_subtract_two():
    day_one = DayOne()
    rounded_down_mass = 4.0
    assert day_one.subtract_two(rounded_down_mass) == 2.0

def test_calculate_fuel():
    day_one = DayOne()
    mass = 12.0
    assert day_one.calculate_fuel(mass) == 2

def test_calculate_total_fuel():
    day_one = DayOne()
    assert day_one.calculate_total_fuel('./test/test_day_one.txt') == -5

