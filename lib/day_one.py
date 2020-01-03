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

    def calculate_mass_fuel(self, mass):
        return self.calculate_fuel(mass)

    def calculate_total_fuel_for_fuel(self, fuel, running_total):
        if fuel < 0:
            return running_total
        else:
            return self.calculate_total_fuel_for_fuel(self.calculate_fuel(fuel), (running_total + fuel))

    def calculate_all_of_the_fuel(self, file_path):
        masses = self.read(file_path)
        total_fuel = 0
        for mass in masses:
            initial_fuel = self.calculate_mass_fuel(mass)
            total_fuel += self.calculate_total_fuel_for_fuel(initial_fuel, 0)
        print total_fuel
        return total_fuel


if __name__ == '__main__':
    day_one = DayOne()
    day_one.calculate_all_of_the_fuel('day-one.txt')
