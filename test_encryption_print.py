import pytest
from encryption import myEncryption 

def main():
    # Define a passphrase for the encryption key
    passphrase = "Super_Secret_Passcode"
    
    # Initialize your encryption class with the passphrase
    crypt = myEncryption(passphrase)
    
    # Define the plaintext message you want to encrypt
    plaintext = input("What is your secret message?: ")

    print("\n")
    
    # Print the unencrypted text
    print("Unencrypted: ", plaintext)

    print("\n")
    
    # Encrypt the plaintext
    encryptedText = crypt.encrypt(plaintext)
    
    # Print the encrypted text
    print("Encrypted Text: ", encryptedText)

    print("\n")

    # Decode to readable format
    print("Encrypted Text (Hex):", encryptedText.hex())

    print("\n")

    # Decrypt the text
    decryptedText = crypt.decrypt(encryptedText)

    # Print the decrypted text
    print("Decrypted Text: ", decryptedText)

    print("\n")

if __name__ == "__main__":
    main()