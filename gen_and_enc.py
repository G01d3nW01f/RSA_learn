#!/usr/bin/python3

import math
import random

def init():

    while True:
        print("Enter the text for ascii encode")
        plain_text = input("> ")
        
        if plain_text != "":
            return plain_text
            break
        else:
            print("input any")

def encode(plain_text):
    print(f"Your Text: {plain_text}")

    encode_array = [ord(c) for c in plain_text]
    print("Encoded to ascii code ")
    line_maker()
    print(encode_array)
    
    text_line = "".join(chr(i) for i in encode_array)
    print(f"------> {text_line}")
    
    
    line_maker()
    return encode_array
    
def gen(a,b):
    if b == 0:
        return a
        
    return gen(b,a%b)
    
def prm_finder():
    test_num = random.randrange(10,100)
    
    for i in range(2,test_num):
        if test_num % i == 0:
            return prm_finder()
            
        return test_num
    
def line_maker():
    line = "+"+"-"*70+"+"
    print(line)
    
    
def en_cryptor(e,n,encode_array):
    
    decode_array = []
    encrypt_value = e
    #decrypt_value = d
    p_and_q = n
    
    for i in encode_array:
        
        crptd_value = i ** e % n
        decode_array.append(crptd_value)
    line_maker()
    line_maker()
    print("[>]Decrypted (ascii_code):")    
    print(decode_array)
    
    text_line = "".join(chr(i) for i in decode_array)
    print(f"-----> {text_line}")
    
    line_maker()
                
    
if __name__ == "__main__":
    
    line_maker()

    plain_text = init()
    encode_array = encode(plain_text)
    
    p = prm_finder()
    q = prm_finder()
    n = p * q
    
    phi = (p-1) * (q-1)
    
    pub_keys = []
    
    for i in range(2,phi):
        if gen(i,phi) == 1 and gen(i,n) == 1:
            pub_keys.append(i)
        if len(pub_keys) >= 100:
            break
        
    e = random.choice(pub_keys)
    del(pub_keys)

    priv_keys = []
    i = 2

    while len(priv_keys) < 5:
        if i * e % phi == 1:
            priv_keys.append(i)
        
        i += 1
        
    d = random.choice(priv_keys)
    del(priv_keys)
    
    print(f"[+]PublicKey : {e} <=> {n}")
    print(f"[+]PrivateKey: {d} <=> {n}")
    
    line_maker()
    
    en_cryptor(e,n,encode_array)
    

