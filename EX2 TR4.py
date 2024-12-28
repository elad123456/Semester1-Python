def merge_emps(list1 :list,list2:list):
    meshutaf=[]
    new_list=[]
    for i in list1:
        for k in list2:
            if i[0]==k[0] and i[0] not in meshutaf:
                meshutaf.append(i[0])
    for i in list1:
        if i[0] not in meshutaf:
            new_list.append(i)
        elif i[0] in meshutaf:
            for k in list2:
                if i[0]==k[0]:
                    new_list.append([i[0],i[1]+k[1]])
    for i in list2:
        if i[0] not in meshutaf:
            new_list.append(i)
    print(new_list)

list1=(input())
list1=eval(list1)
print(list1)
list2=input()
list2=eval(list2)
merge_emps(list1,list2)