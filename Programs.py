
#variables
# Global variable
PI = 3.142  # Constant, typically written in uppercase

def calculate_circle_area(radius):
    # Local variable
    area = PI * (radius ** 2)
    return area

radius = 5
print("Circle area:", calculate_circle_area(radius))

# Variable naming convention
num1 = 10
_num2 = 20
result = num1 + _num2
print("Sum:", result)



#Expressions

x = 5
y = 10
z = 3

# Arithmetic expression
result = x + y - z * 2 / 5
print("Result of arithmetic expression:", result)

# Comparison expression
is_equal = (x == y)
print("Is x equal to y?", is_equal)

# Using multiple operators with precedence
result = x * z + y ** 2 - 4 / 2
print("Expression result with operator precedence:", result)



# Type Casting
# Implicit casting
a = 5
b = 2.0
c = a + b  # Python converts `a` to float automatically
print("Result of implicit casting:", c)  # Output will be a float

# Explicit casting
user_input = "100"
num = int(user_input)  # Converting string to integer
print("Integer value of user input:", num)

float_value = float(num)
print("Explicitly casted to float:", float_value)

# Combining different casts
text_num = "3.5"
converted_num = float(text_num) + 2  # Convert to float, then add
print("Result of combined cast:", converted_num)



# Loops
# While loop - indefinite loop
count = 0
while count < 3:
    print("Count:", count)
    count += 1

# For loop - definite loop with a range
for i in range(3):
    print("Loop index:", i)

# For loop with list
numbers = [1, 2, 3]
for num in numbers:
    print("Number in list:", num)

# Nested loop example
for i in range(2):
    for j in range(3):
        print(f"Nested Loop ")




# Conditions

# If-else condition
temperature = 20
if temperature > 30:
    print("It's hot")
elif 20 <= temperature <= 30:
    print("It's warm")
else:
    print("It's cold")

# Combining conditions
a, b = 10, 20
if a < b and b < 30:
    print("Both conditions are true")

# Using conditions within a loop
for i in range(5):
    if i % 2 == 0:
        print(f"is even")
    else:
        print(f" is odd")
