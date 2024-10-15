import os
def checks(way):
    if os.path.exists(way):
       print("exists")
    else:
       return
    if os.access(way, os.R_OK):
     print('readable')
    if os.access(way, os.W_OK): 
       print('writable')
    if os.access(way, os.X_OK):
       print('executable')

way = input()
checks(way)