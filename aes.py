import numpy as np
from cipher import cipher
from inv_cipher import inv_cipher
from helper import hex_print
from key_expansion import key_expansion
# from inv_cipher import inv_cipher

class AES:
    # input: hex_list, output: hex_list    
    def encrypt(self, input, key):
        out = np.zeros((16,), dtype=int)
        w = key_expansion(key)
        cipher(input, out, w)
        return out
        
    
    # input: hex_list, output: hex_list   
    def decrypt(self, input, key):
        out = np.zeros((16,), dtype=int)
        w = key_expansion(key)
        inv_cipher(input, out, w)
        return out