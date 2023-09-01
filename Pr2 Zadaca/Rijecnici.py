import random

imena_studenata = ['Karlo', 'Ana-Marija', 'Antonio', 'Marko', 'Matea', 'Vice', 'Sara', 'Ivana', 'Ante', 'Ivan Entoni',
                   'Tonka', 'Antonio', 'Mateo', 'Mateo', 'Josip', 'Marko', 'Tino', 'Azer', 'Tomislava', 'Katarina',
                   'Karlo', 'David', 'Ivan', 'Petar', 'Marija', 'Antonio', 'Mario', 'Josip', 'Leonardo', 'Antonio',
                   'Renato', 'Matej', 'Matej', 'Jozo Matej', 'Petar', 'Ivan', 'Stjepan', 'Petar', 'Dražen', 'Zvonimir',
                   'Marin', 'Antonio', 'Stipe', 'Ana', 'Mate', 'Miroslav', 'Karlo', 'Marino', 'Mija', 'Kristijan',
                   'Ante', 'Ana', 'Iva', 'Mladen', 'Ivan', 'Frano', 'Mate', 'Mateo', 'Harun']

ocjene = {}

for ime in imena_studenata:
    ocjena = random.randint(1, 5)
    if ocjena in ocjene:
        ocjene[ocjena] += 1
    else:
        ocjene[ocjena] = 1

broj_prolaznih_ocjena = 0

for ocjena in ocjene:
    if ocjena > 1:
        broj_prolaznih_ocjena += ocjene[ocjena]

postotak_prolaznosti = (broj_prolaznih_ocjena / len(imena_studenata)) * 100

print("Broj ocjena:")
for ocjena in ocjene:
    print(f"Ocjena {ocjena}: {ocjene[ocjena]}")

print(f"Postotak prolaznosti: {postotak_prolaznosti}%")
