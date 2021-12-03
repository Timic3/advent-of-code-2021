from infrastructure.task import Task

"""Day 3: Binary Diagnostic"""

class TaskImpl(Task):
    input = ""

    def __init__(self, input) -> None:
        self.input = input

    def solution1(self):
        gamma = ""
        epsilon = ""
        position = 0
        while True:
            most_common, least_common = self.most_least_common_bit(position)
            if most_common is False:
                break

            gamma += str(most_common)
            epsilon += str(least_common)

            position += 1

        return int(gamma, 2) * int(epsilon, 2)

    def solution2(self):
        oxygen_generator = ""
        co2_scrubber = ""

        oxygen_generator_input = self.input[:]
        co2_scrubber_input = self.input[:]

        position = 0
        while True:
            most_common = self.most_common_bit(oxygen_generator_input, position)
            least_common = self.least_common_bit(co2_scrubber_input, position)

            if (most_common is False and least_common is False) or (len(oxygen_generator_input) == 1 and len(co2_scrubber_input) == 1):
                break

            if most_common is not False and len(oxygen_generator_input) > 1:
                oxygen_generator_input[:] = [binary for binary in oxygen_generator_input if int(binary[position][0]) == most_common]

            if least_common is not False and len(co2_scrubber_input) > 1:
                co2_scrubber_input[:] = [binary for binary in co2_scrubber_input if int(binary[position][0]) == least_common]

            position += 1


        oxygen_generator = oxygen_generator_input[0]
        co2_scrubber = co2_scrubber_input[0]

        return int(oxygen_generator, 2) * int(co2_scrubber, 2)

    def most_common_bit(self, input, position):
        common = [0, 0]
        for binary in input:
            try:
                bit = binary[position]
            except IndexError:
                return False

            common[int(bit)] += 1

        max_bit, min_bit = max(common), min(common)
        return 1 if max_bit == min_bit else common.index(max_bit)

    def least_common_bit(self, input, position):
        common = [0, 0]
        for binary in input:
            try:
                bit = binary[position]
            except IndexError:
                return False

            common[int(bit)] += 1

        max_bit, min_bit = max(common), min(common)
        return 0 if max_bit == min_bit else common.index(min_bit)

    def most_least_common_bit(self, position):
        common = [0, 0]
        for binary in self.input:
            try:
                bit = binary[position]
            except IndexError:
                return False, False

            common[int(bit)] += 1

        return common.index(max(common)), common.index(min(common))
