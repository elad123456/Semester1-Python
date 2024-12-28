n=int(input(" Enter positive numbers: "))
nums=[]
while n>0:
    nums.append(n)
    n = int(input(""))
distance=0
boolean=False
low=int(input("Enter low: "))
high=int(input("Enter high: "))
current_place=0
for num in nums:
    for i in range(len(nums)):
        if num==nums[i]:
            if i-current_place>=low and i-current_place<=high:
                boolean=True
    current_place+=1
if low==0:
    print("Invalid input")
elif low<=high:
    print(boolean)
else:
    print("Invalid input")