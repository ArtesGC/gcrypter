from gcrypter import encrypt, decrypt

if __name__ == '__main__':
    word_enc = encrypt("love")
    print(word_enc)
    word_dec = decrypt(word_enc)
    print(word_dec)
