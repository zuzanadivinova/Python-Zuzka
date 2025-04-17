cislo = int(input("Zadej celé číslo:"))
if cislo % 3 == 0 and cislo % 5 == 0:
    print("FIZZBUZZ")
elif cislo % 3 == 0 :
    print("FIZZ")
elif cislo % 5 == 0 :
    print("BUZZ")
else:
    print(cislo)