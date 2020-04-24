class DayTwo:

    def op_one(self, array):
        position_one = array[1]
        position_two = array[2]
        position_three = array[3]
        value_one = array[position_one]
        value_two = array[position_two]

        total_value = value_one + value_two
        array[position_three] = total_value
        return array

    def op_two(self, array):
        position_one = array[1]
        position_two = array[2]
        position_three = array[3]
        value_one = array[position_one]
        value_two = array[position_two]

        total_value = value_one * value_two
        array[position_three] = total_value
        return array

    def find_sub_array(self, array):
        element_index = 0
        for el in array:
            print("el", el)
            if el == 2:
                element_index = array.index(el)
                print("el index", element_index)
            elif el == 1:
                element_index = array.index(el)
        return array[element_index:(element_index + 4)]

