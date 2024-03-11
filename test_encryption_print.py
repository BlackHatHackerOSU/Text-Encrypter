import pytest
from encryption import myEncryption 

def main():
    # Define a passphrase for the encryption key
    passphrase = "your_secure_passphrase"
    
    # Initialize your encryption class with the passphrase
    crypt = myEncryption(passphrase)
    
    # Define the plaintext message you want to encrypt
    plaintext = "This is a secret message."
    
    # Print the unencrypted text
    print("Unencrypted: ", plaintext)
    
    # Encrypt the plaintext
    encryptedText = crypt.encrypt(plaintext)
    
    # Print the encrypted text
    print("Encrypted Text: ", encryptedText)

    # Decode to readable format
    print("Encrypted Text (Hex):", encryptedText.hex())

    # Decrypt the text
    decryptedText = crypt.decrypt(encryptedText)

    # Print the decrypted text
    print("Decrypted Text: ", decryptedText)


if __name__ == "__main__":
    main()