#Here is the opening stanza of an important work of the English language:

#Burning 'em, if you ain't quick and nimble
#I go crazy when I hear a cymbal
#Encrypt it, under the key "ICE", using repeating-key XOR.

#In repeating-key XOR, you'll sequentially apply each byte of the key; the first byte of plaintext will be XOR'd against I, the next C, the next E, then I again for the 4th byte, and so on.

#It should come out to:

#0b3637272a2b2e63622c2e69692a23693a2a3c6324202d623d63343c2a26226324272765272
#a282b2f20430a652e2c652a3124333a653e2b2027630c692b20283165286326302e27282f

from binascii import hexlify, unhexlify
def repeating_key_XOR (source, key):
    print (len(source))

    key_full = key*(len(source)//len(key)) + key[0:(len(source) % len(key))]


    xored = bytes([ord(b1) ^ ord(b2) for b1, b2 in zip(source, key_full)])

    result = hexlify(xored).decode('ascii')

    return result



#with open("C:\\base\\plain_text.txt", 'rt') as file:

print(repeating_key_XOR("Thanks for coming back to us, as I’m off for two weeks after today Jim has kicked",
                        "ICE"
                        )
      )


