#One of the 60-character strings in this file has been encrypted by single-character XOR.
#Find it.
#(Your code from #3 should help.)



#Opening and reading the file

from binascii import hexlify, unhexlify
import math

English_freq = [
    0.08167, 0.01492, 0.02782, 0.04253, 0.12702, 0.02228, 0.02015,  # a-g
    0.06094, 0.06966, 0.00153, 0.00772, 0.04025, 0.02406, 0.06749,  # h-n
    0.07507, 0.01929, 0.00095, 0.05987, 0.06327, 0.09056, 0.02758,  # o-u
    0.00978, 0.02360, 0.00150, 0.01974, 0.00074                     # v-z
]

def getChi2 (string):
    count = []
    ignored = 0

    count = [0 for i in range(0, 26)]


    for i in string.lower():
        c = ord(i)
        if c >=97 and c <=122:
            count[c-97] +=1
        elif c>=32 and c<=126:
            ignored += 1
        elif c == 9 or c == 10 or c == 13:
            ignored += 1
        else:
            return math.inf



    chi2 = 0
    length = len(string) - ignored

    for i in range(0, 26):
        observed = count[i]
        expected = length * English_freq[i]

        difference = observed - expected
        if expected != 0:
            chi2 += difference**2 / expected

    return chi2

def singe_byte_XOR_cipher(encoded):

    nums = unhexlify(encoded)
    strings = (''.join(chr(num ^ key) for num in nums) for key in range(256))
    result = filter_results(strings)


    return result



def filter_results(strings):
    min_score = 100000
    result = ''
    for s in strings:
        if getChi2(s) != 0 and getChi2(s) < min_score and ' ' in s:
            min_score = getChi2(s)
            result = s
            print (result)

    return result



with open("C:\\base\\github\\python\Crypto_1_4_text.txt", 'rt') as f:
    oputs = (''.join(singe_byte_XOR_cipher(line.rstrip())) for line in f)
    print (filter_results(oputs))




