def is_num(n:str):
    for i in range(len(n)):
        if n[i]=='1' or n[i]=='2' or n[i]=='3' or n[i]=='4' or n[i]=='5' or n[i]=='6' or n[i]=='7' or n[i]=='8' or n[i]=='9':
            n=n
        else:
            return False
    return True
def is_sign(n:str):
    if n=='/' or n=='*' or n=='+' or n=='-':
        return True
    else:
        return False