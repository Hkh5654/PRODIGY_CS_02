# PRODIGY_CS_02

Image Encryption and Decryption Script

This script allows users to encrypt and decrypt images using a simple XOR-based encryption technique. It alters the RGB values of each pixel in the image by applying an XOR operation with a user-specified key. This method ensures that the image can only be properly decrypted using the same key that was used for encryption.

How It Works:

Encryption:

The script reads each pixel’s RGB values (red, green, and blue) from the image.

It then applies an XOR operation between each color component and the given encryption key (an integer between 0 and 255).

The modified pixels are saved in a new image file.

Decryption:

Decryption works by applying the same XOR operation with the same key, which reverses the encryption process and restores the original image.

The user must input the same key that was used for encryption to successfully decrypt the image.

Key Features:

XOR-based Encryption: The encryption process uses the XOR bitwise operation to modify pixel values.

Symmetric Decryption: The same key is used for both encryption and decryption.

Supports Any Image: This script works on any image format supported by the Python Imaging Library (PIL), such as PNG, JPEG, and BMP.
User-Friendly Input: The user can easily provide the image file path, encryption key, and desired output path.
