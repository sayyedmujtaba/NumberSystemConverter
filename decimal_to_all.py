class Decimal:
    def __init__(self, decimal_number):
        # Error handling for invalid input types
        try:
            # Attempt to convert the input to an integer
            self.decimal_number = int(decimal_number)
            if self.decimal_number < 0:
                raise ValueError("Only positive integers are allowed.")
        except ValueError as ve:
            print(f"Error: {ve}")
            self.decimal_number = None  # Set to None if input is invalid
        except Exception as e:
            print(f"Unexpected error: {e}")
            self.decimal_number = None

    def to_binary(self):
        if self.decimal_number is None:
            return "Invalid decimal number"
        
        binary = ""
        number = self.decimal_number
        if number == 0:
            return "0"
        while number > 0:
            remain = number % 2
            binary = str(remain) + binary
            number //= 2
        return binary
    
    def to_octal(self):
        if self.decimal_number is None:
            return "Invalid decimal number"
        
        octal = ""
        number = self.decimal_number
        if number == 0:
            return "0"
        while number > 0:
            remain = number % 8
            octal = str(remain) + octal
            number //= 8
        return octal
    
    def to_hexa_decimal(self):
        if self.decimal_number is None:
            return "Invalid decimal number"
        
        hexa_decimal = ""
        number = self.decimal_number
        if number == 0:
            return "0"
        hex_map = {10: "A", 11: "B", 12: "C", 13: "D", 14: "E", 15: "F"}
        while number > 0:
            remain = number % 16
            if remain > 9:
                hexa_decimal = hex_map[remain] + hexa_decimal
            else:
                hexa_decimal = str(remain) + hexa_decimal
            number //= 16
        return hexa_decimal

    def print_conversions(self):
        if self.decimal_number is None:
            print("Cannot perform conversions due to invalid input.")
            return
        print("Binary:", self.to_binary())
        print("Octal:", self.to_octal())
        print("Hexadecimal:", self.to_hexa_decimal())

# # Usage
# decimal_input = input("Enter a decimal number: ")
# decimal_number = Decimal(decimal_input)
# decimal_number.print_conversions()
