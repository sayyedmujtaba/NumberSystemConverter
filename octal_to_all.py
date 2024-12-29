class Octal:
    def __init__(self, octal_number):
        self.octal_number = octal_number

    def to_binary(self):
        octal_to_binary = {'0': '000', '1': '001', '2': '010', '3': '011', '4': '100', '5': '101', '6': '110', '7': '111'}
        binary_number=""
        for digit in self.octal_number:
            binary_number += octal_to_binary[digit]
        return binary_number

    def to_decimal(self):
        len_bin = len(self.octal_number)
        decimal = 0
        for index, digit in enumerate(self.octal_number):
            power = (len_bin) - index - 1
            decimal += int(digit) * 8 ** power
        return decimal
    
    def to_hexa_decimal(self):
        binary = self.to_binary()
        binary = binary.zfill((len(binary) + 3) // 4 * 4)
        binary_to_hexa = {
            "0000": "0", "0001": "1", "0010": "2", "0011": "3",
            "0100": "4", "0101": "5", "0110": "6", "0111": "7",
            "1000": "8", "1001": "9", "1010": "A", "1011": "B",
            "1100": "C", "1101": "D", "1110": "E", "1111": "F"
        }
        hexa_decimal = ""
        for i in range(0, len(binary), 4):
            hexa_decimal += binary_to_hexa[binary[i:i+4]]
        return hexa_decimal

   
    def print_conversion(self):
        print("Binary:", self.to_binary())
        print("Decimal:", self.to_decimal())
        print("Hexadecimal:", self.to_hexa_decimal())

while True:
    octal_input = input("Enter an Octal number: ")
    if all(char in '01234567' for char in octal_input):
        break
    print("Invalid input. Please enter numbers between 0 and 7.")

octal_number = Octal(octal_input)
octal_number.print_conversion()