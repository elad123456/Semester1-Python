def str_to_int_list(mach :str,tav :str =','):
    new_list=[]
    ezer=''
    count=0
    for letter in mach:
        count+=1
        if count==len(mach):
            ezer+=letter
            new_list.append(int(ezer))
        elif letter==tav:
            new_list.append(int(ezer))
            ezer=''
        else:
            ezer+=letter

    return new_list
string=input("")
new_list=str_to_int_list(string)
sum=0
for num in new_list:
    sum+=num
print("List is :",new_list,"List length is:",len(new_list),"List sum is:",sum)