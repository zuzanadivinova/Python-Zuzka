mesta = ["Praha", "Viden", "Olomouc", "Svitavy", "Zlin", "Ostrava"]
ceny = (150, 200, 120, 120, 100, 180)
cara = "=" * 35
nabidka = """1 - Praha   | 150
2 - Viden   | 200
3 - Olomouc | 120
4 - Svitavy | 120
5 - Zlin    | 100
6 - Ostrava | 180
"""
print("VITEJTE U NASI APLIKACE DESTINATIO")
print(cara)
print(nabidka)
print(cara)
destinace=input("CISLO DESTINACE:")
jmeno=input("JMENO:")
prijmeni=input("PRIJMENI:")
email=input("EMAIL:")
print(cara)
print("CISLO DESTINACE:", destinace)
print(cara)
spravna_destinace = mesta[int(destinace) - 1]
cena = ceny[int(destinace) - 1]
print(spravna_destinace)
print(cena)
print(cara)
print("Děkuju " + jmeno + " za objednávku.")
print("Cíl destinace: " + spravna_destinace + " ,cena jizdného:" + str(cena))
print("Na tvůj email" + email + " jsme ti poslali lístek!")
print()







