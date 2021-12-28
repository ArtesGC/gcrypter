# ************************************************
#  (c) 2019-2021 Nurul-GC.                       *
#  - BSD 3-Clause License                        *
# ************************************************

from typing import Tuple


def decrypt(text_enc: Tuple[int, int]) -> str:
    """Function that decrypt the tuple of tokens
    and re-convert them into string.

    :param text_enc: the tuple of the text encrypted
    :return: the text decrypted
    """
    encrypted = text_enc[0] ^ text_enc[1]
    decrypted = encrypted.to_bytes((encrypted.bit_length() + 7) // 8, 'big')
    return decrypted.decode()
