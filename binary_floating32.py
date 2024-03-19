'''
    * IEEE-754 Binary-32 floating point converter (including all special cases)
    • Input: (1) binary mantissa and base-2 (i.e., 101.01x25) (2) Decimal and base-10 (i.e.
    65.0x103). Also should support special cases (i.e., NaN).
    • Output: (1) binary output with space between section (2) its hexadecimal equivalent (3)
    with option to output in text file.
'''
import tkinter as tk
from tkinter import filedialog, messagebox
from tkinter.scrolledtext import ScrolledText

def checkFormat(sNum):
    ctr = 0
    dot = 0
    while ctr < len(sNum):
        if sNum[ctr] == '.':
            dot += 1
        if dot > 1:
            return False, sNum
        ctr += 1

    # if user doesn't input decimal point,
    # add a .0 at the end
    if dot == 0:
        sNum = "".join([sNum, '.0'])

    # if the user inputs a decimal point 
    # without a number after it,
    # then add one 0
    elif dot == 1 and sNum.index('.') == len(sNum)-1:
        sNum = ''.join([sNum, '0'])

    return True, sNum

def checkBinary(sNum):
    ctr = 0
    while ctr < len(sNum):
        if sNum[ctr] != '0' and sNum[ctr] != '1' and sNum[ctr] != '.':
            return False
        ctr += 1

    return True

def getExponent(sNum, nExp):
    dot = sNum.index('.')
    ctr = 0
    while ctr < len(sNum):
        if sNum[ctr] == '1':
            one = ctr
            break
        ctr += 1
    
    if dot > one:
        adjust = dot - (one+1)
    elif dot < one:
        adjust = dot + one

    return (nExp + adjust) + 127, one

def getMantissa(sNum, one):
    temp = []
    ctr = one+1 # will only get the strings after the 1st occurence of 1
    fractional = 23
    while ctr < len(sNum):
        temp.append(sNum[ctr])
        ctr += 1

    temp.remove('.')
    ctr = len(temp)
    while ctr < fractional:
        temp.append('0')
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

def decToBin(sNum):
    # separate whole and fractional numbers
    dot = sNum.index('.')
    whole = sNum[:dot]
    fractional = sNum[dot+1:]

    # whole number converted to binary
    bWhole = bin(int(whole))[2:]
  
    # get number of decimal places
    dPlaces = str(len(fractional))
    dPlaces = ''.join(['.', dPlaces])
    dPlaces = ''.join([dPlaces, 'f'])

    # convert decimal fraction to binary fraction
    checker = int(fractional) 
    bConverted = []

    while True:
        # fractional part multiplied by 2
        ans = format((checker / 100) * 2, dPlaces)

        # answer converted to string for processing
        temp = str(ans)
        dot = temp.index('.')

        checker = int(temp[dot+1:])
        res = temp[:dot]
        bConverted.append(res)

        if checker == 0:
            break

    # append '.' at the end of whole number
    bWhole = ''.join([bWhole, '.'])

    # converts binary fractional list to string
    convertedList = map(str, bConverted) 
    bFractional = ''.join(convertedList)

    # assemble binary whole and fractional
    binary = ''.join([bWhole, bFractional])
    
    return binary

def binToHex(answer): 
    hexBits = []
    hexList = []
    hexFinal = []

    hexConversion = {
        "0000" : '0',
        "0001" : '1',
        "0010" : '2',
        "0011" : '3',
        "0100" : '4',
        "0101" : '5',
        "0110" : '6',
        "0111" : '7',
        "1000" : '8',
        "1001" : '9',
        "1010" : 'A',
        "1011" : 'B',
        "1100" : 'C',
        "1101" : 'D',
        "1110" : 'E',
        "1111" : 'F'
    }

    # split into 4s
    slice = 1
    ctr = 0
    while ctr < len(answer):

        hexBits.append(answer[ctr])

        if slice == 4:
            hexList.append(hexBits[:4])
            del hexBits[0:4]
            slice = 0

        slice += 1
        ctr += 1

    # convert list to string
    # convert string to hex using hexConversion dictionary
    ctr = 0
    while ctr < len(answer) / 4:
        convertedList = map(str, hexList[ctr]) 
        sBinary = ''.join(convertedList)
        hexFinal.append(hexConversion[sBinary])
        ctr += 1

    # convert hexFinal list to string
    convertedList = map(str, hexFinal) 
    hex = ''.join(convertedList)

    return hex

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
    
