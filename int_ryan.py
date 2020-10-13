import time

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
    if(len(intArray) < 1) : return True

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

inputs = [
           [1, 2, 4, 8],
           [0],
           [9],
           [],
           [1, 4, 8],
           [16, 1, 4, 8],
           [16, 1, 4, 8],
           [16, 1, 4, 8],
           [0, 17, 4, 18, 200]
       ]
targets = [7,0,9,0,7,11,26,25,19]
answers = [ 'true',
        'true',
        'true',
        'true',
        'false',
        'false',
        'false',
        'true',
        'true']
i = 0
for input, target in zip(inputs, targets):
    print('target:',target)
    print('intArray:',input)
    time.sleep(1)
    if(bitWiseORArray(input,target)):
        print('true')
        if answers[i] == 'true':
            print('CORRECT\n\n')
        else:
            print('WRONG\n\n')
    else:
        print('false')
        if answers[i] == 'false':
            print('CORRECT\n\n')
        else:
            print('WRONG\n\n')
    i = i +1
