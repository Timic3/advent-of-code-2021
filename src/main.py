from importlib import import_module
import sys
import os

def main():
    if len(sys.argv[1:]) != 2:
        print("python %s [day] [input file]" % sys.argv[0])
        exit(1)

    day = import_module("advent.%s" % sys.argv[1])

    root_dir = os.path.dirname(os.path.abspath(__file__))
    with open(os.path.join(root_dir, "../assets/%s/%s.in" % (sys.argv[1], sys.argv[2]))) as file:
        input = file.read().splitlines()

    object = day.TaskImpl(input)
    print(object.solution1())
    print(object.solution2())

if __name__ == "__main__":
    main()
