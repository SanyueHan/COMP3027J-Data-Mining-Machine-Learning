from utils import *


def augment(line):
    return_list = list(map(float, line.rstrip("\n").split(",")))
    output = return_list.pop()
    inputs = return_list
    average = sum(inputs) / len(inputs)
    variance = sum([(i-average)**2 for i in inputs]) / len(inputs)
    inputs = [i/variance for i in inputs]

    return ','.join(map(str, inputs+[output])) + "\n"


def main():
    for name in sorted(os.listdir(PRE)):
        with open(PRE+name, "r") as file:
            data = [line for line in file]
        data.pop(0)
        try:
            data = [augment(line) for line in data]
        except ZeroDivisionError:
            print(name)
        with open(AUG+name, "w") as file:
            file.write(','.join([f"{i}_augmented" for i in range(LEN, 0, -1)] + ["target"]) + '\n')
            file.writelines(data)


if __name__ == "__main__":
    main()
