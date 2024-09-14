class CaesarCipher:
    """
    A class to perform Caesar cipher encryption and decryption.
    """

    def __init__(self):
        self.key = self.reveal_key()

    def encrypt(self, text, key=None):
        """
        Encrypts the given text using the Caesar cipher with the provided key.

        Args:
            text (str): The plaintext to encrypt.
            key (int, optional): The encryption key. If None, uses the revealed key.

        Returns:
            str: The encrypted text.
        """
        if key is None:
            key = self.key
        encrypted_text = ""
        for char in text:
            if char.isalpha():
                shifted = ord(char) + key
                if char.islower():
                    if shifted > ord("z"):
                        shifted -= 26
                    elif shifted < ord("a"):
                        shifted += 26
                elif char.isupper():
                    if shifted > ord("Z"):
                        shifted -= 26
                    elif shifted < ord("A"):
                        shifted += 26
                encrypted_text += chr(shifted)
            else:
                encrypted_text += char
        return encrypted_text

    def decrypt(self, text, key=None):
        """
        Decrypts the given text using the Caesar cipher with the provided key.

        Args:
            text (str): The ciphertext to decrypt.
            key (int, optional): The decryption key. If None, uses the revealed key.

        Returns:
            str: The decrypted text.
        """
        if key is None:
            key = self.key
        return self.encrypt(text, -key)

    def reveal_key(self):
        """
        Reveals the encryption/decryption key based on the provided algorithm.

        Returns:
            int: The revealed key.
        """
        total = 0
        for i in range(5):
            for j in range(3):
                if i + j == 5:
                    total += i + j
                else:
                    total -= i - j

        counter = 0
        while counter < 5:
            if total < 13:
                total += 1
            elif total > 13:
                total -= 1
            else:
                counter += 2

        return total

    def find_key(self, ciphertext):
        """
        Tries all possible keys to decrypt the ciphertext and prints each result.

        Args:
            ciphertext (str): The encrypted text to decrypt.
        """
        for shift in range(1, 26):
            decrypted_text = self.decrypt(ciphertext, key=shift)
            print(f"Key {shift}: {decrypted_text}")
