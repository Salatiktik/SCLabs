from constants import REGEXSENTENCE
from re import findall,split

def text_check(text:str):
    #initials check
    for match in findall("[A-Z]{1}\.", text):
        text = text.replace(match, match.replace('.',' '))
    
    text = text.replace('\n',' ')

    return text

def sentence_count(text:str):
    return(len(findall(REGEXSENTENCE, text)))

def declarative_sentence_count(text:str):
    count = 0
    for match in findall(REGEXSENTENCE, text):
        if match[4] != '.' and match[4] != '...':
            count+=1

    return count

def average_sentences_length(text:str):
    return (len(text)-len(findall("[\s,\.!?]+", text)))/len(findall(REGEXSENTENCE, text))    

def average_words_length(text:str):
    words = split('[,\.\s!?]+',text);

    for word in words:
        if(word.isdigit() or word == ''):
            words.remove(word)
    
    return((len(text)-len(findall("[\s,\.!?]+", text)))/len(words))

def top_ngramm(text:str,n:int,k:int):
    words = split('[,\.\s!?]+',text);
    n_gramms = {}
    top_ngramms = {}

    for word in words:
        if(word.isdigit()):
            words.remove(word)
            continue

        if(len(word)>=n):
            for i in range (0,len(word)-n):
                n_gramms[word[i:i+n]] = n_gramms.get(word[i:i+n], 0) + 1

    top_ngramms = sorted(n_gramms.items(), key = lambda x: x[1], reverse = True)[:k]

    print("\t===================")
    for item in top_ngramms:
        print("\t",item[0],"      ",item[1])






        
        

        


        


        