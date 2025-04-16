dict = {}

with open("sanakirja.txt", "r", encoding="utf-8") as file:
       for i in file:
        if ":" in i:
            key, definition = i.strip().split(":", 1)
            dict[key.strip()] = definition.strip()

# Käyttäjä voi hakea haluaamansa sanaa sanakirjasta

def search(word):
    if word in dict:
        print(f"{word}: {dict[word]}")
    else:
        print("Sanaa ei löytynyt sanakirjasta.")


# Käyttäjä voi lisätä haluamansa sanan sanakirjaan

def add(word, definition):
    if word in dict:
        print("Tämä sana kuuluu jo sanakirjaan!")
        return
    else:
        dict[word] = definition
        with open("sanakirja.txt", "a", encoding="utf-8") as file:
            file.write(f"{word}: {definition}\n\n")


# Käyttäjä voi päivittää haluamallensa sanalle uuden merkityksen

def update(word, definition):
    if word not in dict:
        print("Tätä sanaa ei ole sanakirjassa!")
        return

    else:
        with open("sanakirja.txt", "r", encoding="utf-8") as file:
            for i in file:
                if ":" in i.strip():
                    key, value = i.strip().split(":", 1)
                    dict[key.strip()] = value.strip()

    dict[word] = definition
    with open("sanakirja.txt", "w", encoding="utf-8") as file:
        for key, value in dict.items():
            file.write(f"{key}: {value}\n\n")

# Käyttäjä voi poistaa haluamansa sanan sanakirjasta.

def delete(word):
    if word not in dict:
        print("Sanaa ei löytynyt sanakirjasta.")
        return
    else:
        del dict[word]
        with open("sanakirja.txt", "w", encoding="utf-8") as file:
            for key, value in dict.items():
                file.write(f"{key}: {value}\n\n")
        print(f"Sana '{word}' poistettiin sanakirjasta.")


while True:
    print("Valitse toiminto:")
    print("1. Etsi sana")
    print("2. Lisää sana")
    print("3. Päivitä sana")
    print("4. Poista sana")
    print("5. Lopeta")

    choice = input("Valintasi: ")

    if choice == "1":
        word = input("Anna sana: ")
        search(word)
    elif choice == "2":
        word = input("Anna sana: ")
        definition = input("Anna sanaan liittyvä määritelmä: ")
        add(word, definition)
    elif choice == "3":
        word = input("Anna sana: ")
        definition = input("Anna uusi määritelmä: ")
        update(word, definition)
    elif choice == "4":
        word = input("Anna sana: ")
        delete(word)
    elif choice == "5":
        break
    else:
        print("Virheellinen valinta.")
