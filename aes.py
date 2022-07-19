import numpy as np
from cipher import cipher
from inv_cipher import inv_cipher
from helper import hex_print
from key_expansion import key_expansion


def split_arr(a, size):
    return np.split(a, np.arange(size,len(a),size))


BLOCK_SIZE = 16

class AES:

    def pad(self, input):
        r = input.size%BLOCK_SIZE
        padding = [0x80]
        for i in range(BLOCK_SIZE-1-r):
            padding.append(0x00)
        return np.append(input, padding)


    def unpad(self, input):
        pad_len = 0
        for i in range(len(input)-1, -1, -1):
            if input[i] == 0x00:
                pad_len += 1
            elif input[i] == 0x80:
                pad_len += 1
                break
        return np.resize(input, input.size-pad_len)


    # input: int_arr, output: int_arr 
    def encrypt(self, input, key):
        out = np.zeros((16,), dtype=int)
        w = key_expansion(key)
        cipher(input, out, w)
        return out
        
    
    # input: int_arr, output: int_arr 
    def decrypt(self, input, key):
        out = np.zeros((16,), dtype=int)
        w = key_expansion(key)
        inv_cipher(input, out, w)
        return out

    
    def ecb_encrypt(self, input, key):
        input = self.pad(input)
        cipher = []
        plain = split_arr(input, BLOCK_SIZE)
        for p_i in plain:
            c_i = self.encrypt(p_i, key)
            cipher.append(c_i)
        return np.concatenate(cipher)


    def ecb_decrypt(self, input, key):
        plain = []
        cipher = split_arr(input, BLOCK_SIZE)
        for c_i in cipher:
            p_i = self.decrypt(c_i, key)
            plain.append(p_i)
        u_plain = np.concatenate(plain)
        return self.unpad(u_plain)

    def cbc_encrypt(self, input, key):
        pass


    def cbc_decrypt(self, input, key):
        pass