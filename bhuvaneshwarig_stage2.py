# Take input from user
num1 = float(input("Enter first number: "))
num2 = float(input("Enter second number: "))
operator = input("Enter operator (+, -, *, /): ")

# Perform calculation
if operator == "+":
    result = num1 + num2

elif operator == "-":
    result = num1 - num2

elif operator == "*":
    result = num1 * num2

elif operator == "/":
    if num2 == 0:
        print("Error: Cannot divide by zero")
        exit()
    else:
        result = num1 / num2

else:
    print("Invalid operator")
    exit()

# Display result
print("Result =", result)

# Check result type
if result > 0:
    print("Positive")
elif result < 0:
    print("Negative")
else:
    print("Zero")
