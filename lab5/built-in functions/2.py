def upper(string):
    n1 = 0
    n2 = 0
    for i in string:
        if i.isupper():
            n1 += 1
        else:
            n2 += 1
    return n1, n2
    

text = 'AbjdHkFiEJjKFGEK'
a = upper(text)
print(a)
    