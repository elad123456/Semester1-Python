counter=0
num=int(input("Enter positive numbers: "))
if num<=0:
    print("Empty series")
else:
    numbers=[num]
    counter=0
    max_counter=0
    max_index=0
    index=0
    while num>0:
        num=int(input())
        if num>0:
            numbers.append(num)
    for i in range(len(numbers)-1):
        if numbers[i]>numbers[i+1]:
            counter+=1
            if counter>max_counter:
                index=i-counter+1
                max_counter=counter
        else:
            counter=0


    print(index)
