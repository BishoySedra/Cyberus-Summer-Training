def execute(num1, num2, op):
    if op == "+":
        return num1 + num2
    elif op == "-":
        return num1 - num2
    elif op == "*":
        return num1 * num2
    elif op == "/":
        if num2 == 0:
            return "Can't solve"
        return num1 // num2


isContinued = True

while isContinued:
    num1 = int(input("Enter 1st number: "))
    num2 = int(input("Enter 1st number: "))
    op = input("Choose the operator: ")
    if op == "exit":
        break

    print(execute(num1, num2, op))

    option = input("Continue? ")
    if option.lower() == "yes":
        isContinued = True
    else:
        isContinued = False
