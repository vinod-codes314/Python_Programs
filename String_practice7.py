str=input("Enter Text : ")
n="AEIOUaeiou"
count=0
for i in range(0,len(str)):
    if str[i] in n:
        count +=1
print("count of vowels : ",count)