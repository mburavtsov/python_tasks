import re
def abbreviate(s):
    result = []
    list_of_words_with_spaces =  re.split(r"[^a-zA-Z0-9]", s)


    def Contains_Digit(input):
        return any(char.isdigit() for char in input)

    for word in list_of_words_with_spaces:
        if len(word) > 3:
            if Contains_Digit(word):


            result.append(word[0] + str(len(word)-2)+ word[-1])
        else:
            result.append(word)




    return result




print (abbreviate("monolithic_is; sits'the5balloon: monolithic: the_sits; mat"))


#re.split(r"[^a-zA-Z0-9]"