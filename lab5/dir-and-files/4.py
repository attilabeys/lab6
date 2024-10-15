def lines(txtfile):
  try:
    with open(txtfile, "r") as file:
     lines = file.readlines()
     return len(lines)
  except FileNotFoundError:
    print('File does not exists')


way = input("Enter your path ")
count = lines(way)
print(count)