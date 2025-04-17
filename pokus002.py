slovnik = {
    "kočka": "cat",
    "pes": "dog",
    "strom": "tree",
    "auto": "car",
    "dům": "house"
}
pocet_slov=len(slovnik)
print(f"Slovník obsahuje: { pocet_slov} slov!")
for klic in slovnik.keys() :
    print(klic)
for hodnota in slovnik.values() :
    print(hodnota)
novy_klic=input("Zadej nové slovo: ")
novy_preklad=input("Zadej nový překlad: ")
slovnik[novy_klic] = novy_preklad
print("Nový slovník:", slovnik)
slovo_uzivatele=input("Zadej slovo: ")
if slovo_uzivatele in slovnik:
    print(f"Překlad slova '{slovo_uzivatele}' je: {slovnik[slovo_uzivatele]}")
else:
    print(f"Slovo '{slovo_uzivatele}' není ve slovníku.")
slovo_vymaz=input("Zadej slovo na smazání: ")
if slovo_vymaz in slovnik :
    slovnik.pop(slovo_vymaz)
else:
    print("Slovo není ve slovníku:")
