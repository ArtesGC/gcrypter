from gcrypter.encrypt import encrypt
from gcrypter.decrypt import decrypt

if __name__ == '__main__':
    word_enc = encrypt("/home/nurul-gc/Projects/PycharmProjects/pypa-gcrypter/venv/bin/python /home/nurul-gc/Projects/PycharmProjects/pypa-gcrypter/src/tests/enc_test.py")
    print(word_enc)
    word_dec = decrypt(word_enc)
    print(word_dec)
