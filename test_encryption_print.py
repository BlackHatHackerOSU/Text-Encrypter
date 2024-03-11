from encryption import myEncryption

class SecureMessageHandler:
    def __init__(self, passphrase):
        self.initialPassphrase = passphrase
        self.crypt = myEncryption(passphrase)

    def verifyPassphrase(self, prompt):
        passphrase = input(prompt)
        return passphrase == self.initialPassphrase

    def encryptMessage(self, plaintext):
        if not self.verifyPassphrase("\nEnter your passphrase for encryption: "):
            print("\nThe entered passphrase does not match the initialized passphrase. Encryption aborted.")
            return None
        return self.crypt.encrypt(plaintext)

    def decryptMessage(self, encryptedText):
        if not self.verifyPassphrase("\nEnter your passphrase for decryption: "):
            print("\nThe entered passphrase does not match the initialized passphrase. Decryption aborted.")
            return None
        return self.crypt.decrypt(encryptedText)

def main():
    initialPassphrase = input("\nInitialize your passphrase: ")
    handler = SecureMessageHandler(initialPassphrase)

    plaintext = input("\nWhat is your secret message?: ")
    encryptedText = handler.encryptMessage(plaintext)

    if encryptedText:
        print("\nEncrypted Text: ", encryptedText)
        print("\nEncrypted Text (Hex):", encryptedText.hex())

        decryptedText = handler.decryptMessage(encryptedText)
        if decryptedText:
            print("\nDecrypted Text: ", decryptedText, "\n")
        else:
            print("\n** Decryption failed or was aborted. **\n")
    else:
        print("\n** Encryption failed or was aborted.** \n")

if __name__ == "__main__":
    main()
