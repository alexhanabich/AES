import chunk
from aes import AES
from helper import hex_print
import numpy as np
from converter import file_to_ints, ints_to_file, str_to_ints, ints_to_str

aes = AES()
# convert file to int
ints = '00112233445566778899aabbccddeeff'
key = '000102030405060708090a0b0c0d0e0f'
ints = str_to_ints(ints)
key = str_to_ints(key)
cipher = aes.encrypt(ints, key)
cipher = ints_to_str(cipher)
print(cipher == '69c4e0d86a7b0430d8cdb78070b4c55a')