from collections import Counter

def find_it (seq):
    d = Counter(seq)
    for key, v in d.items():
        if v%2 != 0:
            return (key)



    return Counter(seq)


print (find_it([20,1,-1,2,-2,3,3,5,5,1,2,4,20,4,-1,-2,5]))