class UPCValidator:
    """Validates UPCs by comparing comparing check digits."""
    
    def __init__(self, upc_string: str):
        self.upc = upc_string
        self.chars = list(self.upc[0:11])

    def print_info(self):
        print(f"The first 11 digits are {''.join(self.chars)}")
        print(f"The provided check digit is {self.upc[11]}")
        print("Calculating...")

    def find_expected_check_digit(self) -> int:
        odd = (int(self.chars[0]) + int(self.chars[2]) + int(self.chars[4]) + int(self.chars[6]) + int(self.chars[8]) + int(self.chars[10]))
        product = odd * 3
        result = (product + int(self.chars[1]) + int(self.chars[3]) + int(self.chars[5]) + int(self.chars[7]) + int(self.chars[9]))
        m = result % 10
        if m == 0:
            return 0
        else: return 10 - m

    def validate(self):
        self.print_info()
        expected = self.find_expected_check_digit()
        print(f"The expected check digit is {expected}")
        if int(self.upc[11]) == expected:
            print("This is a VALID UPC.")
        else:
            print("This is an INVALID UPC.")

if __name__ == "__main__":
    user_input = str(input("Enter a 12-digit UPC:  "))
    validator = UPCValidator(user_input)
    validator.validate()