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

#Checks for number of decimal points and adds either a .0 or 0 if absent in input significand
def checkFormat(sNum):
    #If input has more than 1 decimal, invalidate
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

#Checks if significand is in binary
def checkBinary(sNum):
    ctr = 0
    while ctr < len(sNum):
        if sNum[ctr] != '0' and sNum[ctr] != '1' and sNum[ctr] != '.':
            return False
        ctr += 1

    return True

#Computes for exponent field
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

#Computes for mantissa field
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

#Combines fields together for final answer
def joinValues(sign, exponent, mantissa):
    temp = []
    s = str(sign)
    e = str(bin(exponent)[2:]).rjust(8, '0') #if exponent in binary is not 8-bit, it is zero-extended
    m = mantissa
    temp.append(s)
    temp.append(e)
    temp.append(m)
    
    # converts list to string
    convertedList = map(str, temp) 
    answer = ''.join(convertedList)

    return answer, s, e, m

#Converts decimal significand to binary
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

#Converts final answer to hex
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

def okSign(nSign):
        if nSign == 0 or nSign == 1:
            return True
        else:
            return False
    
#COMMENTED CODE CHUNK TEMPORARILY MOVED TO test.py
        
class IEEE754ConverterGUI(tk.Tk):
    #Creates GUI + input
    def __init__(self):
        super().__init__()
        self.title("IEEE-754 Binary-32 Floating Point Converter")
        self.geometry("400x400")
        
        # Inputs
        tk.Label(self, text="Base (2 for Binary or 10 for Decimal):").pack()
        self.base_entry = tk.Entry(self)
        self.base_entry.pack()

        tk.Label(self, text="Sign (0 for Positive or 1 for Negative):").pack()
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
        #Assigns inputs to variables
        nBase = self.base_entry.get()
        nSign = self.sign_entry.get()
        sNum = self.num_entry.get()
        nExp = self.exp_entry.get()

        #Checks significand for decimal format
        okFormat, sNum = checkFormat(sNum)

        #Error check for empty input fields
        if not nBase or not nSign or not sNum or not nExp:
            messagebox.showerror("Error", "Please fill in all the fields.")
            return

        # Convert inputs to integers
        try:
            nBase = int(nBase)
            nSign = int(nSign)
            nExp = int(nExp)

        except ValueError:
            messagebox.showerror("Error", "Invalid input for base, sign, or exponent.")
            return
        
        #Gets decimal form of computed exponent & computed mantissa
        if sNum != '0.0':
            exponent, one = getExponent(sNum, nExp)
            mantissa = getMantissa(sNum, one)
        
        # infinity
        if nExp >= 127: 
            exponent = 255
            mantissa = "00000000000000000000000"
        # denormalized
        elif nExp < -126 and mantissa != "00000000000000000000000": 
            exponent = 00000000
        # zero
        elif sNum == 0.0: 
            exponent = 00000000
            mantissa = "00000000000000000000000"
        # NaN (sNaN? & qNaN?)
        
        if nBase == 2 and checkBinary(sNum) and okFormat and okSign(nSign):
            pass
        elif nBase == 10 and okFormat and okSign(nSign):
            sNum = decToBin(sNum)
        else:
            if nBase != 2 or nBase != 10:
                messagebox.showerror("Error", "Invalid input.\nInput 2 for the input to be read as Binary \nInput 10 for the input to be read as Decimal")
                return
            elif nSign != 0 or nSign != 1:
                messagebox.showerror("Error", "Invalid input.\nInput 0 for the input to be read as Positive \nInput 1 for the input to be read as Negative")
                return
            else:    
                messagebox.showerror("Error", "Invalid input.")
                return

        answer, fSign, fExp, fMant = joinValues(nSign, exponent, mantissa)
        hex = binToHex(answer)
        self.show_result(fSign, exponent, fExp, fMant, hex)
        #self.show_result(nSign, exponent, mantissa, hex)

    #Outputs results
    def show_result(self, fSign, exponent, fExp, fMant, hex):
        self.output_text.delete(1.0, "end")
        self.output_text.insert("end", f"Sign: {fSign}\n")
        self.output_text.insert("end", f"Exponent (Decimal): {exponent}\n")
        #self.output_text.insert("end", f"Exponent (Binary): {bin(exponent)[2:]}\n")
        self.output_text.insert("end", f"Exponent (Binary): {fExp}\n")
        self.output_text.insert("end", f"Mantissa: {fMant}\n")
        #self.output_text.insert("end", f"Binary: {sign} | {bin(exponent)[2:]} | {mantissa}\n")
        self.output_text.insert("end", f"Binary: {fSign} | {fExp} | {fMant}\n")
        self.output_text.insert("end", f"Hexdecimal: {hex}\n")

    #Saves output to a text file
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