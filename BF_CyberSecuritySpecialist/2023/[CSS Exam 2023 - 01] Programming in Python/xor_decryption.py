import json
import os

def determine_xor_key(original_file, encrypted_file):
    """
    Determine the 32-byte XOR key from the original and encrypted versions of the file.
    """
    with open(original_file, 'rb') as original, open(encrypted_file, 'rb') as encrypted:
        original_bytes = original.read(32)
        encrypted_bytes = encrypted.read(32)

        # Determine key by XOR'ing each byte of the original with the encrypted file
        key = bytes([original_bytes[i] ^ encrypted_bytes[i] for i in range(32)])
        return key

def print_key(key):
    """
    Print the 32 bytes of the encryption key.
    """
    key_hex = key.hex()
    print(f"Encryption key (hex): {key_hex}")

def save_key_to_json(key, output_filename='key.json'):
    """
    Save the key to a JSON file.
    """
    key_hex = key.hex()
    with open(output_filename, 'w') as json_file:
        json.dump({'key': key_hex}, json_file)

def decrypt_file(input_filename, output_filename, key):
    """
    Decrypt an encrypted file using the provided XOR key.
    """
    key_length = len(key)
    with open(input_filename, 'rb') as encrypted, open(output_filename, 'wb') as decrypted:
        i = 0
        while True:
            byte = encrypted.read(1)
            if not byte:
                break
            decrypted_byte = bytes([byte[0] ^ key[i % key_length]])
            decrypted.write(decrypted_byte)
            i += 1

def main():
    # Filenames
    original_file = 'c1-logo.jpg'
    encrypted_file = 'c1-logo.jpg_encrypted'
    encrypted_files = [
        'c1-message.txt_encrypted',
        'c1-picture.jpg_encrypted',
        'c1-document.pdf_encrypted'
    ]

    # Determine the XOR key
    key = determine_xor_key(original_file, encrypted_file)

    # Print the key
    print_key(key)

    # Save the key to a JSON file
    save_key_to_json(key)

    # Decrypt the remaining files
    for encrypted_filename in encrypted_files:
        output_filename = encrypted_filename.replace('_encrypted', '_decrypted')
        decrypt_file(encrypted_filename, output_filename, key)
        print(f"Decrypted {encrypted_filename} to {output_filename}")

if __name__ == "__main__":
    main()
