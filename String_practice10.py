str=input("Enter Text : ")
revstr=str[::-1]
if str == revstr:
    print(str,"is palindrome")
else:
    print(str,"is not palindrome")