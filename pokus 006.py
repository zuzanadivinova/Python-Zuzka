TEXTS = [
    '''Situated about 10 miles west of Kemmerer,
    Fossil Butte is a ruggedly impressive
    topographic feature that rises sharply
    some 1000 feet above Twin Creek Valley
    to an elevation of more than 7500 feet
    above sea level. The butte is located just
    north of US 30 and the Union Pacific Railroad,
    which traverse the valley.''',
    '''At the base of Fossil Butte are the bright
    red, purple, yellow and gray beds of the Wasatch
    Formation. Eroded portions of these horizontal
    beds slope gradually upward from the valley floor
    and steepen abruptly. Overlying them and extending
    to the top of the butte are the much steeper
    buff-to-white beds of the Green River Formation,
    which are about 300 feet thick.''',
    '''The monument contains 8198 acres and protects
    a portion of the largest deposit of freshwater fish
    fossils in the world. The richest fossil fish deposits
    are found in multiple limestone layers, which lie some
    100 feet below the top of the butte. The fossils
    represent several varieties of perch, as well as
    other freshwater genera and herring similar to those
    in modern oceans. Other fish such as paddlefish,
    garpike and stingray are also present.'''
]
user = {
    "bob": "123",
    "ann": "pass123",
    "mike": "password123",
    "liz": "pass123"
}
separator = ("-"*50)

user_name = input("Username: ")
pass_word = input("Password: ")
print(separator)

if not user.get(user_name) == pass_word:
    print("Unregistered user, terminating the program..")
    exit() 
else:   
    print(f"Welcome to the app, {user_name}.\nWe have 3 texts to be analyzed.")
    print(separator)

    number = input("Enter a number btw. 1 and 3 to select: ")
    print(separator)

    if not number.isdigit() or not 1 <= int(number) <= 3:
        print("Invalid number, terminating the program..")
        exit()
    
    selected_text = TEXTS[int(number) - 1]
    words = selected_text.split()
    clean_words = [word.strip(".,") for word in words] 

    title_words = []
    upper_words = []
    lower_words = []
    numeric_words = []
    numeric_sum = 0

    for word in words:
        if word.istitle():        
            title_words.append(word)
        elif word.isupper():
            upper_words.append(word)
        elif word.islower():
            lower_words.append(word)
        elif word.isnumeric():
            numeric_words.append(word)
            numeric_sum += int(word)

    print(f"There are {len(words)} words in the selected text.")
    print(f"There are {len(title_words)} titlecase words.")
    print(f"There are {len(upper_words)} uppercase words.")
    print(f"There are {len(lower_words)} lowercase words.")
    print(f"There are {len(numeric_words)} numeric strings.")
    print(f"The sum of all the numbers is {numeric_sum}.")
    print(separator)

    print("LEN|    OCCURENCES      |NR.") 
    print(separator)

    word_lengths = {}
    for word in words:
        word = word.strip(", . ? !")
        length = len(word)
        if length in word_lengths:
          word_lengths[length] += 1
        else:
          word_lengths[length] = 1
    for length in sorted(word_lengths):
        count = word_lengths[length]
        print(f"{length:>3}|{'*' * count:<20}|{count}")
     


