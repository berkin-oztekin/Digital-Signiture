import base64
import hashlib

from cryptography.fernet import Fernet

from KeyGen import getSrcPrivKey, public_KeyDST, RSA_encryption

with open("ID.txt", "r", encoding="utf-8") as file:
    source = file.read()


def hashID(ID):
    hashedID = hashlib.sha256(str.encode(ID))
    return hashedID.hexdigest()


def concatenate(x, y):
    return str(x) + str(y)


def symmetricCipher(x, y):
    result = (x + y) % 26
    return result


def performXOR(x, y):  # x ' e source private keyi y' ye destination public key verilecek
    new = [chr(ord(a) ^ ord(b)) for a, b in zip(x, y)]
    v3 = "".join(new)
    return v3


def performXOR2(x, y):
    return x ^ y


hashed_source = hashID(source)

print("Hashed source:", hashed_source)

# XOR (XOR(a1, a2)  XOR(b1, b2))
a = performXOR2(getSrcPrivKey()[0], public_KeyDST[0])
print(a)
b = performXOR2(getSrcPrivKey()[1], public_KeyDST[1])
print(b)
kH = (a, b)
print("kH=", kH)
encryptedHash = RSA_encryption(str(hashed_source), kH)

print("Encryped hash value:", encryptedHash)
Z = concatenate(str(source), '\n' + encryptedHash)
print(Z)

sessionKey = Fernet.generate_key()
fernet = Fernet(sessionKey)
z_encrypted = fernet.encrypt(Z.encode())
print("Fernet key:", sessionKey)
print("Fernet encrypted Z:", z_encrypted)

encryptedSessionKey = RSA_encryption(str(sessionKey), public_KeyDST)

print(encryptedSessionKey)

# z = symmetricCipher(int(z)), sessionKey)
# y = symmetricEncryption(sessionKey, public_KeyDST)
# signID = concatenate(str(z), str(y))
# print("Sign ID:", signID)
