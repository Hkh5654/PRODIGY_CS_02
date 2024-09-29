from PIL import Image

def encrypt_image(image_path, output_path, key):
    # Open an image file
    with Image.open(image_path) as img:
        pixels = img.load()  # Load pixel data
        
        # Get image dimensions
        width, height = img.size

        # Encrypt each pixel
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # Simple XOR operation with key for encryption
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)
        
        # Save the encrypted image
        img.save(output_path)
        print(f"Image encrypted and saved as {output_path}")

def decrypt_image(image_path, output_path, key):
    # Open an image file
    with Image.open(image_path) as img:
        pixels = img.load()  # Load pixel data
        
        # Get image dimensions
        width, height = img.size

        # Decrypt each pixel (same operation as encryption)
        for x in range(width):
            for y in range(height):
                r, g, b = pixels[x, y]
                # Simple XOR operation with key for decryption
                pixels[x, y] = (r ^ key, g ^ key, b ^ key)
        
        # Save the decrypted image
        img.save(output_path)
        print(f"Image decrypted and saved as {output_path}")

# User inputs
key = int(input("Enter encryption key (0-255): "))
mode = input("Type 'encrypt' to encrypt or 'decrypt' to decrypt: ")
image_path = input("Enter the image file path: ")
output_path = input("Enter the output file path: ")

# Perform the operation
if mode == 'encrypt':
    encrypt_image(image_path, output_path, key)
elif mode == 'decrypt':
    decrypt_image(image_path, output_path, key)
else:
    print("Invalid mode selected.")