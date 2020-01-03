import math

class DayOne:

    def read(self, file_path):
        file_content = open(file_path)
        lines = [float(line) for line in file_content.read().splitlines()]
        return lines

    def divide(self, mass):
        return mass / 3

    def round_down(self, divided_mass):
        return math.floor(divided_mass)

    def subtract_two(self, rounded_mass):
        return rounded_mass - 2

    def calculate_fuel(self, mass):
        divided_mass = self.divide(mass)
        rounded_mass = self.round_down(divided_mass)
        return int(self.subtract_two(rounded_mass))

    def calculate_total_fuel(self, file_path):
        masses = self.read(file_path)
        total_fuel = 0
        for mass in masses:
            total_fuel += self.calculate_fuel(mass)
        print total_fuel
        return total_fuel


if __name__ == '__main__':
    day_one = DayOne()
    day_one.calculate_total_fuel('day-one.txt')
