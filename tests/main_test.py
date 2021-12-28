# ************************************************
#  (c) 2019-2021 Nurul-GC.                       *
#  - BSD 3-Clause License                        *
# ************************************************

from gcrypter import encrypt, decrypt

if __name__ == '__main__':
    word_enc = encrypt("love")
    print(word_enc)
    word_dec = decrypt(word_enc)
    print(word_dec)
