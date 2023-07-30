from caesar_cipher_art import logo

print(logo)

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
            'v', 'w', 'x', 'y', 'z']


def caesar(input_text, shift_amount, cipher_direction):
    end_text = ""
    for char in input_text:
        if char in alphabet:
            position = alphabet.index(char)
            if cipher_direction == "encode":
                position += shift_amount % 26
            elif cipher_direction == "decode":
                position -= shift_amount % 26
            if position > 25:
                position -= 26
            elif position < 0:
                position += 26
            end_text += alphabet[position]
        else:
            end_text += char

    print(f"The {direction}d text is {end_text}")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    caesar(input_text=text, shift_amount=shift, cipher_direction=direction)
    prompt = input("Type 'yes' if you want to go again. Otherwise type 'no'.\n")
    if prompt == 'no':
        should_continue = False
        print("Goodbye!!!")
