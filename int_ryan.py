def NOR(a, b):
    if(a == '0') and (b == '0'):
        return True
    elif(a == '0') and (b == '1'):
        return False
    elif(a == '1') and (b == '0'):
        return False
    elif(a == '1') and (b == '1'):
        return False
def OR(a, b):
    if a == '1':
        return True
    elif b == '1':
        return True
    else:
        return False

def bitWiseORArray(intArray, target):
    sum_found = False
    if(len(intArray) < 1) : return sum_found

    possilbe_solutions = list()
    #possilbe_solutions_bin = list()
    target_binary = list(reversed(bin(target)[2:]))
    for number in intArray:
        if number > target: continue
        number_binary = list(reversed(bin(number)[2:]))
        index = 0
        bit_good = None
        for bit in number_binary:
            if (target_binary[index]) == '0':
                if(NOR(target_binary[index], bit)):
                    bits_good = True
                else:
                    bits_good = False
            else:
                bits_good= True
            index = index + 1
        if bits_good:
            possilbe_solutions.append(number)
            #possilbe_solutions_bin.append(bin(number))
    bitwiseORsolution = 0
    for number in possilbe_solutions:
        bitwiseORsolution |= number
    if bitwiseORsolution == target:
        sum_found = True
    else:
        sum_found = False
    #print('Possible Solutions:',possilbe_solutions_bin)
    return sum_found


array_to_test = [10, 9, 8]
sum_to_test = 7
print('target:',sum_to_test)
print('intArray:',array_to_test)
if(bitWiseORArray(array_to_test,sum_to_test)):
    print('Possilbe')
else:
    print('Not Possible')
