def encrypt(plainText, key):
    if 0 < key < 27:
        result = ""
        plainText = plainText.lower()

        for i in range(len(plainText)):
            char = plainText[i]
            if char == ' ':
                result += " "
            else:
                result += chr((ord(char) + key - 97) % 26 + 97)  # chr() return string that represent as character
            # ord('a') return 97
        return result
    else:
        return "Please input positive key!"


def decrypt(cipherText, key):
    if 0 < key < 27:
        result = ""
        cipherText = cipherText.lower()

        for i in range(len(cipherText)):
            char = cipherText[i]
            if char == ' ':
                result += " "
            else:
                result += chr((ord(char) - key - 97) % 26 + 97)
        return result
    else:
        return "Please enter the positive key!"


def bruteForceAttack(cipherText):
    LETTERS = 'abcdefghijklmnopqrstuvwxyz'
    cipherText = cipherText.lower()
    for key in range(len(LETTERS)):
        translated = ''
        for symbol in cipherText:
            if symbol in LETTERS:
                if symbol == " ":
                    translated += " "
                num = LETTERS.find(symbol)
                num = num - key
                if num < 0:
                    num = num + len(LETTERS)
                translated = translated + LETTERS[num]
            else:
                translated = translated + symbol
        print('Hacking key #%s: %s' % (key, translated))


message = str(input("Enter the message: "))
key = int(input("Enter the key: "))
print("Cipher text : " + encrypt(message, key))
print("Plain text : " + decrypt(encrypt(message, key), key))
bruteForceAttack(encrypt(message,key))

