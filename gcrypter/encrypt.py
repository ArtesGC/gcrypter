# ******************************************************************************
#  (c) 2019-2021 Nurul-GC.                                                     *
# ******************************************************************************
"""
GCrypter-API
"""
from secrets import token_bytes


def encrypt(text: str):
    """funcao encriptadora"""
    encoded = text.encode()
    enbyted = token_bytes(len(text))

    num_encoded = int.from_bytes(encoded, 'big')
    num_enbyted = int.from_bytes(enbyted, 'big')

    encrypted = num_encoded ^ num_enbyted
    return encrypted, num_enbyted
