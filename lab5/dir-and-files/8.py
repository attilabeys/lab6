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
    try:
       if os.path.exists(way):
          os.remove(way)
    except FileNotFoundError:
       print("File does not exists") #No need to delete
       


way = input()
checks(way)