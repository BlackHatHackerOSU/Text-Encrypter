This project provides a Python implementation for a basic encryption and decryption system, named myEncryption. It uses a simplified version of block cipher encryption, leveraging SHA-256 for key derivation and a basic XOR operation for encrypting blocks of data. This implementation is not recommended for production use but serves as an educational tool for understanding encryption basics.


# Project Structure:
- encryption.py: The core module that implements the myEncryption class. It provides functionality for key derivation, encryption, and decryption.
- test_encryption.py: A test module using pytest to verify the encryption and decryption logic.
- test_encryption_print.py: An interactive test script to demonstrate encryption and decryption flows with user input.
- LICENSE: The license file containing the terms under which the software is distributed.

# Installation

**Open your terminal and run the following commands** 

git clone <git clone https://github.com/BlackHatHackerOSU/Text-Encrypter.git>
cd Text-Encrypter

**Ensure Python is Installed**
python --version
or
python3 --version

# Usage

## To run the interactive test script:
**execute:**
python test_encryption_print.py

## To run automated tests:
**ensure pytest is installed:**
pip install pytest

**then execute the test script:**
pytest test_encryption.py

# License
This project is licensed under the MIT License - see the LICENSE file for details.
