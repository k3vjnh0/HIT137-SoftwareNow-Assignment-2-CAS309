class StringCipherProcessor:
    """
    A class to process strings and decrypt Caesar ciphers.
    """

    def __init__(self, string=None, ciphertext=None):
        """
        Initialize the StringCipherProcessor instance.

        Args:
            s (str, optional): The string to process. Defaults to None.
            ciphertext (str, optional): The ciphertext to decrypt. Defaults to None.
        """
        self.string = string
        self.ciphertext = ciphertext

    def process_string(self):
        """
        Processes the provided string to extract numbers, letters, even numbers, uppercase letters,
        and their ASCII codes.
        """
        if self.string is None:
            print("No string provided for processing.")
            return

        number_string = []
        letter_string = []
        even_numbers = []
        even_ascii_values = []
        uppercase_letters = []
        uppercase_ascii_values = []

        # Process the string
        for char in self.string:
            if char.isdigit():
                number_string.append(char)
                if int(char) % 2 == 0:
                    even_numbers.append(char)
                    even_ascii_values.append(ord(char))
            elif char.isalpha():
                letter_string.append(char)
                if char.isupper():
                    uppercase_letters.append(char)
                    uppercase_ascii_values.append(ord(char))

        # Join lists into strings for printing
        number_string_joined = "".join(number_string)
        letter_string_joined = "".join(letter_string)

        print(f"Number string: {number_string_joined}")
        print(f"Letter string: {letter_string_joined}")
        print(f"Even numbers: {', '.join(even_numbers)}")
        print(f"ASCII code of even numbers: {', '.join(map(str, even_ascii_values))}")
        print(f"Uppercase letters: {', '.join(uppercase_letters)}")
        print(
            f"ASCII code of uppercase letters: {', '.join(map(str, uppercase_ascii_values))}"
        )

    def caesar_decrypt(self, shift):
        """
        Decrypts the ciphertext using a Caesar cipher with the specified shift.

        Args:
            shift (int): The shift value for decryption.

        Returns:
            str: The decrypted text.
        """
        if self.ciphertext is None:
            print("No ciphertext provided for decryption.")
            return ""

        shift = shift % 26  # Normalize the shift to a range of 0-25

        def decrypt_char(char):
            if char.isalpha():
                base = ord("A") if char.isupper() else ord("a")
                return chr((ord(char) - base - shift) % 26 + base)
            return char

        decrypted_text = "".join(decrypt_char(char) for char in self.ciphertext)
        return decrypted_text

    def find_key(self):
        """
        Tries all possible shifts (1 to 25) to decrypt the ciphertext and prints the results.
        """
        if self.ciphertext is None:
            print("No ciphertext provided for decryption.")
            return

        for shift in range(1, 26):
            decrypted_text = self.caesar_decrypt(shift)
            print(f"Key {shift}: {decrypted_text}")
