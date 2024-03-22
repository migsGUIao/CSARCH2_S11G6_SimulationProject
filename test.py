#CURRENT ERROR MESSAGE FOR TEST CASE 3#
# Exception in Tkinter callback
# Traceback (most recent call last):
#   File "D:\IDE\Python\Lib\tkinter\__init__.py", line 1967, in __call__
#     return self.func(*args)
#            ^^^^^^^^^^^^^^^^
#   File "d:\College\Term 2 2023-2024\CSARCH2\CSARCH2_S11G6_SimulationProject\binary_floating32.py", line 270, in convert
#     mantissa = getMantissa(sNum, one)
#                ^^^^^^^^^^^^^^^^^^^^^^
#   File "d:\College\Term 2 2023-2024\CSARCH2\CSARCH2_S11G6_SimulationProject\binary_floating32.py", line 73, in getMantissa
#     temp.remove('.')
# ValueError: list.remove(x): x not in list

# PLACED HERE TEMPORARILY
# if __name__ == '__main__':
#     print("\n--------------------------------------------------------")
#     print("Welcome to IEEE-754 Binary-32 floating point converter!")
#     print("----------------------------------------------------------")

#     while True:
#         while True:
#             print("Enter base (2 or 10)")
#             nBase = int(input("-> "))
#             if nBase == 2 or nBase == 10:
#                 break

#         while True:
#             print("Enter sign (0 or 1)")
#             nSign = int(input("-> "))
#             if nSign == 0 or nSign == 1:
#                 break

#         while True:
#             print("Enter number+decimal (ex 1000.00011)")
#             sNum = str(input("-> "))  

#             if nBase == 2 and checkBinary(sNum) and checkFormat(sNum):
#                 break
#             if nBase == 10 and checkFormat(sNum):
#                 break
        
#         print("Enter exponent")
#         nExp = int(input())
#         break

#     # processed values
#     exponent, one = getExponent(sNum, nExp)
#     mantissa = getMantissa(sNum, one)
#     answer = joinValues(nSign, exponent, mantissa)
#     hex = binToHex(answer)

#     print("\n--------------------------------")
#     print("These are your inputs\n")
#     print("Base: "), nBase
#     print("Sign: ", nSign)
#     print("Number: ", sNum)
#     print("Exponent", nExp)
#     print("--------------------------------")
#     print("Sign: ", nSign)
#     print("Exponent:")
#     print("Decimal: ", exponent)
#     print("Binary: ", bin(exponent)[2:], " (", exponent, ")") # bin() converts to binary
#     print("Fraction", mantissa)
#     print("--------------------------------")
#     print("Answer in bin: ", answer)
#     print("Answer in hex: ", hex)

    # print(bin(.75)) binary function only accepts integers