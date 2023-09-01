import re

regex = r'^i.*[0-5].*\sZ$'

user_input = input("Unesite string: ")

if re.match(regex, user_input):
    print("Podudaranje pronađeno!")
else:
    print("Podudaranje nije pronađeno.")
