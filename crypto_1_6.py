import codecs


def calculate_hamming_distance (a_string, b_string):
    h_distance = 0
    #a_string_bin = ''.join('{0:08b}'.format(ord(x), 'b') for x in a_string)
    #b_string_bin = ''.join('{0:08b}'.format(ord(x), 'b') for x in b_string)

    a_tuple_bin = ''.join('{0:08b}'.format(x, 'b') for x in a_string)
    b_tuple_bin = ''.join('{0:08b}'.format(x, 'b') for x in b_string)

    for a, b in zip(a_tuple_bin, b_tuple_bin):
        if a != b:
            h_distance += 1

    return h_distance


with open("C:\\base\\plain_text.txt", 'rt') as file:
    data = file.read().replace('\n', '')


    source_unbased = codecs.decode(bytes(data, 'utf-8'), 'base64')

    #KEYSIZE = 3

    #parts = [source_unbased[i:i + KEYSIZE] for i in range(0, len(source_unbased), KEYSIZE)]


    for KEYSIZE in range (2, 40):
        parts = [source_unbased[i:i + KEYSIZE] for i in range(0, len(source_unbased), KEYSIZE)]
        h_distance_normalized = calculate_hamming_distance(parts[0], parts[1])/KEYSIZE
        KEYSIZE, h_distance_normalized

    #KEYSIZE 5 shows distance 1.2. assuming that key is size of 5;

    #breaking ciphered text on blocks of size 5


    KEYSIZE = 5
    parts = [source_unbased[i:i + KEYSIZE] for i in range(0, len(source_unbased), KEYSIZE)]

    #form new blocks. each has N-th byte of each block

    b0 = []
    b1 = []
    b2 = []
    b3 = []
    b4 = []

    for p in parts:
        if len(p) == 5:
            b0.append(p[0])

    for p in parts:
        if len(p) == 5:
            b1.append(p[1])

    for p in parts:
        if len(p) == 5:
            b2.append(p[2])

    for p in parts:
        if len(p) == 5:
            b3.append(p[3])
    for p in parts:
        if len(p) == 5:
            b4.append(p[4])

    print(b0)
    print(b1)
    print(b2)
    print(b3)
    print(b4)



