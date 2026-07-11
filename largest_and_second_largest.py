List=[1,20,7,89,4,7,0,33,66,98,666,98]
Bigest=0
Second_Bigest=0
for i in range(0,len(List)):
    if List[i]>Bigest:
        Bigest=List[i]
    if List[i] > Second_Bigest & List[i] < Bigest:
        Second_Bigest=List[i]
print(Bigest)
print(Second_Bigest)
        