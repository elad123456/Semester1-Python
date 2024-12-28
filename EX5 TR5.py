def legit(n1:str,n2:str)->list:
    numbers=n1+n2
    n1 = n1.replace('-', '')
    n2 = n2.replace('-', '')
    n2 = n2.replace(' ', '')
    n1 = n1.replace(' ', '')
    if len(n1)%2!=0:
        return [False, 'odd series']
    if len(n2)%2!=0:
        return [False, 'odd series']
    numbers=numbers.replace('-','')
    numbers=numbers.replace(' ','')
    leng=len(numbers)
    if len(numbers)%2!=0:
        return [False,'odd series']
    for l in numbers:
        if not(l=='0' or l=='1' or l=='2' or l=='3' or l=='4' or l=='5' or l=='6' or l=='7' or l=='8' or l=='9' or l=='-'):
            return [False,'invalid inputs']
    else:
        return [True]
def polinom_shrinking(n1:str,n2:str)->str:
    numbers=n1+n2
    numbers=numbers.replace(' ','')
    legit_1=legit(n1,n2)
    if legit_1[0]==False:
        return legit_1[1]
    polinom_dict={}
    ezer=[]
    i=0
    while len(numbers)!=0:
        if numbers[i]=='-':
            ezer.append(numbers[i:i+2])
            numbers=numbers[2::]
        else:
            ezer.append(numbers[i])
            numbers=numbers[1::]

    for i in range(len(ezer)):
        if i%2==0:
            mekadem=int(ezer[i])
            hezka=int(ezer[i+1])
            if hezka not in polinom_dict:
                polinom_dict[hezka]=mekadem
            else:
                polinom_dict[hezka]+=mekadem
    ezer=''
    for i in polinom_dict:
        if polinom_dict[i]!=0:
            ezer+=str(polinom_dict[i])
            ezer+=' '
            ezer+=str(i)
            ezer+=' '
    return ezer
n_1=input('')
n_2=input('')
print(polinom_shrinking(n_1,n_2))
