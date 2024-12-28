num=int(input("Enter positive numbers:"))
numbers=[num]
while num>0:
    num = int(input(""))
    if num>0:
        numbers.append(num)
num = int(input("Enter num:"))
boolean=False
if len(numbers)>0:
    for i in range(len(numbers)-1):
        for k in range(i,len(numbers)):
            if numbers[i]+numbers[k]==num:
                boolean=True
                break
print(boolean)