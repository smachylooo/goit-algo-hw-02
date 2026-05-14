from collections import deque

def is_palindrome(text):
    clean_text = text.lower().replace(" ", "")
    symbols = deque(clean_text)

    while len(symbols) > 1:
        if symbols.popleft() != symbols.pop():
            return False

    return True

text = input("Введіть рядок: ")

if is_palindrome(text):
    print("Це паліндром")
else:
    print("Це не паліндром")