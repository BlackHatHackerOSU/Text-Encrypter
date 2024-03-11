import pytest
from encryption import myEncryption 

def test_advanced_crypt_encryption_and_decryption():
    passphrase = "secure_passphrase"
    plaintext = "This is a secret message."

    crypt = myEncryption(passphrase)
    
    # Encrypt the plaintext
    ciphertext = crypt.encrypt(plaintext)
    
    # Ensure ciphertext is not the same as plaintext
    assert ciphertext != plaintext.encode()
    
    # Decrypt the ciphertext
    decrypted_text = crypt.decrypt(ciphertext)
    
    # Verify decrypted text matches the original plaintext
    assert decrypted_text == plaintext

    # Additional test to ensure encrypting the same message twice results in different ciphertexts
    ciphertext2 = crypt.encrypt(plaintext)
    assert ciphertext != ciphertext2, "Ciphertexts are identical, IV might not be working properly."

# If running this file directly, invoke pytest
if __name__ == "__main__":
    pytest.main()
