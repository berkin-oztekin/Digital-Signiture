from KeyGen import getDstPrivKey, RSA_decryption
from Source import encryptedSessionKey, z_encrypted, sessionKey
from cryptography.fernet import Fernet
import hashlib


print("-------Destination Side---------")
decryptedSessionKey = RSA_decryption(encryptedSessionKey, getDstPrivKey())

print(decryptedSessionKey == sessionKey)
print("Decrypted Session Key:", len(decryptedSessionKey), decryptedSessionKey)
print("Encrypted Session Key:", len(sessionKey), sessionKey)


fernet = Fernet(sessionKey)

z_decrypt = fernet.decrypt(z_encrypted).decode()

print("Fernet decrypted Z:", z_decrypt)

Z = z_decrypt.split('\n')

sourceWithoutHash = Z[:-1]
result = ''

for i in range(len(sourceWithoutHash)):
    if i == len(sourceWithoutHash) - 1:
        result += (sourceWithoutHash[i])
    else:
        result += (sourceWithoutHash[i] + '\n')

print("Source without the hash:\n" + result)

hash_computed = hashlib.sha256(str.encode(result))

encryptedHash = Z[-1]

print("Encrypted hash:", encryptedHash)

print("Hash Computed:", hash_computed.hexdigest())

