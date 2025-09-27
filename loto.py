import random
def pacs(i):
    a=[]
    
    for aa in range(50):
        a=a+[aa+1]
    return a

def packget(p):
    a=[]
    for aa in range(8):
        aaa=p[random.randrange(len(p)-1)]
        a=a+[aaa]
        p.remove(aaa)
    a.sort()
    return p,a 

print("\033c\033[43;30m\n")
a=pacs(50)
a,p=packget(a)
print(p)
a,p=packget(a)
print(p)
a,p=packget(a)
print(p)
a,p=packget(a)
print(p)
a,p=packget(a)
print(p)
print(a)