import calculator

user_input = input("Input calculation (in form 'operator,value1,value2', eg '+,1,2'): ")

user_input_components = user_input.split(" ")
operator = user_input_components[0]
value1 = float(user_input_components[1])
value2 = float(user_input_components[2])

print(f"Evaluating {value1} {operator} {value2}")

print(f'Result: {calculator.calculate(operator, value1, value2)}')