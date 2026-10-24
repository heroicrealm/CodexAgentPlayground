name = input("Как вас зовут? ")
print(f"Привет, {name}!")
letter_count = sum(character.isalpha() for character in name)
print(f"Количество букв в вашем имени: {letter_count}")
