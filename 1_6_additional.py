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

    #nums = unhexlify(encoded)
    strings = (''.join(chr(num ^ key) for num in encoded) for key in range(256))
    result = filter_results(strings)


    return result



def filter_results(strings):
    min_score = 100000
    result = ''
    for s in strings:
        if getChi2(s) != 0 and getChi2(s) < min_score and ' ' in s:
            min_score = getChi2(s)
            result = s
            print(result)


    return result



b0 = [29, 15, 78, 31, 19, 27, 0, 32, 51, 6, 13, 12, 30, 17, 26,
      29, 9, 83, 12, 1, 0, 71, 69, 9, 8, 31, 98, 65, 26, 116, 26,
      122, 58, 26, 29, 1, 65, 49, 6, 11, 73, 27, 7, 78, 7, 8, 84,
      25, 22, 105, 2, 7, 1, 2, 27, 54, 84, 78, 59, 15, 0, 28, 84,
      79, 12, 14, 61, 73, 13, 14, 11, 7, 78, 11, 0, 31, 77, 14, 65,
      71, 79, 66, 12, 6, 42, 89, 7, 49, 10, 89, 29, 19, 14, 11, 4,
      48, 28, 26, 8, 82, 19, 92, 15, 44, 7, 25, 27, 42, 2, 79, 22,
      8, 23, 101, 0, 25, 53, 58, 73, 1, 13, 22, 0, 0, 48, 26, 98,
      32, 82, 17, 78, 6, 11, 23, 29, 101, 71, 74, 65, 69, 16, 19,
      46, 78, 100, 116, 3, 65, 82, 0, 10, 9, 9, 48, 73, 6, 2, 7,
      16, 95, 29, 69, 83, 64, 79, 78, 8, 77, 10, 6, 29, 33, 0, 78,
      60, 78, 67, 82, 17, 14, 12, 8, 49, 6, 27, 4, 23, 0, 26, 78,
      6, 22, 77, 27, 65, 71, 0, 8, 1, 23, 72, 76, 61, 58, 61, 78,
      54, 21, 7, 22, 5, 54, 6, 6, 73, 19, 54, 85, 78, 69, 29, 77,
      2, 89, 40, 65, 19, 25, 27, 35, 80, 13, 33, 26, 89, 23, 27,
      65, 10, 65, 54, 27, 7, 10, 29, 17, 26, 29, 10, 83, 20, 67,
      69, 75, 0, 4, 12, 33, 39, 87, 15, 59, 1, 78, 82, 29, 101,
      69, 13, 59, 25, 24, 4, 27, 21, 83, 78, 10, 7, 12, 79, 79,
      6, 0, 69, 7, 29, 41, 79, 23, 53, 7, 84, 0, 84, 6, 44, 18,
      52, 8, 7, 6, 19, 1, 26, 27, 13, 22, 12, 29, 67, 71, 0, 28,
      12, 4, 35, 82, 0, 45, 26, 78, 29, 53, 7, 13, 65, 44, 6, 79,
      26, 23, 19, 77, 73, 8, 83, 5, 63, 83, 109, 80, 22, 27, 25,
      5, 78, 7, 53, 10, 84, 19, 28, 1, 10, 107, 61, 6, 24, 73, 27, 61,
      79, 11, 66, 29, 12, 14, 0, 15, 78, 2, 0, 82, 54, 121, 28, 48, 1,
      65, 82, 19, 7, 60, 8, 48, 0, 7, 25, 28, 84, 26, 1, 4, 75, 77, 6,
      121, 64, 83, 28, 73, 7, 53, 78, 8, 116, 15, 0, 6, 29, 0, 10, 65,
      49, 6, 7, 73, 28, 24, 26, 10, 69, 18, 9, 72, 0, 109, 83, 0, 0, 23,
      98, 99, 1, 58, 2, 100, 43, 17, 12, 69, 21, 120, 73, 72, 12, 23, 0, 26, 6, 17,
      58, 9, 10, 67, 71, 0, 6, 28, 29, 44, 78, 11, 53, 55, 65, 16, 17, 66, 28, 77, 47,
      73, 29, 28, 6, 61, 26, 66, 73, 84, 8, 29, 42, 8, 78, 0, 13, 22, 37, 83, 9, 53,
      78, 0, 82, 13, 6, 28, 65, 61, 69, 31, 73, 21, 24, 82, 27, 8, 83, 5, 13, 71, 14,
      79, 10, 16, 28, 98, 73, 10, 45, 26, 75, 1, 29, 0, 0, 49, 44, 15, 72, 10, 23, 84,
      26, 2, 0, 1, 12, 14, 78, 18, 87, 69, 16, 19, 110, 0, 62, 32, 8, 0, 17, 29, 79, 0,
      22, 57, 8, 6, 28, 82, 17, 26, 78, 38, 28, 2, 1, 65, 6, 78, 16]


strings = (''.join(chr(num ^ key) for num in b0) for key in range(256))
for s in strings:
    print (getChi2(s))
