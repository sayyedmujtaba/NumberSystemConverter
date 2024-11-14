class Decimal:
    def __init__(self, decimal_number):
        self.decimal_number = decimal_number

    def to_binary(self):
        binary = ""
        number = self.decimal_number  # Use a temporary variable to avoid changing the original decimal number
        if number == 0:
            return "0"
        while number > 0:
            remain = number % 2
            binary = str(remain) + binary
            number //= 2  # Update by integer division
        return binary
    
    def to_octal(self):
        octal = ""
        number = self.decimal_number  # Use a temporary variable to avoid changing the original decimal number
        if number == 0:
            return "0"
        while number > 0:
            remain = number % 8
            octal = str(remain) + octal
            number //= 8  # Update by integer division
        return octal
    
    def to_hexa_decimal(self):
        hexa_decimal = ""
        number = self.decimal_number  # Use a temporary variable to avoid changing the original decimal number
        if number == 0:
            return "0"
        hex_map = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        while number > 0:
            remain = number % 16
            if remain > 9:
                hexa_decimal = hex_map[remain] + hexa_decimal
            else:
                hexa_decimal = str(remain) + hexa_decimal
            number //= 16  # Update by integer division
        return hexa_decimal

decimal_number = Decimal(12)
print(decimal_number.to_binary())
print(decimal_number.to_octal())
print(decimal_number.to_hexa_decimal())