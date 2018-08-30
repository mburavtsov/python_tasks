#The hex encoded string:

#1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736

#... has been XOR'd against a single character. Find the key, decrypt the message.
#You can do this by hand. But don't: write code to do it for you.
#How? Devise some method for "scoring" a piece of English plaintext. Character frequency is a good metric. Evaluate each output and choose the one with the best score.

from binascii import hexlify, unhexlify
import re

def singe_byte_XOR_cipher (encoded):

    nums = unhexlify(encoded)
    results = []

    for key in range (256):
        result = ''

        for num in nums:
            result += (chr(num ^ key))
        results.append(result)


    print(max(results, key=lambda s: len(re.findall('[a-zA-z]', s))))
    print(max(results, key=lambda s: s.count(' ')))



singe_byte_XOR_cipher("1b37373331363f78151b7f2b783431333d78397828372d363c78373e783a393b3736")



