#%%
#Bir fonksiyon yazın (adı line), iki parametre alsın: bir tamsayı ve bir string; tamsayı kadar uzunlukta
# bir satır yazdırsın ve karakter olarak stringin ilk harfini kullansın, eğer string boşsa * kullansın.


def Line(length, value):
    if value:
        print(length * value)
    else:
        print("*" * length)

Line(3,"2")


#%%
#Bir fonksiyon yazın (box_of_hashes), bir tamsayı parametre alsın ve genişliği 10, yüksekliği parametre kadar
#olan bir # dikdörtgeni yazdırsın.

def box_of_hashes(width):
    for i in range(width):
        print("#" * 10)

box_of_hashes(2)


#%%
#Bir fonksiyon yazın (square_of_hashes), bir tamsayı parametre alsın ve kenar uzunluğu bu parametreye eşit olan
#bir # karesi yazdırsın.

def square_of_hashes(kenar):
    for i in range(kenar):
        print("# " * kenar)

square_of_hashes(4)


#%%
#Bir fonksiyon yazın (square), iki parametre alsın: birincisi karesel yapının kenar uzunluğu, ikincisi karesel yapıyı
#oluşturan karakter; belirtilen özelliklerde bir kare yazdırsın.

def square(kenar, karakter):
    for i in range(kenar):
        print(kenar * karakter)

square(5, "+")


#%%
#Bir fonksiyon yazın (triangle), bir tamsayı parametre alsın ve yüksekliği ve tabanı bu parametreye eşit olan bir #
#üçgeni yazdırsın.

def triangle(taban):
    star = "#"
    for i in range(taban):
        print(star)
        star += "#"

triangle(5)


#%%
#Bir fonksiyon yazın (shape), dört parametre alsın: birincisi üçgenin boyutunu ve karakterini, ikincisi dikdörtgenin
#boyutunu ve karakterini belirtir; önce üçgeni, sonra dikdörtgeni yazdırsın.

def shape(ucgen_boyut, ucgen_karakter, dikdortgen_boyut, dikdortgen_karakter):
    for i in range(ucgen_boyut + 1):
        print(ucgen_karakter * i)

    for i in range(dikdortgen_boyut + 1):
        print(dikdortgen_karakter * i)

shape(5, "#", 3, "*")


#%%
#Bir fonksiyon yazın (spruce), bir parametre alsın; önce "a spruce!" yazsın, sonra belirtilen büyüklükte bir çam ağacı
#çizsin.

def spruce(boyut):
    space_len = boyut - 1
    space = " "
    star = "*"
    print("a spruce!")
    for i in range(boyut):
        print((space * space_len) + star)
        star += "**"
        space_len -= 1
    print(" " * (boyut - 1) + "*")
spruce(5)


#%%
#Bir fonksiyon yazın (greatest_number), üç parametre alsın ve bu parametrelerden en büyüğünü döndürsün.

def greatest_number(n1, n2, n3):
    if (n1 == n2 and n2 == n3):
        print("numbers are equal")
    elif (n1 > n2 and n1 > n3):
        print(f"greatest number is = {n1}")
    elif (n2 > n1 and n2 > n3):
        print(f"greatest number is = {n2}")
    elif (n3 > n1 and n3 > n2):
        print(f"greatest number is = {n3}")
    #veya sadece tek satırda da yapılabilir max fonksiyonuyla= print(max(n1,n2,n3))

greatest_number(2,3,1)


#%%
#Bir fonksiyon yazın (same_chars), bir string ve iki indeks alsın ve bu indekslerdeki karakterlerin aynı
#olup olmadığını kontrol edip, sonuç olarak True ya da False döndürsün.

def same_chars(string, index1, index2):
    if index1 < 0 or index1 >= len(string) or index2 < 0 or index2 > len(string):
        return  False
    elif string[index1] != string[index2]:
        return False
    else:
        return True

print(same_chars("programming", 6, 7))


#%%
#Bir fonksiyon yazın (first_word, second_word, last_word), her biri bir cümle alacak ve sırasıyla ilk,
#ikinci veya son kelimeyi döndürecek.

def first_word(sentence):
    word = ""
    for char in sentence:
        if char == " ":
            break
        word += char
    return word
def second_word(sentence):
    word = ""
    space_count = 0 # kaç boşluk geçtiğimizi sayacak sayaç
    for char in sentence:
        if char == " ":
            space_count += 1
        elif space_count == 1:
            word += char
    return word
