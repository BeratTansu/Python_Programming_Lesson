from math import sqrt

#The following program contains several syntactic errors. Please fix the program so that the syntax is in order and the program works as specified by the examples below.
boolean_condition = True
while(boolean_condition):
    try:
        number = int(input("Enter a number: "))
    except:
        ValueError: print("That's not a number!")
        continue
    if number >100:
        print("The number was greater than one hundred")
        number = number - 100
        print("Now it's value has decreased by one hundred")
        print(f"Its value is now {number}")
        break
    print(f"{number} must be my lucky number! ")
    print("Have a nice day!")
    break


#Examples of expected behaviour:
#Please type in a word: hey
#There are 3 letters in the word hey
#Thank you!
#Please type in a word: b
#Thank you!

word = ""
while len(word) == 0 or not word.isalpha(): #boş giriş veya sayı içeriyorsa döngü devam eder
    word = input("Enter a word: ").strip() # girişi al ve boşlukları temizle
    if len(word) == 0:
        print("You didn't anything!")
    elif len(word) == 1:
        print("You entered number!")

word_length = len(word)

if word_length == 1:
    print("Thank you!")
else:
    print(f"There are {word_length} letters in the word {word}")


#Examples of expected behaviour:
#Please type in a number: 1.34
#Integer part: 1
#Decimal part: 0.34

number = float(input("Enter a number: "))
integer_part = int(number)
decimal_part = number - int(number)
decimal_length = len(str(decimal_part).split('.')[1]) #split('.'): bir string'i nokta (.) karakteri etrafında böler. Yani "1.23456" string'ini nokta karakterinden ayırmak için kullanılır.
decimal_part = round(decimal_part, decimal_length) #ondalık kısmı yuvarlama (örneğin, 10 haneli hassasiyetle)
print(f"Integer part: {integer_part}") #integer_part bir tam sayı olduğu için Python, otomatik olarak string formatına çevirir.
print(f"Decimal part: {str(decimal_part)}") #decimal_part bir ondalık sayı olduğu için, daha doğru bir şekilde yazdırabilmek adına str() kullanıyoruz ve gerektiğinde formatlama yapıyoruz.


#Examples of expected behaviour:
#How old are you? 12
#You are not of age!

#How old are you? 32
#You are of age!

age = int(input("How old are you? "))
if age >= 18:
    print("You are of age!")
else:
    print("You are not of age!")


#Examples of expected behaviour:
#Please type in the first number: 5
#Please type in another number: 3
#The greater number was: 5

#Please type in the first number: 5
#Please type in another number: 5
#The numbers are equal!

n1 = int(input("Please type in the first number: "))
n2 = int(input("Please type in another number: "))
if n1 > n2:
    print(f"The greater number was {n1}")
elif n1 < n2:
    print(f"The greater number was {n2}")
elif n1 == n2:
    print("The numbers are equal!")
else:
    print("They are not numbers!")


#Examples of expected behaviour:
#Person 1:
#Name: Alan
#Age: 26
#Person 2:
#Name: Ada
#Age: 27
#The elder is Ada

#Person 1:
#Name: Bill
#Age: 1
#Person 2:
#Name: Jean
#Age: 1
#Bill and Jean are the same age
print("Person 1:")
p1name = str(input("Name: "))
p1age = int(input("Age: "))
print("Person 2:")
p2name = str(input("Name: "))
p2age = int(input("Age: "))

if p1age > p2age:
    print(f"The elder is {p1name}")
elif p1age < p2age:
    print(f"The elder is {p2name}")
else:
    print(f"{p1name} and {p2name} are the same age!")


#Examples of expected behaviour:
#Please type in the 1st word: car
#Please type in the 2nd word: scooter
#scooter comes alphabetically last.

#Please type in the 1st word: python
#Please type in the 2nd word: python
#You gave the same word twice.

word1 = str(input("Please type in the 1st word: "))
word2 = str(input("Please type in the 2nd word: "))

if word1.upper() > word2.upper():
    print(f"{word1} comes alphabetically last")
elif word1.upper() < word2.upper():
    print(f"{word2} comes alphabetically last")
else:
    print(f"You gave the same word twice")


#Examples of expected behaviour:
#What is your age? 13
#Ok, you're 13 years old

#What is your age? 2
#I suspect you can't write quite yet...

#What is your age? -4
#That must be a mistake

age = int(input("What is your age? "))
if age < 5:
    print(f"I suspect you can't write quite yet...")
elif age >= 5:
    print(f"Ok, you are {age} years old")
else:
    print(f"That must be a mistake!")


#Examples of expected behaviour:
point = int(input("How many points [0-100]: "))
if point > 100:
    print(f"Impossible!")
elif point >= 0 and point < 50:
    print(f"Fail!")
elif point >= 50 and point < 60:
    print(f"Your grade : 1")
elif point >= 60 and point < 70:
    print(f"Your grade : 2")
elif point >= 70 and point < 80:
    print(f"Your grade : 3")
elif point >= 80 and point < 90:
    print(f"Your grade : 4")
elif point >= 90 and point <= 100:
    print(f"Your grade : 5")
else:
    print(f"Impossible!")


#Examples of expected behaviour:
#Number: 9
#Fizz

#Number: 7
#That's not fizz, buzz and fizzbuzz

#Number: 45
#FizzBuzz

