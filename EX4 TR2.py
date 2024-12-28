from operator import length_hint
sum=0
ezer=0
id=input("enter your id number: ")
while length_hint(id)!=9:
    id = input("enter your id number: ")
for i in range(1,9):
    if i%2!=0:
        ezer=int(id[i-1])
        sum+=ezer
    else:
        ezer=int(id[i-1])*2
        if ezer>=10:
            sum+=(ezer%10)+(ezer//10)
        else:
            sum+=ezer
print(((sum+9)//10)*10-sum==int(id[8]))