import hashlib
from collections import deque
import re
salt = 'yjdafjpo'
keys = 64
index = 0
hashlist = deque()

#result = hashlib.md5(str2hash.encode()).hexdigest()

keyCount = 0



# gasesc primul hash cu 3 caractere repetate
while True:
    hash = hashlib.md5((salt + str(index)).encode()).hexdigest()
    m = re.search(r'(\d)\1{2}', hash) 
    if  m != None:
        (start, _) = m.span()
        c = hash[start]
        break
    index += 1

# trebuie sa am 1000 de hash-uri in lista


while keyCount < keys:
    # adaug in hashlist  hashuri pana cand am 1000
    n = len(hashlist)
    if n < 1000:
        for i in range(1000 - len(hashlist)):
            hashlist.append(hashlib.md5((salt + str(index + 1 + i + n)).encode()).hexdigest())  
    # caut primul hash cu 5x 
    for item in hashlist:
        m = re.search('(' + c + ')\1{4}', hash) 
        if m != None:
            keyCount += 1
            break
    hashlist.popleft()
    

    
            
    
    
