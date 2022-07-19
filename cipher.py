import numpy as np
from helper import get_sbox, ff_mult, to_matrix, to_matrix, get_round_key, add_round_key

# substitute bytes with sbox
def sub_bytes(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            state[i][j] = get_sbox(state[i][j])


# shift ith row by -i
def shift_rows(state):
    for i in range(len(state)):
        state[i] = np.roll(state[i], -i)


# mix columns
def mix_columns(state):
    for col in np.transpose(state):
        copy = np.copy(col)
        col[0] = ff_mult(2,copy[0]) ^ ff_mult(3,copy[1]) ^ copy[2] ^ copy[3]
        col[1] = copy[0] ^ ff_mult(2,copy[1]) ^ ff_mult(3,copy[2]) ^ copy[3]
        col[2] = copy[0] ^ copy[1] ^ ff_mult(2,copy[2]) ^ ff_mult(3,copy[3])
        col[3] = ff_mult(3,copy[0]) ^ copy[1] ^ copy[2] ^ ff_mult(2,copy[3])


# input: 128bit block, output: 128bit block
def cipher(input, output, w):
    nb = 4
    nr = len(w)//4 - 1
    state = to_matrix(input)
    add_round_key(state, get_round_key(w, 0, nb-1))
    for i in range(1, nr):
        sub_bytes(state)
        shift_rows(state)
        mix_columns(state)
        add_round_key(state, get_round_key(w, i*nb, (i+1)*nb-1))
    sub_bytes(state)
    shift_rows(state)
    add_round_key(state,  get_round_key(w, nr*nb, (nr+1)*nb-1))
    output[:] = np.transpose(state).flatten()