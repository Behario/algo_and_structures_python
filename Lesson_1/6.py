# 6.	Пользователь вводит номер буквы в алфавите. Определить, какая это буква.

import string

ALPHABET = string.ascii_lowercase
LETTER_INDEX = int(input("Введите номер буквы из английского алфавита: "))
LETTER_FINDER = ALPHABET[LETTER_INDEX-1]
print(f"Ваша буква: {LETTER_FINDER}")