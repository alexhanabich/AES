from cipher import add_round_key
from helper import ff_multiply, hex_print_matrix, inv_look_up, to_list, to_matrix, transpose, words_to_key

def inv_sub_bytes(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            state[i][j] = inv_look_up(state[i][j])


def inv_shift_rows(state):
    for i in range(len(state)):
        for _ in range(i):
            state[i] = [state[i][-1]] + state[i][:-1]


def inv_mix_columns(state):
    transposed_state = transpose(state)
    for col in transposed_state:
        copy = col.copy()
        col[0] = ff_multiply(0x0e,copy[0]) ^ ff_multiply(0x0b,copy[1]) ^ ff_multiply(0x0d,copy[2]) ^ ff_multiply(0x09,copy[3])
        col[1] = ff_multiply(0x09,copy[0]) ^ ff_multiply(0x0e,copy[1]) ^ ff_multiply(0x0b,copy[2]) ^ ff_multiply(0x0d,copy[3])
        col[2] = ff_multiply(0x0d,copy[0]) ^ ff_multiply(0x09,copy[1]) ^ ff_multiply(0x0e,copy[2]) ^ ff_multiply(0x0b,copy[3])
        col[3] = ff_multiply(0x0b,copy[0]) ^ ff_multiply(0x0d,copy[1]) ^ ff_multiply(0x09,copy[2]) ^ ff_multiply(0x0e,copy[3])
    state[:] = transpose(transposed_state)


def inv_cipher(state, state_out, w):
    nb = 4
    nr = len(w)//4 - 1
    state = to_matrix(state)
    add_round_key(state,  words_to_key(w, nr * nb, (nr + 1) * nb - 1))
    for i in range(nr-1, 0, -1):
        inv_shift_rows(state)
        inv_sub_bytes(state)
        add_round_key(state, words_to_key(w, i * nb, (i + 1) * nb - 1))
        inv_mix_columns(state)
    inv_shift_rows(state)
    inv_sub_bytes(state)
    add_round_key(state,  words_to_key(w, 0, nb - 1))
    state_out[:] = to_list(state)