from infrastructure.task import Task

"""Day 2: Dive!"""

class TaskImpl(Task):
    input = ""

    def __init__(self, input) -> None:
        self.input = list(map(self.sanitize, input))

    def solution1(self):
        horizontal = 0
        depth = 0
        for direction, units in self.input:
            if direction == "forward":
                horizontal += units
            elif direction == "down":
                depth += units
            elif direction == "up":
                depth -= units
        return horizontal * depth

    def solution2(self):
        horizontal = 0
        depth = 0
        aim = 0
        for direction, units in self.input:
            if direction == "forward":
                horizontal += units
                depth += (aim * units)
            elif direction == "down":
                aim += units
            elif direction == "up":
                aim -= units
        return horizontal * depth

    def sanitize(self, x):
        x = x.split()
        return (x[0], int(x[1]))
