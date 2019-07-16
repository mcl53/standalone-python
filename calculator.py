import math
print("Hello, this is a calculator!")
num1 = input("First number: ")
operation = input("Give an operation: ")
if operation != "sqrt":
    num2 = input("Second number: ")


def check(num):
    try:
        int(num)
    except ValueError:
        return False


def check_whole(value):
    if float(value) == int(value):
        print(int(value))
    else:
        print(float(value))

def calculate(num_1, oper, num_2):
    if oper == "+":
        value = float(num_1) + float(num_2)
        return value
    elif oper == "-":
        value = float(num_1) - float(num_2)
        return value
    elif oper == "*":
        value = float(num_1) * float(num_2)
        return value
    elif oper == "/":
        value = float(num_1) / float(num_2)
        return value
    elif oper == "**":
        value = float(num_1) ** float(num_2)
        return value

def cal_root(num_1):
    value = math.sqrt(float(num_1))
    return value

def check_oper(operator):
    if operator in "+-*/**sqrt":
        return True
    else:
        return False


is_num1 = check(num1)
if is_num1 is not True:
    print("The first value was not a number")
if operation != "sqrt":
    is_num2 = check(num2)
    if is_num2 is not True:
        print("The second value was not a number")

valid_oper = check_oper(operation)
if valid_oper is not True:
    print("The operation is invalid")

if operation != "sqrt":
    if is_num1 and is_num2 and valid_oper:
        value = calculate(num1, operation, num2)
        check_whole(value)
elif operation == "sqrt":
    if is_num1 and valid_oper:
        value = cal_root(num1)
        check_whole(value)
