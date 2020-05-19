import calculator

def process_line(line):
    line_components = line.split(" ")
    operator = line_components[1]
    value1 = float(line_components[2])
    value2 = float(line_components[3])

    print(f"{value1} {operator} {value2} = {calculator.calculate(operator, value1, value2)}")

def process_command_line(line, input_file_lines):
    line_components = line.split(" ")
    line_number_to_evaluate = 0

    temp = len(input_file_lines)

    if len(line_components) == 2:
        line_number_to_evaluate = int(line_components[1])
    else:
        line_number_to_evaluate = calculator.calculate(line_components[2], int(line_components[3]), int(line_components[4]))

    print(f"Command: {line} resolves to input line {line_number_to_evaluate}.")

    input_line = input_file_lines[line_number_to_evaluate - 1]

    process_line(input_line)

with open("step_2.txt") as file:
    input_file_lines = file.readlines()

with open("step_3.txt") as command_file:
    [process_command_line(line, input_file_lines) for line in command_file.readlines()]