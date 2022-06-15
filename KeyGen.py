from random import randint


def RSA_keyGen(p, q):
    # T
    N = p * q
    T = (p - 1) * (q - 1)
    e = findRelativelyPrimeNumberInRange(T)
    d = findSecondNumber(e, T)
    if d == None:
        e = findRelativelyPrimeNumberInRange(T)
        d = findSecondNumber(e, T)

    privateKey = (e, N)
    publicKey = (d, N)
    return privateKey, publicKey


def isRelativelyPrime(p, q):
    return gcd(p, q) == 1


def findRelativelyPrimeNumberInRange(y):
    list = []
    for i in range(y - 1):
        if i != 1 and i != 0:
            if isRelativelyPrime(i, y):
                return i


def is_prime(n):
    for i in range(2, n):
        if (n % i) == 0:
            return False
    return True


def findSecondNumber(e, n):
    liste = []
    for i in range(n):
        if ((e * i) - 1) % n == 0:
            return i


def gcd(p, q):
    while q != 0:
        p, q = q, p % q
    return p


srcPriv, srcPublic = RSA_keyGen(11, 17)

public_KeySRC = srcPublic


def getSrcPrivKey():
    return srcPriv

dstPriv, dstPublic = RSA_keyGen(29, 59)
# public_KeyComponentDST = DSTkeys[0]

public_KeyDST = dstPublic


def getDstPrivKey():
    #private_KeyComponentDST = DSTkeys[1]
    #private_KeyDST = (private_KeyComponentDST, N)
    return dstPriv


def RSA_encryption(text, key):
    ASCII_values = []
    result = ""
    N = key[1]
    e = key[0]
    for character in text:
        ASCII_values.append(ord(character))
    for ascii in ASCII_values:
        result += chr(pow(ascii, e) % N)
    return result


def RSA_decryption(text, key):
    ASCII_values = []
    result = ""
    N = key[1]
    d = key[0]
    for character in text:
        ASCII_values.append(ord(character))
    for ascii in ASCII_values:
        result += chr(pow(ascii, d) % N)
    return result


def symmetricDecryption(src, key):
    d = key[0]
    N = key[1]
    return pow(src, d) % N


def symmetricEncryption(src, key):  # rsa encryption böyle calısıyor ama src (hash bi sayı değil)
    e = key[0]
    N = key[1]
    return pow(src, e) % N


def random_with_N_digits(n):
    range_start = 10 ** (n - 1)
    range_end = (10 ** n) - 1
    return randint(range_start, range_end)
