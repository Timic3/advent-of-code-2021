from infrastructure.task import Task

"""Day 1: Sonar Sweep"""

class TaskImpl(Task):
    input = ""

    def __init__(self, input) -> None:
        self.input = list(map(int, input))

    def solution1(self):
        return sum([self.input[i] > self.input[i - 1] for i in range(1, len(self.input))])

    def solution2(self):
        return sum([sum(self.input[i - 3 : i]) < sum(self.input[i - 2 : i + 1]) for i in range(3, len(self.input))])
