import os
def copy(way, way2):
   try:
      with open(way, 'r') as s:
         with open(way2, 'w') as g:
            marks = s.read()
            g.write(marks)
    
   except FileNotFoundError:
      print("File not found")


way = input()
way2 = input()
copy(way, way2)