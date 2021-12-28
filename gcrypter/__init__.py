# ************************************************
#  (c) 2019-2021 Nurul-GC.                       *
#  - BSD 3-Clause License                        *
# ************************************************

"""
gcrypter
    Is an encryption algorithm based on bytes and their correspondent numbers to encode strings.

- To Encrypt:
    - It gets the length of the text given and encode both (text and lenght) into bytes
    then convert the bytes'values into numbers and return a tuple with two tokens (numbers);

- To Decrypt:
    - It gets the tuple and retrieve both the values and reconvert them into bytes
    according to his bit-length and then decode the byte to the original string (text);

(c) 2019-2021 Nurul-GC.
"""

from gcrypter.encrypt import encrypt
from gcrypter.decrypt import decrypt

__author__ = "Nurul-GC"
__license__ = "BSD 3-Clause License"
__copyright__ = "© 2019-2021 Nurul-GC"
__trademark__ = "™ ArtesGC-DevSoft"
