n=int(input("enter a number: "))
e=1
ezer1=1
for i in range(1,n+1):
    e+=ezer1*(1/i)
    ezer1*=(1/i)
print(e)