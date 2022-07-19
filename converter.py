def file_to_ints(filename):
    with open(filename, 'rb') as f:
        content = f.read()
    return list(content)


def ints_to_file(ints, filename):
    with open(filename, 'wb+') as f:
        f.write(bytes(ints))

filename = 'test.png'
lst = file_to_ints(filename)

ints_to_file(lst, filename)