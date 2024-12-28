def list_of_number(n:str):
    if n=='2':
        return ['a','b','c']
    if n=='3':
        return ['d','e','f']
    if n=='4':
        return ['g','h','i']
    if n=='5':
        return ['j','k','l']
    if n=='6':
        return ['m','n','o']
    if n=='7':
        return ['p','q','r','s']
    if n=='8':
        return ['t','u','v']
    if n=='9':
        return ['w','x','y','z']
def cellpohone(n:int,sentence:str)->bool:
    n=str(n)
    if '1' in n:
        return False
    if len(n)!=len(sentence):
        return False
    for i in range(len(n)):
        if not (sentence[i] in list_of_number(n[i])):
            return False
    return True
n=int(input(''))
sentence=input('')
print(cellpohone(n,sentence))