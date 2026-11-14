def encrypt(text, shift):
    result = ""

    for char in text:
        if char.isalpha():
            start = ord('A') if char.isupper() else ord('a')
            new_char = chr((ord(char) - start + shift) % 26 + start)
            result += new_char
        else:
            result += char

    return result


def decrypt(text, shift):
    return encrypt(text, -shift)


print("===== CAESAR CIPHER =====")
print("1. Encrypt")
print("2. Decrypt")

choice = input("Enter your choice (1 or 2): ")
message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

if choice == "1":
    print("Encrypted message:", encrypt(message, shift))
elif choice == "2":
    print("Decrypted message:", decrypt(message, shift))
else:
    print("Invalid choice!")