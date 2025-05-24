#Example 1 :
print("Minutes in a year!")
print(365*24*60)

#Example 2 :
name = input("What is your name? ")
print("Hi " + name + " nice to meet you!")
                                    
#Example 3 :
name = input("What is your name? ")
age = input("How old are you? ")
address = input("Where do you live? ")
print(f"Hi {name}, you are {age} years old and lived at {address} ")

#Example 4 :
x = input( "x = ")
y = input( "y = ")

print(int(x) + int(y))
print(int(x) - int(y))
print(int(x) * int(y))
print(int(x) / int(y))
print(x + y)

#Example 5 :
weight = float(input("What is your weight? "))
height = float(input("What is your height? "))

height = height / 100
bmi = weight / (height ** 2)
print(f"Your BMI is: {bmi}")

if bmi < 18.5:
    print("You are under weight")
elif 18.5 <= bmi < 25:
    print("You are normal weight")
elif 25 <= bmi <30:
    print("You are over weight")
else:
    print("You are obese!")

#Example 6 :
name = input("What is your name? ")
birthdate = int(input("Which year were you born? "))
while(birthdate > 2025):
    birthdate = int(input("Please under the 2025 "))
age = 2025 - birthdate
print(f"Hi {name}, you will be {age}, and the end of the 2025")

#Example 7 :
number1 = int(input("Enter is first number: "))
number2 = int(input("Enter is second number: "))
operator = input("What is operator: ")
 
if operator == "+":
    print(f"{number1 } + { number2}" + number1 + number2)
elif operator == "-":
    print(f"{number1 } - { number2}" + number1 - number2)
elif operator == "*":
    print(f"{number1 } * { number2} = {number1 * number2}")
elif operator == "/":
    print(f"{number1 } / { number2}" + number1 / number2)
else:
    print("That's not an operator!")
