def encrypt(text: str) -> str:
    words = []
    for word in text.split():
        new_word = ''
        word_len = len([c for c in word if c.isupper() or c.islower()])
        for char in word:
            if char.isupper():
                new_word += chr((ord(char) + word_len - 65) % 26 + 65)
            elif char.islower():
                new_word += chr((ord(char) + word_len - 97) % 26 + 97)
            else:
                new_word += char
        words.append(new_word)
    return ' '.join(words)

text = input()
print(encrypt(text))