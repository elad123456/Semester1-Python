from itertools import count
from operator import index
def is_letter(letter:str)->bool:
    if ord(letter)>=65 and ord(letter)<=122:
        return True
    else:
        return False

def reverse_only_alph(sentence:str):
    reverse_sentence_=''
    not_letters_imdex=[]
    return_sentence=''
    count=0
    for letter in sentence:
        if is_letter(letter):
            reverse_sentence_+=letter
        else:
            not_letters_imdex.append((count,letter))
        count+=1
    reverse_sentence_=reverse_sentence_[len(reverse_sentence_)-1::-1]
    count=0
    while count<len(sentence):
        if  any([count in t for t in not_letters_imdex]):
            for simbole in not_letters_imdex:
                if simbole[0]==count:
                    return_sentence+=simbole[1]
        else:
            return_sentence+=reverse_sentence_[0]
            reverse_sentence_=reverse_sentence_[1:len(reverse_sentence_)]
        count+=1
    return return_sentence

sentence=input()
print(reverse_only_alph(sentence))