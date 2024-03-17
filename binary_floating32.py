'''
    * IEEE-754 Binary-32 floating point converter (including all special cases)
    • Input: (1) binary mantissa and base-2 (i.e., 101.01x25) (2) Decimal and base-10 (i.e.
    65.0x103). Also should support special cases (i.e., NaN).
    • Output: (1) binary output with space between section (2) its hexadecimal equivalent (3)
    with option to output in text file.
'''

def checkFormat(sNum):
    ctr = 0
    dot = 0
    while ctr < len(sNum):
        if sNum[ctr] == '.':
            dot += 1
        if dot > 1:
            return False
        if ctr == len(sNum)-1:
            break
        ctr += 1
    return True

def checkBinary(sNum):
    ctr = 0
    while ctr < len(sNum):
        if sNum[ctr] != '0' and sNum[ctr] != '1' and sNum[ctr] != '.':
            return False
        if ctr == len(sNum)-1:
            break
        ctr += 1
    return True

def getExponent(sNum, nExp):
    dot = sNum.index('.')
    ctr = 0
    while ctr < len(sNum):
        if sNum[ctr] == '1':
            one = ctr
            break
        if ctr == len(sNum)-1:
            break
        ctr += 1
    
    if dot > one:
        adjust = dot - (one+1)
    elif dot < one:
        adjust = dot - one

    return (nExp + adjust) + 127, one

def getMantissa(sNum, one):
    temp = []
    ctr = one+1 # will only get the strings after the 1st occurence of 1
    fractional = 23
    while ctr < len(sNum):
        if ctr < len(sNum):
            temp.append(sNum[ctr])
        if ctr == len(sNum)-1:
            break
        ctr += 1

    temp.remove('.')
    ctr = len(temp)
    while ctr < fractional:
        temp.append('0')
        if ctr == fractional-1:
            break
        ctr += 1

    # converts list to string
    convertedList = map(str, temp) 
    sNum = ''.join(convertedList)
    return sNum

def joinValues(sign, exponent, mantissa):
    temp = []
    s = str(sign)
    e = str(bin(exponent)[2:])
    m = mantissa
    
    temp.append(s)
    temp.append(e)
    temp.append(m)
    
    # converts list to string
    convertedList = map(str, temp) 
    answer = ''.join(convertedList)
    return answer

# https://www.geeksforgeeks.org/python-program-to-convert-binary-to-hexadecimal/
def binToHex(n): # binary to hex kinuha ko lang yung codeHAHAH
    bnum = int(n)
    temp = 0
    mul = 1
    list = []
     
    count = 1
     
    hexaDeciNum = ['0'] * 100

    i = 0
    while bnum != 0:
        rem = bnum % 10
        temp = temp + (rem*mul)

        if count % 4 == 0:

            if temp < 10:
                hexaDeciNum[i] = chr(temp+48)
            else:
                hexaDeciNum[i] = chr(temp+55)
            mul = 1
            temp = 0
            count = 1
            i = i+1
             
        else:
            mul = mul*2
            count = count+1
        bnum = int(bnum/10)
         
    if count != 1:
        hexaDeciNum[i] = chr(temp+48)
         
    if count == 1:
        i = i-1
         
    while i >= 0:
        list.append(hexaDeciNum[i])
        i = i-1

    convertedList = map(str, list) 
    hex = ''.join(convertedList)
    return hex

if __name__ == '__main__':
    print("\n--------------------------------------------------------")
    print("Welcome to IEEE-754 Binary-32 floating point converter!")
    print("----------------------------------------------------------")

    while True:
        while True:
            print("Enter base (2 or 10)")
            nBase = int(input("-> "))
            if nBase == 2 or nBase == 10:
                break

        while True:
            print("Enter sign (0 or 1)")
            nSign = int(input("-> "))
            if nSign == 0 or nSign == 1:
                break

        while True:
            print("Enter number+decimal (ex 1000.00011)")
            sNum = str(input("-> "))  

            if nBase == 2 and checkBinary(sNum) and checkFormat(sNum):
                break
            if nBase == 10 and checkFormat(sNum):
                break
        
        print("Enter exponent")
        nExp = int(input())
        break

    # processed values
    exponent, one = getExponent(sNum, nExp)
    mantissa = getMantissa(sNum, one)
    answer = joinValues(nSign, exponent, mantissa)
    hex = binToHex(answer)

    print("\n--------------------------------")
    print("These are your inputs\n")
    print("Base: "), nBase
    print("Sign: ", nSign)
    print("Number: ", sNum)
    print("Exponent", nExp)
    print("--------------------------------")
    print("Sign: ", nSign)
    print("Exponent:")
    print("Decimal: ", exponent)
    print("Binary: ", bin(exponent)[2:], " (", exponent, ")") # bin() converts to binary
    print("Fraction", mantissa)
    print("--------------------------------")
    print("Answer in bin: ", answer)
    print("Answer in hex: ", hex)

    # print(bin(.75)) binary function only accepts integers








