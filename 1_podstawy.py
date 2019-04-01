print("CDV")
print(2)

#potęgowanie
'''
komentarz blokowy
'''
#potęgowanie
potega = 2 ** 10
print(potega)

#pobieranie danych z klawiatury
imie = input("podaj imie: ")
#konkatenacja +
nazwisko = input("podaj nazwisko: ")
print("twoje imie z klawiatury: " + imie + "     " + "twoje imie z klawiatury: " + nazwisko)



print("Podaj swój wiek: ",end="")
wiek = input()
print("Twoj wiek: ",wiek," lat")

nazwisko = "Kowalski"
pierwszyZnak = nazwisko[0]
print(pierwszyZnak)

dlugosc = len(nazwisko)
print(dlugosc)

ostatniZnak = nazwisko[len(nazwisko)-1]
print(ostatniZnak)

ostatniZnak = nazwisko[-1]
print (ostatniZnak)

#konwersja

x = "5"
print(type(x))
x = int(x)
print(type(x))

y=4
print(type(y)) #int
y = y/2
print(type(y)) #float
print(y) #2.0

nazwisko = "Kowalski"
print(nazwisko[0]) #K
print(nazwisko[0:3]) #Kow
print(nazwisko[-2]) #k
print(nazwisko[-2:]) #ki
print(nazwisko[:-2]) #Kowals
print(nazwisko[:-2:2]) #Kwl

