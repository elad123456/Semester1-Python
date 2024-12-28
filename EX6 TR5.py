
def how_many_words(sentence:str,n:int=1)->list:

    ezer=sentence.split(' ')

    most_common_words={}
    for word_check in ezer:
        if word_check not in most_common_words:
            counter=0
            for word in ezer:
                if word==word_check:
                    counter+=1
            most_common_words[word_check]=counter

    if n>=len(ezer):
        n=len(most_common_words.keys())
    ezer = []
    while len(ezer)!=n:
        max_h=max(most_common_words.values())
        for i in most_common_words:
            if most_common_words[i]==max_h:
                ezer.append(i)
                del most_common_words[i]
                break
    return_sentence=''
    for word in ezer:
        return_sentence+=word
        return_sentence+=' '
    return return_sentence
sentence=input('')
n=int(input(''))
print(how_many_words(sentence,n))