class IEEE754ConverterGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("IEEE-754 Binary-32 Floating Point Converter")
        self.geometry("400x400")
        
        # Inputs
        tk.Label(self, text="Base (2 or 10):").pack()
        self.base_entry = tk.Entry(self)
        self.base_entry.pack()

        tk.Label(self, text="Sign (0 or 1):").pack()
        self.sign_entry = tk.Entry(self)
        self.sign_entry.pack()

        tk.Label(self, text="Number with decimal (e.g., 1000.00011):").pack()
        self.num_entry = tk.Entry(self)
        self.num_entry.pack()

        tk.Label(self, text="Exponent:").pack()
        self.exp_entry = tk.Entry(self)
        self.exp_entry.pack()

        # Buttons for converting and saving result to txt file
        tk.Button(self, text="Convert", command=self.convert).pack()
        tk.Button(self, text="Save Result", command=self.save_result).pack()

        # Outputs
        tk.Label(self, text="Output:").pack()
        self.output_text = ScrolledText(self, height=7)
        self.output_text.pack()

    def convert(self):
        nBase = int(self.base_entry.get())
        nSign = int(self.sign_entry.get())
        sNum = self.num_entry.get()
        nExp = int(self.exp_entry.get())
        okFormat, sNum = checkFormat(sNum)

        if nBase == 2 and checkBinary(sNum) and okFormat:
            pass
        elif nBase == 10 and okFormat:
            sNum = decToBin(sNum)
        else:
            messagebox.showerror("Error", "Invalid input.")
            return


        if sNum != '0.0':
            exponent, one = getExponent(sNum, nExp)
            mantissa = getMantissa(sNum, one)

        # infinity
        if nExp >= 127:
            exponent = 11111111
            mantissa = "00000000000000000000000"
        
        # denormalized
        elif nExp < -126 and mantissa != "00000000000000000000000":
            exponent = 00000000

        # zero
        elif sNum == '0.0':
            exponent = 00000000
            mantissa = "00000000000000000000000"

        # sNaN?
        # qNaN?
        
        answer = joinValues(nSign, exponent, mantissa)
        hex = binToHex(answer)

        self.show_result(nSign, exponent, mantissa, answer, hex)

    def show_result(self, sign, exponent, mantissa, binary, hex):
        self.output_text.delete(1.0, "end")
        self.output_text.insert("end", f"Sign: {sign}\n")
        self.output_text.insert("end", f"Exponent (Decimal): {exponent}\n")
        self.output_text.insert("end", f"Exponent (Binary): {bin(exponent)[2:]}\n")
        self.output_text.insert("end", f"Mantissa: {mantissa}\n")
        self.output_text.insert("end", f"Binary: {binary}\n")
        self.output_text.insert("end", f"Hexdecimal: {hex}\n")

    def save_result(self):
        result = self.output_text.get(1.0, "end").strip()
        if not result:
            messagebox.showwarning("Warning", "No result to save.")
            return
        
        file_path = filedialog.asksaveasfilename(defaultextension=".txt", filetypes=[("Text files", "*.txt")])
        if file_path:
            with open(file_path, "w") as file:
                file.write(result)
                messagebox.showinfo("Success", "Result saved successfully.")

if __name__ == '__main__':
    app = IEEE754ConverterGUI()
    app.mainloop()