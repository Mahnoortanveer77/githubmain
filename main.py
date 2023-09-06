import string
def encoding(text, alpha, alphar):
    message = ''
    for ch in text:
        index = alpha.index(ch)
        message += alphar[index]
    return message


def decoding(text, alpha, alphar):
    message = ''
    for ch in text:
        index = alphar.index(ch)
        message += alpha[index]
    return message


if _name_ == "_main_":
    alpha = string.printable
    alphar = alpha[::-1]
    text = input("Please enter your text: ")

    print("Original Message:" + text)

    encoded_message = encoding(text, alpha, alphar)
    print("Encoded Message: " + encoded_message)

    decoded_message = decoding(encoded_message, alpha, alphar)
    print("Decoded Message: " + decoded_message)

    validation = (text == decoded_message)
    print("Did decoding work? :" + str(validation))