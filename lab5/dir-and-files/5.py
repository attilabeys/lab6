def intoFile(way, list1):
    try:
        with open(way, 'w') as file:
            for i in list1:
                file.write(f"{i}\n")
            print('successfully')
    except FileNotFoundError:
        print('File does not exist')

way = input()
list1 = ["BANANA", "Banana", "banana", "bANANA"]
intoFile(way, list1)
    