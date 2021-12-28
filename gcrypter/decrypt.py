# ******************************************************************************
#  (c) 2019-2021 Nurul-GC.                                                     *
# ******************************************************************************
"""
GCrypter-API
"""
from typing import Tuple


def decrypt(text_enc: Tuple[int, int]):
    """funcao desencriptadora"""
    encrypted = text_enc[0] ^ text_enc[1]
    decrypted = encrypted.to_bytes((encrypted.bit_length() + 7) // 8, 'big')
    return decrypted.decode()
