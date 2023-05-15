import time
import math

while True:
    print("Choose the calculator:")
    print("1. Normal Calculator")
    print("2. Scientific Calculator")
    print("3. Exit")
    choice = input("Enter choice (1/2/3): ")

    if choice == '1':
        while True:
            print("Select operation:")
            print("1. Addition")
            print("2. Subtraction")
            print("3. Multiplication")
            print("4. Division")
            print("5. Exponents")
            print("6. Exit")

            choice = input("Enter choice (1/2/3/4/5/6): ")

            if choice == '6':
                print("Exiting the calculator", end="")
                for i in range(3):
                    print(".", end="", flush=True)
                    time.sleep(1)
                print()
                break

            equation = input("Enter equation: ")

            if choice == '1':
                operands = equation.split('+')
                result = sum(map(float, operands))
                print("Answer:", result)
                time.sleep(1)

            elif choice == '2':
                operands = equation.split('-')
                result = float(operands[0])
                for operand in operands[1:]:
                    result -= float(operand)
                print("Answer:", result)
                time.sleep(1)

            elif choice == '3':
                operands = equation.split('*')
                result = 1
                for operand in operands:
                    result *= float(operand)
                print("Answer:", result)
                time.sleep(1)

            elif choice == '4':
                operands = equation.split('/')
                if '0' in operands:
                    print("Cannot divide by zero.")
                else:
                    result = float(operands[0])
                    for operand in operands[1:]:
                        result /= float(operand)
                    print("Answer:", result)
                time.sleep(1)

            elif choice == '5':
                operands = equation.split('~')
                result = math.pow(float(operands[0]), float(operands[1]))
                print("Answer:", result)
                time.sleep(1)

            else:
                print("Invalid input")

    elif choice == '2':
        print("Select operation:")
        print("1. Sine")
        print("2. Cosine")
        print("3. Tangent")
        print("4. Logarithm")
        print("5. Square root")
        print("6. Exit")

        choice = input("Enter choice (1/2/3/4/5/6): ")

        if choice == '1':
            angle = float(input("Enter angle in degrees: "))
            result = math.sin(math.radians(angle))
            print("Answer:", result)
            time.sleep(1)

        elif choice == '2':
            angle = float(input("Enter angle in degrees: "))
            result = math.cos(math.radians(angle))
            print("Answer:", result)
            time.sleep(1)

        elif choice == '3':
            angle = float(input("Enter angle in degrees: "))
            result = math.tan(math.radians(angle))
            print("Answer:", result)
            time.sleep(1)

        elif choice == '4':
            num = float(input("Enter number: "))
            base = float(input("Enter base: "))
            result = math.log(num, base)
            print("Answer:", result)
            time.sleep(1)

        elif choice == '5':
            num = float(input("Enter number: "))
            result = math.sqrt(num)
            print("Answer:", result)
            time.sleep(1)

        elif choice == '6':
            print("Exiting the calculator", end="")

       
        elif choice == '7':
            num1 = float(input("Enter the number: "))
            result = math.sqrt(num1)
            print("Answer:", result)
            time.sleep(1)

        elif choice == '8':
            num1 = float(input("Enter the base number: "))
            num2 = float(input("Enter the exponent: "))
            result = num1 ** num2
            print("Answer:", result)
            time.sleep(1)

        else:
            print("Invalid input")
