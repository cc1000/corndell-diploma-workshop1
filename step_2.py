import calculator

def process_line(line):
    line_components = line.split(" ")
    operator = line_components[1]
    value1 = float(line_components[2])
    value2 = float(line_components[3])

    print(f"{value1} {operator} {value2} = {calculator.calculate(operator, value1, value2)}")

with open("step_2.txt") as file:
    [process_line(line) for line in file.readlines()]