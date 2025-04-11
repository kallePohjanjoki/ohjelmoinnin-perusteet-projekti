dict = {}

with open("sanakirja.txt", "r", encoding="utf-8") as file:
       for i in file:
        if ":" in i:
            key, definition = i.strip().split(":", 1)
            dict[key.strip()] = definition.strip()

def search(word):
    if word in dict:
        print(f"{word}: {dict[word]}")
    else:
        print("Sanaa ei löytynyt sanakirjasta.")


def add(word, definition):
    if word in dict:
        print("Tämä sana kuuluu jo sanakirjaan!")
        return
    else:
        dict[word] = definition
        with open("sanakirja.txt", "a", encoding="utf-8") as file:
            file.write(f"{word}: {definition}\n\n")


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