def last_word(sentence):
    word = ""
    for char in reversed(sentence):
        if char == " ":
            break
        word += char
    return reversed(word)
print(first_word("berat tansu çabuk"))
print(second_word("berat tansu çabuk"))
print(last_word("berat tansu çabuk"))


#%%
#Bir listeyi başlatıp, kullanıcıdan indeks ve değer alarak güncelleyen, -1 girilene kadar çalışan Python programı yazar mısın?
liste = [1,2,3,4,5]
while(True):
    index = int(input("güncellemek istediğiniz indexi girin (çıkmak istiyorsanız -1 giriniz): "))
    if(index == -1):
        print("programdan çıkılıyor!")
        break

    new_value = int(input("yeni değeri giriniz: "))

    liste[index] = new_value

    print(f"güncellenmiş liste : {liste}")


#%%
#Kullanıcıdan kaç öğe ekleyeceğini alıp, tek tek listeye ekleyen ve sonunda listeyi yazdıran bir Python programı yazar mısın?
eklenecek_sayi = int(input("kaç öge eklemek istiyorsunuz: "))

values = []

for i in range(eklenecek_sayi):
    value = input("eklemek istediğiniz değeri giriniz: ")
    values.append(value)

print(f"listenin son hali: {values}")


#%%
#Kullanıcının ekleme veya çıkarma seçimine göre listeyi güncelleyen, ekleme işlemlerinde sıralı sayı ekleyen bir Python programı yazar mısın?
numbers = []
while(True):
    choice = input("Ekleme (E) veya Çıkarma (Ç) işlemi yapın, Çıkmak istiyorsanız (Q): ").strip().upper()
    if choice == "E":
        new_value = input("Eklemek istediğiniz değeri giriniz: ")
        numbers.append(new_value)
    if choice == "Q":
        print("programdan çıkılıyor...")
        break
    elif choice == "Ç":
        if numbers: #liste boş mu diye kontrol edilir! eğer liste boş değilse if'e girer boşsa else'e
            numbers.pop()
        else:
            print("Liste zaten boş!")

print(f"Yeni Liste: {numbers}")


#%%
#Kullanıcıdan kelimeler alıp, bir kelime ikinci kez girildiğinde farklı kelimelerin sayısını yazdırarak sonlanan bir Python programı yazar mısın?
words = []

while(True):
    word = input("Bir kelime girin (çıkmak için boş bırakın): ")

    if word == "":
        break

    if word in words:
        print(f"Farklı kelimelerin sayısı: {len(words)}")
        break

    words.append(word)


#%%
#Kullanıcıdan alınan değerleri listeye ekleyen ve her eklemede listeyi hem eklenme sırasına göre hem de küçükten büyüğe sıralan şekilde yazdıran Python programını yazınız.
liste = []

while(True):
    value = input("bir değer girin(çıkmak için 'q' tuşuna basın): ").upper()

    if value == "Q":
        print("Programdan çıkılıyor...")
        break

    try:
        deger = int(value)
        liste.append(value)
        print(f"Ekleme sırası : {liste}")
        print(f"Sıralanmış : {sorted(liste)}")
    except ValueError:
        print("Geçersiz giriş, lütfen sayı giriniz!")


#%%
#Bir liste alan ve bu listenin uzunluğunu döndüren length adında bir fonksiyon yazınız.
liste1 = [1,2,3,4,5]
def length(liste):
    return len(liste)

print(f"The length is {length(liste1)}")


#%%
#Bir tam sayı listesi alan ve bu listenin aritmetik ortalamasını döndüren mean adında bir fonksiyon yazınız.
tam_sayilar = [1,2,3,4,7,5,8,6]
def mean(liste):
    if not liste:
        return 0
    return sum(liste) / len(liste)

    #sum ve len fonksiyonları kullanılmadan yapılan çözüm;
    #total = 0
    #count = 0
    #for num in liste:
        #total += num
        #count += 1
    #return total / count

print(f"Listenin ortalaması : {mean(tam_sayilar)}")


#%%
#Bir tam sayı listesi alan ve bu listedeki en büyük ile en küçük değer arasındaki farkı (aralığı) döndüren range_of_list adında bir fonksiyon yazınız.
tam_sayilar = {2,1,5,6,4,7,9,8}
def range_of_list(liste):
    if not liste:
        return 0

    smallest = biggest = None
    for i in liste:
        if biggest is None or i > biggest:
            biggest = i
        if smallest is None or i < smallest:
            smallest = i
    return biggest - smallest

print(f"Listenin aralığı: {range_of_list(tam_sayilar)}")