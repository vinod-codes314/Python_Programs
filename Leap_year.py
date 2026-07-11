n=int(input("Enter Year :"))
if(n%4==0 or n%400==0):
    print("Leap Year")
else:
    print("Non Leap Year")