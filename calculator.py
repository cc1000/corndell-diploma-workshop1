def calculate(operator, value1, value2):
    if operator == "+": return value1 + value2
    elif operator == "-": return value1 - value2
    elif operator == "x": return value1 * value2
    elif operator == "/": return value1 / value2
    elif operator == "^": return value1 ** value2
    else: raise Exception("Unsupported operator")