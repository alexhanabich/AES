from main import AES 

aes = AES()
in_file = 'test.png'
out_file = 'out.png'
key = '2b7e151628aed2a6abf7158809cf4f3c'
file = aes.ecb_encrypt_file(in_file, out_file, key)