Imena_studenata = ["Mario", "Josip", "Ivana", "Mija", "Ivan", "Ante", "Marino", "Ana-Marija", "Frano", "Mladen", "Marko", "Jozo Matej", "Karlo", "Mate", "Katarina", "Tomislava", "Alija", "Sara", "Petar", "Safet", "Matej", "Stjepan", "Ivan", "Antonio", "David", "Ivan Entoni", "Marija", "Mate", "Kristijan", "Antonio", "Ružica", "Petar", "Ana", "Zvonimir", "Matea", "Petar", "Miroslav", "Matea", "Marija", "Marko", "Antonio", "Matej", "Iva", "Leonardo", "Karlo", "Josip", "Ivan", "Vice", "Azer"]
Prezimena_studenata = ["Jonjić", "Ćavar", "Bunoza", "Sabljić", "Luetić", "Šimić", "Rupar", "Bakula", "Vranjković", "Tomić", "Benković", "Lasić", "Rezo", "Penava", "Galić", "Đopa", "Kičin", "Budimir", "Lončar", "Srna", "Knežević", "Marić", "Udovičić", "Jakovljević", "Grubišić", "Bunoza", "Krištić", "Zeljko", "Slišković", "Bebek", "Grgić", "Ilišević", "Šimić", "Milardović", "Tufekčić", "Markić", "Pinjuh", "Bošnjak", "Krištić", "Ćubela", "Mlikota", "Kraljević", "Šimović", "Karačić", "Bagarić", "Jurković", "Živković", "Božić", "Džemić"]
Bodovi = [100, 100, 100, 90, 80, 75, 60, 60, 55, 55, 55, 50, 50, 50, 50, 50, 50, 40, 35, 35, 30, 30, 25, 25, 20, 20, 20, 15, 15, 15, 15, 15, 10, 10, 10, 10, 5, 5, 5, 5, 0, 0, 0, 0, 0, 0, 0, 0]

ocjene = {
    "Nedovoljan": range(0, 50),
    "Dovoljan": range(50, 66),
    "Dobar": range(65, 81),
    "Vrlodobar": range(80, 91),
    "Izvrstan": range(90, 101)
}

studenti_ocjene = {}

for ime, prezime, bod in sorted(zip(Imena_studenata, Prezimena_studenata, Bodovi), key=lambda x: x[1]):
    for ocjena, raspon in ocjene.items():
        if bod in raspon:
            studenti_ocjene[ime + " " + prezime] = ocjena

for student, ocjena in studenti_ocjene.items():
    print(f"{student}: {ocjena}")
