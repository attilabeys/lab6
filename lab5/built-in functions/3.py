def isPalindrome(s):
    s = s.replace(" ", "").lower()
    return s == s[::-1]

# Input from the user
string = input("Enter a string: ")
a = isPalindrome(string)
print(a)
