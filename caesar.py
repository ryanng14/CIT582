def encrypt(key,plaintext):
    ciphertext=""
    #YOUR CODE HERE
    for c in range(0, len(plaintext)):
        new_c = ((ord(plaintext[c]) + key - 65) % 26) + 65
        ciphertext = ciphertext + chr(new_c)
    return ciphertext

def decrypt(key,ciphertext):
    plaintext=""
    #YOUR CODE HERE
    for c in range(0, len(ciphertext)):
        new_c = ((ord(ciphertext[c]) - key - 65) % 26) + 65
        plaintext = plaintext + chr(new_c)
    return plaintext

