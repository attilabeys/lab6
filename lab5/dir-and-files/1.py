import os
def onlyDir(way):
    directions = [d for d in os.listdir(way) if os.path.isdir(os.path.join(way, d))]
    for i in directions:
        print(i)
    lists = [f for f in os.listdir(way) if os.path.isfile(os.path.join(way, f))]
    for i in lists:
        print(i)
    all = os.listdir(way)
    for i in all:
        print(i)
    
road = input()
onlyDir(road)