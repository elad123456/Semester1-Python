n=int(input("enter a number:"))
n1=n
revers=0
i=0
while n!=0:
    i+=1
    n=n//10
for k in range(i):
    revers+=(n1%10)*(10**(i-1))
    n1=n1//10
    i-=1
print(revers)