x=int(input("How many strings do you want to enter:"))
if x>1:
    strs_list=[]
    for i in range(x):
        sen=input()
        strs_list.append(sen)
    mini=strs_list[0]
    for sentence in strs_list:
        if len(sentence)<len(mini):
            mini=sentence
    sen=''
    for l in range(len(mini)):
        counter=0
        for k in range(x-1):
            if strs_list[k][l]==strs_list[k+1][l]:
                counter+=1
        if counter==x-1:
            sen+=strs_list[k][l]
    if sen!='':
        print(sen)
if x<=1 and x!=0:
    print("Invalid input")