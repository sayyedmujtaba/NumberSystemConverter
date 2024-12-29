class Hexadecimal:
    def __init__(self, hexadecimal_number):
        self.hexadecimal_number = hexadecimal_number

    def to_binary(self):
        binary_number = ""
        hexa_to_binary = { "0": "0000", "1": "0001", "2": "0010", "3": "0011", "4": "0100", "5": "0101", "6": "0110", "7": "0111", "8": "1000", "9": "1001", "A": "1010", "B": "1011", "C": "1100", "D": "1101", "E": "1110", "F": "1111", "a": "1010", "b": "1011", "c": "1100", "d": "1101", "e": "1110", "f": "1111"}
        for digit in self.hexadecimal_number:
            binary_number += hexa_to_binary[digit]
        return binary_number

    def to_decimal(self):
        len_hexa = len(self.hexadecimal_number)
        decimal = 0
        for index, digit in enumerate(self.hexadecimal_number):
            power = (len_hexa) - index - 1
            decimal += int(digit) * 16 ** power
        return decimal

    def to_octal(self):
        binary = self.to_binary()
        binary = binary.zfill((len(binary) + 2) // 3 * 3)
        binary_to_octal = {"000": "0", "001": "1", "010": "2", "011": "3","100": "4", "101": "5", "110": "6",  "111": "7"}
        octal_number = ""
        for i in range(0, len(binary), 3):
            chunk = binary[i:i+3]
            octal_number += binary_to_octal[chunk]
        return octal_number
        pass

    def print_conversions(self):
        print("Binary:", self.to_binary())
        print("Decimal:", self.to_decimal())
        print("Octal:", self.to_octal())


hexa_decimal_input = input("Enter a decimal number: ")
hexa_decimal_number = Hexadecimal(hexa_decimal_input)
hexa_decimal_number.print_conversions()

