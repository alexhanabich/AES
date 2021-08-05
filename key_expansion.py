from helper import byte_list_to_word, look_up, word_to_byte_list

rcon = [ 0x00000000, 
           0x01000000, 0x02000000, 0x04000000, 0x08000000, 
           0x10000000, 0x20000000, 0x40000000, 0x80000000, 
           0x1B000000, 0x36000000, 0x6C000000, 0xD8000000, 
           0xAB000000, 0x4D000000, 0x9A000000, 0x2F000000, 
           0x5E000000, 0xBC000000, 0x63000000, 0xC6000000, 
           0x97000000, 0x35000000, 0x6A000000, 0xD4000000, 
           0xB3000000, 0x7D000000, 0xFA000000, 0xEF000000, 
           0xC5000000, 0x91000000, 0x39000000, 0x72000000, 
           0xE4000000, 0xD3000000, 0xBD000000, 0x61000000, 
           0xC2000000, 0x9F000000, 0x25000000, 0x4A000000, 
           0x94000000, 0x33000000, 0x66000000, 0xCC000000, 
           0x83000000, 0x1D000000, 0x3A000000, 0x74000000, 
           0xE8000000, 0xCB000000, 0x8D000000 ]


def sub_word(word):
    byte_list = word_to_byte_list(word)
    for i in range(4):
        byte_list[i] = look_up(byte_list[i])
    word = byte_list_to_word(byte_list)
    return word


def rot_word(word):
    byte_list = word_to_byte_list(word)
    byte_list = byte_list[1:] + [byte_list[0]]
    word = byte_list_to_word(byte_list)
    return word


def key_expansion(key):
    nb = 4
    num_byte = len(key)
    nk = num_byte // 4
    nr = nk + 6
    w = [()]*(nb * (nr + 1))
    for i in range(nk):
        w[i] = byte_list_to_word((key[4*i], key[4*i+1], key[4*i+2], key[4*i+3]))
    for i in range(nk,(nb * (nr + 1))):
        temp = w[i - 1]
        if (i % nk) == 0:
            temp = sub_word(rot_word(temp)) ^ rcon[i // nk]
        elif (nk > 6 and i % nk == 4):
            temp = sub_word(temp)
        w[i] = w[i - nk] ^ temp
    return w