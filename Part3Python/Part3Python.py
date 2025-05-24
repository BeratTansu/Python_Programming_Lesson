#%%
#girilen sayıdan 10a kadar yazdıran program
number = int(input("Enter a number: "))
while number < 10:
    number += 1
    print(number)
print("Execution Finished!")

#%%
#0dan 30a kadar olan çift sayıları yazdıran program
number = 0
while (number < 31):
  if (number % 2 == 0):
    print(number)
  number += 1

print("finish")

#%%
#girilen sayıdan 1e kadar yazdıran ve en son now! yazdıran program
print("Are you ready?")
number = int(input("Enter a number: "))
while number >= 1:
    print(number)
    number -= 1
print("Now!")

#%%
#girilen sayıya kadar 2nin üslerini yazdıran program
upperLimit = int(input("Enter a upper limit: "))
number = 1
while number <= upperLimit:
    print(number)
    number *= 2
print("finito")

#%%
#hem üssü alınacak sayıyı hem de en son limitini girdiğimiz program
upper_Limit = int(input("Enter a upper limit: "))
base = int(input("Enter a base: "))
number = 1
while number <= upper_Limit:
    print(number)
    number = number * base
print("finish")

#%%
#ardışık sayıları toplayan ve limit değerine eşit olursa ya da aşarsa durduran program
limit = int(input("Enter a limit: "))
number = 1
sum = 0
calculation = "The consecutive sum= "
while sum < limit:
    sum += number
    calculation += str(number)
    if (sum < limit):
        calculation += " + "
    number += 1
calculation +=f" = {sum}"
print(calculation)

#%%
#yıldızlardan piramit yaptıran kod
starNumber = int(input("Enter a star number: "))
row = "*"
while starNumber > 0:
    print(" " * starNumber + row)
    row += "**"
    starNumber -= 1

#*************************************EXAMPLES*************************************


#%%
#Bir sayı girdisi alarak 20'ye ulaşana kadar artıran bir döngü yazın.
number = int(input("Enter a number: "))
while number <= 20:
    print(number)
    number += 1


#%%
#0'dan 50'ye kadar olan tek sayıları ekrana yazdıran bir Python programı yazın.
number = 0
while number <= 50:
    if number % 2 != 0:
        print(number)
    number += 1


#%%
#Bir sayı girdisi alarak, bu sayıdan geriye doğru sıfıra kadar (sıfır dahil değil) geri sayan bir döngü oluşturun.
number = int(input("Enter a number: "))
while number >= 1:
    print(number)
    number -= 1


#%%
#Kullanıcıdan bir üst sınır alarak, 1’den başlayıp her seferinde 3 ile çarpan bir döngü oluşturun.
limit = int(input("Enter a limit: "))
number = 1
while number <= limit:
    print(number)
    number *= 3


#%%
#Kullanıcıdan bir üst sınır ve bir taban değeri alarak, 1’den başlayıp her seferinde taban ile çarpan bir döngü yazın.
limit = int(input("Enter a limit: "))
number = 1
base = int(input("Enter a base: "))
while number <= limit:
    print(number)
    number *= base


#%%
#Kullanıcının girdiği bir limit değere ulaşana kadar pozitif tamsayıları toplayan bir döngü oluşturun.
limit = int(input("Enter a limit: "))
number = 1
sum = 0
while sum < limit:
    print(number)
    sum += number
    number += 1
print(f"sum =  {sum}")


#%%
#Kullanıcının girdiği bir limit değere ulaşana kadar pozitif tamsayıları toplayan ve işlemi ekrana matematiksel gösterim şeklinde yazdıran bir Python programı yazın.
limit = int(input("enter a limit: "))
number = 1
sum = 0
calculation = "The consecutive sum: "
while sum < limit:
    sum += number
    calculation += str(number)
    if (sum < limit):
        calculation += " + "
    number += 1
calculation +=f" = {sum}"
print(calculation)


#%%
#Yıldızlardan oluşan bir piramit deseni oluşturan bir Python programı yazın.
starNumber = int(input("enter a star number: "))
row = "*"
while starNumber > 0:
    print(" " * starNumber + row)
    row += "**"
    starNumber -= 1


#%%
#yukarıdaki örneğin tam tersini yapınız.
n = int(input("Tavan değerini girin: "))  # Kullanıcıdan tavan değerini al
row = n  # İlk satırda tam olarak n yıldız olacak

while row > 0:
    print(" " * (n - row) + "*" * (2 * row - 1))  # Boşluk + yıldızları yazdır
    row -= 1  # Yıldız sayısını azalt



