#For some reason extra chars are returned which are not part of the string, so taking result[0] does not rerun that char

import codecs

def convert_hex_to_b64 (string):
    #print(string)

    string_noencode = codecs.decode(string, 'hex')

    print(string_noencode)


    string_64 = codecs.encode(string_noencode, 'base64')[:-1]
    print(string_64)
    return 0


convert_hex_to_b64("49276d206b696c6c696e6720796f757220627261696e206c696b65206120706f69736f6e6f7573206d757368726f6f6d")
