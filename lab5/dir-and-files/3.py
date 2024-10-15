import os
def checks(way):
    if os.path.exists(way):
       print("exists")
       directory = [d for d in os.listdir(way) if os.path.isdir(os.path.join(way, d))]
       for i in directory:
          print(i)
       files = [f for f in os.listdir(way) if os.path.isfile(os.path.join(way, f))]
       for i in files:
          print(i)

    else:
       return
    



way = input()
checks(way)