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


def ligal_list(list1:list)->bool:
    if list1[0]>=len(list1):
        return True
    else:
        i=0
        j=i+list1[i]
        while j<len(list1):

            if list1[j]==0:
                m=j
                for k in range(list1[i]):
                    j=m-k
                    if list1[j]!=0:
                        break
                if k==list1[i]-1:
                    return False
            else:
                i=j
                j=i+list1[i]
        return True
list1=input("")
list1=str_to_int_list(list1,',')

print(ligal_list(list1))