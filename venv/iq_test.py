def iq_test(numbers):
    numbers_list = numbers.split()
    odd = []
    even = []

    for d in numbers_list:
        if int(d) % 2 == 0:
            even.append(d)
        else:
            odd.append(d)

    if len(odd) == 1:
        return ( numbers_list.index(odd[0])+1)
    else:
        return (numbers_list.index(even[0])+1)












    #print(l_numbers)



iq_test("2 4 7 8 10")