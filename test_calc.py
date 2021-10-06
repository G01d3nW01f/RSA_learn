
#!/usr/bin/python3


def init():
    
    cyph_txt = input("[+]Enter CypherText: ")
    p = input("[+]Enter PubKey1   : ")
    q = input("[+]Enter PubKe2    : ")

    return p,q,cyph_txt
    
def prime_num_create():
    PrimeList = [2]
    maxNumber = 10000
    for x in range(2,maxNumber):
        for y in PrimeList:
            if x % y == 0:
                break
            
        else:
            
            PrimeList.append(x)
    print(f"[:]Generated: {len(PrimeList)}")            
    return PrimeList

def fix_array(p,prime_nums):
    
    fixed_array = []
    
    for i in prime_nums:
        if int(i) > int(p):
            fixed_array.append(i)
            
    print(f"[!]Fixed: {len(fixed_array)}")
    return fixed_array 

def clck(cyph_txt,q,fixed_array):
    
    cyph_array = [ord(p) for p in cyph_txt] 
    
    
    for m in fixed_array:
        dcrypt_arr = []
        for i in cyph_array:
            
            i = i ** int(m) % int(q) 
            dcrypt_arr.append(i)
    
        print(dcrypt_arr)            
        t = [chr(p) for p in dcrypt_arr]
        
        z = "".join(chr(p) for p in dcrypt_arr)
        
        print(z)
    
            


if __name__ == "__main__":
    p,q,cyph_txt = init()
    
    prime_nums = prime_num_create()
    fixed_array = fix_array(p,prime_nums)
    clck(cyph_txt,q,fixed_array)
