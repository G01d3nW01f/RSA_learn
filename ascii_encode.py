#!/usr/bin/python3

def init():

    while True:
        print("Enter the text for ascii encode")
        plain_text = input(">")
        
        if plain_text != "":
            return plain_text
            break
        else:
            print("input any")

def encode(plain_text):
    print(f"Your Text: {plain_text}")

    encode_array = [ord(c) for c in plain_text]
    print("Encoded to ascii code ")
    print(encode_array)


if __name__ == "__main__":

    plain_text = init()
    encode(plain_text)
