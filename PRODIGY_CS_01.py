def caesar_cipher_encrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():  # Check if character is a letter
            shift_base = 65 if char.isupper() else 97  # ASCII base for uppercase/lowercase
            result += chr((ord(char) - shift_base + shift) % 26 + shift_base)
        else:
            result += char  # Non-alphabetic characters remain unchanged
    return result


def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)  # Just reverse the shift


# Main Program
if __name__ == "__main__":
    message = input("Enter your message: ")
    shift = int(input("Enter shift value (0-25): "))

    encrypted = caesar_cipher_encrypt(message, shift)
    print(f"\nEncrypted Message: {encrypted}")

    decrypted = caesar_cipher_decrypt(encrypted, shift)
    print(f"Decrypted Message: {decrypted}")


    
