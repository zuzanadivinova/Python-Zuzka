slovnik = {
    "kočka": "cat",
    "pes": "dog",
    "strom": "tree",
    "auto": "car",
    "dům": "house"
}
pocet_slov=len(slovnik)
print(f"Slovník obsahuje: { pocet_slov} slov!")

print("česká slova:")
for klic in slovnik.keys():
    print(klic)

print("anglická slova:")
for hodnota in slovnik.values() :
    print(hodnota)

novy_klic=input("Zadej nové české slovo: ")
novy_preklad=input("Zadej nový překlad: ")
slovnik[novy_klic] = novy_preklad
print("Nový slovník:", slovnik)

slovo_uzivatele=input("Zadej k překladu slovo: ")
if slovo_uzivatele in slovnik:
    print(f"Překlad slova '{slovo_uzivatele}' je: {slovnik[slovo_uzivatele]}")
else:
    print(f"Slovo '{slovo_uzivatele}' není ve slovníku.")

slovo_vymaz=input("Zadej slovo na smazání: ")
if slovo_vymaz in slovnik :
    del slovnik[slovo_vymaz]
    print(f"Opravený slovník: {slovnik}")
else:
    print("Slovo není ve slovníku:")