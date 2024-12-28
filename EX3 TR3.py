ezer=True
nums=[]
num = int(input(" Enter positive numbers: "))
while ezer:
    if num<=0:
        ezer=False
    else:
        nums.append(num)
        num = int(input())
if len(nums) > 0:
    max=0
    A=nums[0]
    B=nums[0]
    for a in range(len(nums)-1):
        for b in range(a,len(nums)):
            if nums[a]<nums[b] and nums[b]-nums[a]>max:
                max=nums[b]-nums[a]
                B=b
                A=a
    if max==0:
        print("There are no such indices")
    else:
        print(A,B)
else:
    print("There are no such indices")