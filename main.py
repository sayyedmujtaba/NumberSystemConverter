from binary_to_all import Binary
from decimal_to_all import Decimal
from hexadecimal_to_all import Hexadecimal
from octal_to_all import Octal


def main_menu():

    print("==================================================================================")
    print("Welcome to Mujtab's Numbers conversion Calculator.\n")
    print("Choose an option from the below menu to convert a number to desired category.\n")
    print("Select 1 to convert a number from Binary to others.\n")
    print("Select 2 to convert a number form Decimal to others.\n")
    print("Select 3 to convert a number from Octal to others.\n")
    print("Select 4 to convert Hexadecimal to others.\n")
    print("Select 5 to exit.\n")
    print("==================================================================================")

def main():
    main_menu()

    try:

        while True:
            
            choice = int(input("Enter a number of your choice: "))

            if choice == 1:

                while True:
                    binary_input = input("Enter binary number: ")
                    if all(char in '01' for char in binary_input):
                        break
                    print("Invalid input. Please enter a binary number containing only 0 and 1.")
                binary_number = Binary(binary_input)
                binary_number.print_conversion()

                print("=================================================================")

            
            elif choice == 2:

                decimal_input = input("Enter a decimal number: ")
                decimal_number = Decimal(decimal_input)
                decimal_number.print_conversions()

                print("=================================================================")

            elif choice == 3:

                while True:
                    octal_input = input("Enter an Octal number: ")
                    if all(char in '01234567' for char in octal_input):
                        break
                    print("Invalid input. Please enter numbers between 0 and 7.")
                
                octal_number = Octal(octal_input)
                octal_number.print_conversion()

                print("=================================================================")

            elif choice == 4:

                hexa_decimal_input = input("Enter a hexa_decimal number: ")
                hexa_decimal_number = Hexadecimal(hexa_decimal_input)
                hexa_decimal_number.print_conversions()

                print("=================================================================")

            elif choice == 5:

                print("Goodbye")
                print("=================================================================")
                exit()

            else:
                print("Give number from the given menu")


    except:
        print("Enter an Integer from the given menu.")



if __name__ == "__main__":
    main()