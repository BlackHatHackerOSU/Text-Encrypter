import os
import hashlib 

class myEncryption:
    BLOCK_SIZE = 16  # Block size in bytes
    
    def __init__(self, passphrase):
        self.key = self.deriveKey(passphrase)
        
    def deriveKey(self, passphrase):
        # Simplified key derivation using SHA-256 and a static salt
        salt = b"this_is_not_a_secure_salt"
        return hashlib.pbkdf2_hmac('sha256', passphrase.encode(), salt, 100000, dklen=self.BLOCK_SIZE)
    
    def xorBytes(self, block_a, block_b):
        return bytes(a ^ b for a, b in zip(block_a, block_b))
    
    def encrypt(self, plaintext):
        iv = os.urandom(self.BLOCK_SIZE)  # Generate a random IV
        encryptedBlocks = [iv]
        previousBlock = iv
        
        # Padding plaintext to a multiple of BLOCK_SIZE
        paddingLength = self.BLOCK_SIZE - (len(plaintext) % self.BLOCK_SIZE)
        plaintext += chr(paddingLength) * paddingLength
        
        # Encrypt each block
        for i in range(0, len(plaintext), self.BLOCK_SIZE):
            block = plaintext[i:i+self.BLOCK_SIZE].encode()
            # Simulate block cipher by XORing the block with a pseudo-random block derived from the key and previous block
            pseudoRandomBlock = hashlib.sha256(previousBlock + self.key).digest()[:self.BLOCK_SIZE]
            encryptedBlock = self.xorBytes(block, pseudoRandomBlock)
            encryptedBlocks.append(encryptedBlock)
            previousBlock = encryptedBlock
            
        return b''.join(encryptedBlocks)
    
    def decrypt(self, ciphertext):
        iv = ciphertext[:self.BLOCK_SIZE]
        decryptedText = b''
        previousBlock = iv
        
        for i in range(self.BLOCK_SIZE, len(ciphertext), self.BLOCK_SIZE):
            encryptedBlock = ciphertext[i:i+self.BLOCK_SIZE]
            pseudoRandomBlock = hashlib.sha256(previousBlock + self.key).digest()[:self.BLOCK_SIZE]
            decryptedBlock = self.xorBytes(encryptedBlock, pseudoRandomBlock)
            decryptedText += decryptedBlock
            previousBlock = encryptedBlock
        
        # Remove padding
        paddingLength = decryptedText[-1]
        return decryptedText[:-paddingLength].decode()