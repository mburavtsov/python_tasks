#Write a function that takes two equal-length buffers and produces their XOR combination.
#If your function works properly, then when you feed it the string:
#1c0111001f010100061a024b53535009181c
#... after hex decoding, and when XOR'd against:
#686974207468652062756c6c277320657965
#... should produce:
#746865206b696420646f6e277420706c6179

from binascii import hexlify, unhexlify

def fixed_XOR(source, cipher):


    bytes1, bytes2 = unhexlify(source), unhexlify(cipher)

    xor_bytes = bytes([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)])
    print(bytes([b1 ^ b2 for b1, b2 in zip(bytes1, bytes2)]))

    result = hexlify(xor_bytes).decode('ascii')

    return result



fixed_XOR("1c0111001f010100061a024b53535009181c", "686974207468652062756c6c277320657965")