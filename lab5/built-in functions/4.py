import time

def mySqrt(numb, myTime):
    sec = myTime / 1000
    time.sleep(sec)
    if numb == 0 or numb == 1:
        return numb
    else:
        res = numb ** 0.5
        return res

number = 144
mil = 1345 

a = mySqrt(number, mil)
print(f"The square root of {number} after {mil} milliseconds is: {a}")