number = int(input("Number: "))
if number % 3 == 0 and number % 5 == 0:
    print(f"FizzBuzz")
elif number % 5 == 0:
    print(f"Buzz")
elif number % 3 == 0:
    print(f"Fizz")
else:
    print(f"that's not fizz and not buzz")


#Examples of expected behaviour:
#Please type in a number: 3
#The number is odd

#Please type in a number: 18
#The number is even

#Please type in a number: -4
#The number is negative

#Please type in a number: 0
#The number is zero

number = int(input("Please type in a number: "))
if number % 2 == 0:
    print(f"The number is even")
elif number % 2 != 0:
    print(f"The number is odd")
elif number == 0:
    print(f"The number is zero")
elif number < 0:
    print(f"The number is negative")
else:
    print(f"That's not a number!")


#Examples of expected behaviour:
#Please type in a year: 2011
#That year is not a leap year.

#Please type in a year: 2020
#That year is a leap year.

#Please type in a year: 1800
#That year is not a leap year.

year = int(input("Please type in a year: "))
if year % 100 == 0 and year % 4 == 0:
    print(f"That year is a leap year.")
else:
    print(f"That year is not a leap year.")


#Examples of expected behaviour:
#1st letter: x
#2nd letter: c
#3rd letter: p
#The letter in the middle is p

#1st letter: C
#2nd letter: B
#3rd letter: A
#The letter in the middle is B

letter1 = input("1st letter: ")
letter2 = input("2nd letter: ")
letter3 = input("3rd letter: ")
if letter1 > letter2:
    letter1, letter2 = letter2, letter1
if letter1 > letter3:
    letter1, letter3 = letter3, letter1
if letter2 > letter3:
    letter2, letter3 = letter3, letter2

print(f"The letter in the middle is {letter2}")


#Examples of expected behaviour:
#Value of gift: 3500
#No tax!

#Value of gift: 5000
#Amount of tax: 100.0 euros

#Value of gift: 27500
#Amount of tax: 1950.0 euros

value_of_gift = int(input("Value of gift: "))
tax = 0
if value_of_gift < 5000:
    print(f"No tax!")
elif value_of_gift >= 5000 and value_of_gift < 25000:
    tax = (100 + (value_of_gift - 5000) * 0.08)
    print(f"Amount of tax: {tax} euros")
elif value_of_gift >= 25000 and value_of_gift < 55000:
    tax = (1700 + (value_of_gift - 25000) * 0.10)
elif value_of_gift >= 55000 and value_of_gift < 200000:
    tax = (4700 + (value_of_gift - 55000) * 0.12)
    print(f"Amount of tax: {tax} euros")
elif value_of_gift >= 200000 and value_of_gift < 1000000:
    tax = (22100 + (value_of_gift - 200000) * 0.15)
    print(f"Amount of tax: {tax} euros")
elif value_of_gift >= 1000000:
    tax = (142100 + (value_of_gift - 1000000) * 0.17)
    print(f"Amount of tax: {tax} euros")


#Examples of expected behaviour:
#hi
#Shall we continue? yes
#hi
#Shall we continue? oui
#hi
#Shall we continue? jawohl
#hi
#Shall we continue? no
#okay then

while(True):
    print("hi")
    answer = input("Shall we continue?")
    if answer == "no":
        break

#Examples of expected behaviour:
#Please type in a number: 16
#4.0
#Please type in a number: 4
#2.0
#Please type in a number: -3
#Invalid number
#Please type in a number: 1
#1.0
#Please type in a number: 0
#Exiting...


while True:
    try:
        number = int(input("Please type in a number: "))
        if number > 0:
            print(sqrt(number))
        elif number < 0:
            print("Ivalid number")
        elif number == 0:
            print("Exiting...")
            break
    except ValueError:
        print("That's not a number!")

#Examples of expected behaviour:
#Countdown!
#5
#4
#3
#2
#1
#Now!

number = 5
print("Countdown!")
while True:
    print(number)
    number -= 1
    if number == 0:
        break
print("Now!")


#Examples of expected behaviour:
#Password: sekred
#Repeat password: secret
#They do not match!
#Repeat password: cantremember
#They do not match!
#Repeat password: sekred
#User account created!

password = input("Password: ")
while True:
    repeatPassword = input("Repeat password: ")
    if password != repeatPassword:
        print("Passwords don't match")
    else:
        print("Password matches")
        break


#Examples of expected behaviour:
#PIN: 3245
#Wrong
#PIN: 1234
#Wrong
#PIN: 0000
#Wrong
#PIN: 4321
#Correct! It took you 4 attempts

#PIN: 4321
#Correct! It only took you one single attempt!

pin = "1234"
attemp = 1
while True:
    inputpin = input("PIN: ")
    if pin == inputpin and attemp == 1:
        print("Correct! It only took you one single attempt!")
        break
    elif pin != inputpin:
        attemp += 1
        print("wrong")
    elif pin == inputpin and attemp != 1:
        print(f"Correct! It only took you {attemp} attempt!")
        break

#%%
#A variation of the example above:
attemps = 4
pin = "1234"
while (attemps > 0):
    inputpin = input("PIN: ")
    if pin == inputpin:
        print("Correct PIN entered, Welcome!")
        break
    elif pin != inputpin:
        attemps -= 1
        print(f"Incorrect... try again! {attemps} attemps left!")