# Caesar Cipher 🔒

![Python Version](https://img.shields.io/badge/python-3.8%2B-blue)
![License](https://img.shields.io/badge/license-MIT-green)

A Python implementation of the classic Caesar Cipher for basic text encryption and decryption.

## 📜 About
The Caesar Cipher is one of the simplest and most widely-known encryption techniques. It works by shifting each letter in the plaintext by a fixed number of positions in the alphabet. This implementation provides a foundation for understanding basic cryptographic concepts.

## ✨ Features
- Encrypt and decrypt text using a shift-based cipher
- Handles both uppercase and lowercase letters
- Preserves non-alphabetic characters
- Simple command-line interface
- Automatic shift normalization for values over 26

## 🚀 Quick Start

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/fahadelahikhan/Caesar-Cipher.git
   cd Caesar-Cipher
   ```

2. Run the application:
   ```bash
   python Caesar-Cipher.py
   ```

### Basic Usage
```python
# Import the caesar function
from caesar_cipher import caesar

# Encrypt a message
encrypted = caesar(start_text="hello", shift_amount=3, cipher_direction="encode")
# Output: Your encoded text is: khoor

# Decrypt a message
decrypted = caesar(start_text="khoor", shift_amount=3, cipher_direction="decode")
# Output: Your decoded text is: hello
```

### Example Encryption
```python
# Encrypt a secret message
message = "meet me after class"
shift = 5
encrypted_message = caesar(message, shift, "encode")
print(encrypted_message)  # Output: rjjy rj fiyhw hqfxx

# Decrypt the message
decrypted_message = caesar(encrypted_message, shift, "decode")
print(decrypted_message)  # Output: meet me after class
```

## 📖 How It Works
The Caesar Cipher works by:
1. Taking each letter in the plaintext
2. Shifting it by a specified number of positions in the alphabet
3. Wrapping around using modulo 26 arithmetic
4. Non-alphabetic characters are left unchanged

The encryption formula can be represented as:
```
E(x) = (x + n) mod 26
```
Where `x` is the position of the letter in the alphabet and `n` is the shift amount.

## ⚖️ License
Distributed under the MIT License. See [LICENSE](LICENSE) for details.

---

> **Note**: The Caesar Cipher is not secure for modern cryptographic needs. Use this implementation for educational purposes only.
