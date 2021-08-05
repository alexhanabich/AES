from helper import ff_multiply, hex_print_list, hex_print_matrix, look_up, to_list, to_matrix, transpose, words_to_key

def sub_bytes(state):
    for i in range(len(state)):
        for j in range(len(state[i])):
            state[i][j] = look_up(state[i][j])


def shift_rows(state):
    for i in range(len(state)):
        for _ in range(i):
            state[i] = state[i][1:] + [state[i][0]]


def mix_columns(state):
    transposed_state = transpose(state)
    for col in transposed_state:
        copy = col.copy()
        col[0] = ff_multiply(2,copy[0]) ^ ff_multiply(3,copy[1]) ^ copy[2] ^ copy[3]
        col[1] = copy[0] ^ ff_multiply(2,copy[1]) ^ ff_multiply(3,copy[2]) ^ copy[3]
        col[2] = copy[0] ^ copy[1] ^ ff_multiply(2,copy[2]) ^ ff_multiply(3,copy[3])
        col[3] = ff_multiply(3,copy[0]) ^ copy[1] ^ copy[2] ^ ff_multiply(2,copy[3])
    state[:] = transpose(transposed_state)


def add_round_key(state, key):
    key = to_matrix(key)
    for i in range(len(state)):
        for j in range(len(state[i])):
            state[i][j] ^= key[i][j]


def cipher(state, state_out, w):
    nb = 4
    nr = len(w)//4 - 1
    state = to_matrix(state)
    add_round_key(state, words_to_key(w, 0, nb - 1))
    for i in range(1, nr):
        sub_bytes(state)
        shift_rows(state)
        mix_columns(state)
        add_round_key(state, words_to_key(w, i * nb, (i + 1) * nb - 1))
    sub_bytes(state)
    shift_rows(state)
    add_round_key(state,  words_to_key(w, nr * nb, (nr + 1) * nb - 1))
    state_out[:] = to_list(state)