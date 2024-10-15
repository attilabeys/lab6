def tup(tup1):
    for i in tup1:
        if i in ("", None, 0):
            return False
    return True
        
myTup = ("", "banana", "banana", "Cherry", "apple")
myTup1 = ("banana", "ll", "ll", "ll")
myTup2 = ("kjf", None, "krjgnm", 0)

a = tup(myTup)
b = tup(myTup1)
c = tup(myTup2)
print(a,b,c)
        