class Binary:
    def __init__(self, binary_number):
        self.binary_number = binary_number

    def to_decimal(self):
        len_bin = len(self.binary_number)
        decimal = 0
        for index, digit in enumerate(self.binary_number):
            power = (len_bin) - index - 1
            decimal += int(digit) * 2 ** power
        return decimal
    
    def to_octal(self):
        if len(self.binary_number) % 3 == 1:
            self.binary_number = "00" + self.binary_number
        elif len(self.binary_number) % 3 == 2:
            self.binary_number = "0" + self.binary_number
        binary_to_octal = {"000": "0", "001": "1", "010": "2", "011": "3","100": "4", "101": "5", "110": "6",  "111": "7"}
        octal_number = ""  
        for i in range(0, len(self.binary_number), 3): 
            chunk = self.binary_number[i:i+3]  
            octal_number += binary_to_octal[chunk]
        return octal_number

    def to_hexadecimal(self):
        if len(self.binary_number) % 4 == 3:
            self.binary_number = "0" + self.binary_number
        elif len(self.binary_number) % 4 == 2:
            self.binary_number = "00" + self.binary_number
        elif len(self.binary_number) % 4 == 1:
            self.binary_number = "000" + self.binary_number
        binary_to_hexadecimal={'0000': '0', '0001': '1', '0010': '2', '0011': '3', '0100': '4', '0101':'5',    '0110': '6', '0111': '7', '1000': '8', '1001': '9', '1010': 'A', '1011': 'B', '1100': 'C','1101':     'D', '1110': 'E', '1111': 'F'}
        hexa_decimal_number = ""
        for i in range(0, len(self.binary_number), 4): 
            chunk = self.binary_number[i:i+4]  
            hexa_decimal_number+=binary_to_hexadecimal[chunk]
        return hexa_decimal_number.lstrip("0")

    def print_conversion(self):
        print("Decimal:", self.to_decimal())
        print("Octal:", self.to_octal())
        print("Hexadecimal:", self.to_hexadecimal())

# while True:
#     binary_input = input("Enter binary number: ")
#     if all(char in '01' for char in binary_input):
#         break
#     print("Invalid input. Please enter a binary number containing only 0 and 1.")

# binary_number = Binary(binary_input)
# binary_number.print_conversion()
