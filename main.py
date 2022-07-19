from aes import AES
from helper import hex_print
import numpy as np
from converter import file_to_ints, ints_to_file

aes = AES()
input = np.array([0x32 , 0x43 , 0xf6 , 0xa8 , 0x88 , 0x5a , 0x30 , 0x8d , 0x31 , 0x31 , 0x98 , 0xa2 , 0xe0 , 0x37 , 0x07 , 0x34])
key = np.array([0x2b, 0x7e, 0x15, 0x16, 0x28, 0xae, 0xd2, 0xa6, 0xab, 0xf7, 0x15, 0x88, 0x09, 0xcf, 0x4f, 0x3c])
ciphertext = aes.encrypt(input, key)
plaintext = aes.decrypt(ciphertext, key)
hex_print(plaintext)

# filename = 'test.png'
# lst = np.array(file_to_ints(filename))
# ciphertext = aes.ecb_encrypt(lst, key)

# plaintext = aes.ecb_decrypt(ciphertext, key)

# ints_to_file(plaintext, 'out.png')