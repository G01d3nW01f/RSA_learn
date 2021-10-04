#!/usr/bin/python3

import random
import math

def gen(a,b):
    if b == 0:
        return a
    return gen(b,a%b)
    
def prm_finder():
    test_number = random.randrange(10,100)
    
    #for i in test_number: 
    #    if test_number % i == 0:
    #        return i
     
    for i in range(2,test_number):
        if test_number % i == 0:
            return prm_finder()
            
        return test_number
        
p = prm_finder()
q = prm_finder()

n = p*q
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

print(f"PublicKeys : {e,n}")
print(f"PrivateKeys: {d,n}")


