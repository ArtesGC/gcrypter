# ************************************************
#  (c) 2019-2021 Nurul-GC.                       *
#  - BSD 3-Clause License                        *
# ************************************************

from secrets import token_bytes
from typing import Tuple


def encrypt(text: str) -> Tuple[int, int]:
    """Function that encrypts the text given into
    numbers.

    :param text: the text to be encrypted
    :return: tuple with two tokens of numbers"""

    encoded = text.encode()
    enbyted = token_bytes(len(text))

    num_encoded = int.from_bytes(encoded, 'big')
    num_enbyted = int.from_bytes(enbyted, 'big')

    encrypted = num_encoded ^ num_enbyted
    return encrypted, num_enbyted
