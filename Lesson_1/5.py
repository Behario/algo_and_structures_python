#5.	Пользователь вводит две буквы. Определить, на каких местах
# алфавита они стоят, и сколько между ними находится букв.
import string

ALPHABET = string.ascii_lowercase
LETTER_LEFT = input("Введите букву левой границы алфавита: ")
LETTER_LEFT = LETTER_LEFT.lower()
LETTER_RIGHT = input("Введите букву правой границы алфавита: ")
LETTER_RIGHT = LETTER_RIGHT.lower()
INDEX_LEFT = ALPHABET.index(LETTER_LEFT)
INDEX_RIGHT = ALPHABET.index(LETTER_RIGHT)
RANGE = ALPHABET[INDEX_LEFT:INDEX_RIGHT+1]

print(f"Первая буква {LETTER_LEFT} находится на позиции {INDEX_LEFT + 1};\n"
      f"Вторая буква {LETTER_RIGHT} находится на позиции {INDEX_RIGHT + 1};\n"
      f"Между ними находится ровно {len(RANGE) - 2} буквы")
