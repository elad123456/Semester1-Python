
def org_str(values:list)->list:
    leng=len(values)
    ezer=[]
    search=True
    for k in range(leng):
        for i in range(len(values)):
            if search:
                if not is_sign(values[i]):
                    ezer.append(values[i])
                    values.pop(i)
                    search=not search
                    break
            else:
                if is_sign(values[i]):
                    ezer.append(values[i])
                    values.pop(i)
                    search=not search
                    break
    return ezer
def is_number(n:str)->bool:
    if ord(n) >= 48 and ord(n) <= 57:
        return True
    else:
        return False
def is_sign(n:str)->bool:
    if n=='*' or n=='+' or n=='-' or n=='/' or n=='//':
        return True
    else:
        return False
def legit_str(values)->list:
    count_num=0
    count_signs=0
    ezer=[]
    count=0
    ezer_bool=True
    for l in values:
        if ezer_bool:
            if ord(l)>=48 and ord(l)<=57 :
                count_num += 1
                ezer.append(l)
                if count+1!=len(values):
                    if ord(values[count+1])>=48 and ord(values[count+1])<=57:
                        ezer_bool=False
                        ezer.pop()
                        ezer.append(l+values[count+1])
                        count+=1

            elif l=='*' or l=='+' or l=='-':
                count_signs+=1
                ezer.append(l)
            elif l=='/':
                count_signs+=1
                ezer.append(l)
                if count+1!=len(values):
                    if values[count+1]=='/':
                        ezer_bool = False
                        ezer.pop()
                        ezer.append(l+values[count+1])
                        count += 1

            elif l==' ':
                l=l
            else:
                return [False,'invalid letters']
            count+=1
        else:
            ezer_bool=True
    if count_num-1==count_signs:
        return [True,ezer]
    if count_num>count_signs:
        return [False,'too many numbers']
    else:
        return [False, 'missing a number']

def evaluate_expression(values)->int or str:
    ezer=legit_str(values)
    new_ezer=[]
    if not ezer[0]:
        return ezer[1]
    else:
        ezer=org_str(ezer[1])
        ezer = ['/' if x == '//' else x for x in ezer]

        kefel=True
        while len(ezer)!=1:
            if kefel:
                for i in range(len(ezer)):
                    if ezer[i]=='*':
                        number=int(ezer[i-1])*int(ezer[i+1])
                        ezer[i-1]=number
                        ezer.pop(i)
                        ezer.pop(i)
                        break
                    if ezer[i]=='/':
                        number=int(ezer[i-1])/int(ezer[i+1])
                        ezer[i-1]=number
                        ezer.pop(i)
                        ezer.pop(i)
                        break
                    if '*' not in ezer and '/' not in ezer:
                        kefel=False
                        break

            else:
                for i in range(len(ezer)):
                    if ezer[i]=='+':
                        number=int(ezer[i-1])+int(ezer[i+1])
                        ezer[i-1]=number
                        ezer.pop(i)
                        ezer.pop(i)
                        break
                    if ezer[i]=='-':
                        number=int(ezer[i-1])-int(ezer[i+1])
                        ezer[i-1]=number
                        ezer.pop(i)
                        ezer.pop(i)
                        break
        return ezer[0]
values=input('')
print(evaluate_expression(values))


