tekst = "   Anna, paweł, JuliA"

lista = tekst.split(", ")
print(tekst)
print(lista)

imie1 = lista[0]
print(imie1)

imieDuze = imie1.upper()
print(imieDuze)

#zawartość
print("\Podaj swoje nazwisko: ",end="")
nazwisko = input()
zawartosc = nazwisko.isalpha()
print(zawartosc)

text1="\nJulia\n"
text2="Nowak"
print(text1 + + text2)

text1 = text1.rstrip()
print(text1+text2)

#wyświetlenie łańcucha znaków

text + "%s,Java i %s" % ("PHP", "Python")

text = "{1},Java i {0}".format("PHP","Python")

new = text.replace("PHP","C#")
print(new)

#wypisanie danych
rok =2019
miesiac = "kwiecien"
dzien = 1

print("\nData: ",end="")
print(dzien,miesiac,rok,sep= "_")
