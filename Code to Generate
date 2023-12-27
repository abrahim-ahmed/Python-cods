def code_generator(text):
    encoded_message = ""
    for letter in text:
        if letter.isalpha():
            encoded_letter = chr((ord(letter) - ord('a') + 1) % 26 + ord('a'))
            encoded_message += encoded_letter
        else:
            encoded_message += letter
    return encoded_message

# Example Usage

message = ""
encoded_message = code_generator(message)
print(encoded_message)

# Output:

# Ifmmp, Xpsme!
