import sys
import random
import string


password = []
characters_left = -1

def update_characters_left(number_of_characters):
    global characters_left

    if number_of_characters < 0 or number_of_characters > characters_left:
        print("Liczba znaków przekracza liczbę wolnych znaków. Wybierz liczbę z przedziału od 0 do ", characters_left)
        sys.exit(0)
    else:
        characters_left -= number_of_characters
        print("Pozostało", characters_left, "znaków.")



password_length = int(input("Jak długie ma być hasło?"))

#dlugosc hasla
if password_length < 7:
    print("Hasło musi mieć minimum 7 znaków.")
    sys.exit(0)
else:
    characters_left = password_length

#male litery
while True:
    try:
        lowercase_letters = int(input("Ile małych liter ma mieć hasło?"))
        break
    except ValueError:
        print("Proszę podaj cyfrę:")
        continue
print("Ilość małych liter:", characters_left)
update_characters_left(lowercase_letters)

#duze litery
while True:
    try:
        uppercase_letters = int(input("Ile dużych liter ma mieć hasło?"))
        break
    except ValueError:
        print("Proszę podaj cyfrę:")
        continue
print("Ilość dużych liter:", characters_left)
update_characters_left(uppercase_letters)

#znaki specjalne
while True:
    try:
        special_characters = int(input("Ile znaków specjalnych ma mieć hasło?"))
        break
    except ValueError:
        print("Proszę podaj cyfrę:")
        continue
print("Ilość znaków specjalnych:", characters_left)
update_characters_left(special_characters)

#cyfry
while True:
    try:
        digits = int(input("Ile cyfr ma mieć hasło?"))
        break
    except ValueError:
        print("Proszę podaj cyfrę:")
        continue
print("Ilość cyfr:", characters_left)
update_characters_left(digits)


if characters_left > 0:
    print("\nNie wszystkie znaki zostały wykorzystane. Hasło zostanie uzupełnione małymi literami.")
    lowercase_letters += characters_left

# informacje nt generowanego hasla
print()
print("Długość hasła:", password_length)
print("Ilość małych liter:", lowercase_letters)
print("Ilość dużych liter:", uppercase_letters)
print("Ilość znaków specjalnych:", special_characters)
print("Ilość cyfr:", digits)


for _ in range(password_length):

    if lowercase_letters > 0:
        password.append(random.choice(string.ascii_lowercase))
        lowercase_letters -= 1

    if uppercase_letters > 0:
        password.append(random.choice(string.ascii_uppercase))
        uppercase_letters -= 1

    if special_characters > 0:
        password.append(random.choice(string.punctuation))
        special_characters -= 1

    if digits > 0:
        password.append(random.choice(string.digits))
        digits -= 1

random.shuffle(password)

print("Wygenerowane hasło:", "".join(password))
