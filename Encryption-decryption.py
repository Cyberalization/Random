KEY = 13

# ====================================================================
# Vigenere
def move_key(charMessage, charKey):
    return ((charMessage + charKey) % 26) + ord('A')

def extend_key(key, length):
    keyIndex = 0
    keyLength = len(key)
    newKey = ""
    for _ in range(length):
        if keyIndex == keyLength:
            keyIndex = 0
        newKey += key[keyIndex]
    print("Generated new key")
    return newKey

def vigenere_encryption(message, key):
    encryptedMessage = ""
    length = len(message)
    for index in range(length):
        if message[index].isalpha():
            encryptedMessage += chr(move_key(ord(message[index]), ord(key[index])))
    return encryptedMessage

def vigenere_decryption(message, key):
    decryptedMessage = ""
    length = len(message)
    for index in range(length):
        if message[index].isalpha():
            decryptedMessage += chr(move_key(ord(message[index]), -ord(key[index])))
    return decryptedMessage

# ====================================================================
# ROT13

def rot13_encryption(message):
    encryptedMessage = ""
    length = len(message)
    for index in range(length):
        asciiNum = ord(message[index])
        if asciiNum >= 97 and asciiNum <= 109:
            asciiNum += KEY
        elif asciiNum >= 110 and asciiNum <= 122:
            asciiNum -= KEY
        elif asciiNum >= 65 and asciiNum <= 77:
            asciiNum += KEY
        elif asciiNum >= 78 and asciiNum <= 90:
            asciiNum -= KEY
        elif asciiNum >= 32 and asciiNum <= 64:
            asciiNum += KEY
        encryptedMessage += chr(asciiNum)
    return encryptedMessage

def rot13_decryption(message):
    decryptedMessage = ""
    length = len(message)
    for index in range(length):
        asciiNum = ord(message[index])
        if asciiNum >= 97 and asciiNum <= 109:
            asciiNum -= KEY
        elif asciiNum >= 110 and asciiNum <= 122:
            asciiNum += KEY
        elif asciiNum >= 65 and asciiNum <= 77:
            asciiNum -= KEY
        elif asciiNum >= 78 and asciiNum <= 90:
            asciiNum += KEY
        elif asciiNum >= 32 and asciiNum <= 64:
            asciiNum -= KEY
        decryptedMessage += chr(asciiNum)
    return decryptedMessage

# ====================================================================
# XOR
def xor_encryption(message, numKeyFirst, numKeySecond):
    encryptedMessage = ""
    length = len(message)
    for index in range(length):
        if index % 2 == 0:
            encryptedMessage += chr(ord(message[index]) ^ numKeyFirst)
        elif index > 100:
            encryptedMessage += chr(ord(message[index]) ^ numKeyFirst ^ numKeySecond)
        else:
            encryptedMessage += chr(ord(message[index]) ^ numKeySecond)
    return encryptedMessage

# ====================================================================

def encryption(message, key, numKeyFirst, numKeySecond):
    # step 1: Vigenere
    cipher = vigenere_encryption(message, key)

    # step 2: ROT13
    cipher = rot13_encryption(cipher)
    # print(cipher)

    # step 3: XOR
    cipher = xor_encryption(cipher, numKeyFirst, numKeySecond)
    return cipher

def decryption(message, key, numKeyFirst, numKeySecond):
    # step 1: XOR
    plain = xor_encryption(cipher, numKeyFirst, numKeySecond)

    # step 2: ROT13
    plain = rot13_encryption(plain)

    # step 3: Vigenere
    plain = vigenere_decryption(plain, key)
    return plain

# message = input("Input plaintext: ").upper()
# key = input("Input key: ").upper()
# numKeyFirst = int(input("Input angka untuk enkripsi pertama: "))
# numKeySecond = int(input("Input angka untuk enkripsi kedua: "))

# Testing Input
message = "Testing".upper()
key = "Helo".upper()
numKeyFirst = 3
numKeySecond = 10

# encryption
# extend key nya buat Vigenere
key = extend_key(key, len(message))
# encrypt message nya menggunakan key nya
cipher = encryption(message, key, numKeyFirst, numKeySecond)
print("Cipher: " + cipher)

# decryption
plain = decryption(message, key, numKeyFirst, numKeySecond)
print("Plaintext: " + plain)