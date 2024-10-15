import os
import string
def files(way):
 if not os.path.exists(way):
    os.makedirs(way)
 for letter in string.ascii_uppercase:
    with open(way + letter + ".txt", "w") as f:
        f.writelines(letter)

way = input()
files(way)        