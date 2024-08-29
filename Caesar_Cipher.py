alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r',
            's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j',
            'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']


def caesar(start_text, shift_amount, cipher_direction):
    if cipher_direction == "decode":
        shift_amount *= -1
    end_text = ""
    for char in start_text:
        if char in alphabet:
            end_text += alphabet[alphabet.index(char) + shift_amount]
        else:
            end_text += char

    print(f"Your {cipher_direction}d text is: {end_text}\n")


should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt: \n")
    if direction == "encode" or direction == "decode":
        text = input("Type your message: \n").lower()
        shift = int(input("Type the shift number:\n"))
        shift = shift % 26
        caesar(start_text=text, shift_amount=shift, cipher_direction=direction)
    else:
        print("\nInvalid Input !!\n")

    result = input("Type 'yes' if you want to go again. Otherwise type 'no' !\n")
    if result == "no":
        should_continue = False
        print("Good Bye.")
    elif result == "yes":
        should_continue = True
    else:
        print("\nInvalid Input !!\n")
