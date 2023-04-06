from textStats import text_check,sentence_count,nondeclarative_sentence_count,average_words_length,average_sentences_length, top_ngramm
from constants import K,N
from texts import TEXTS

def task_one():
    option = input("Choose option:\n\t1)One of the prepeared texts\n\t2)Your text\n\nInput option:")
    if option=="1":
        textNum = input("Choose text number:1-3\n\nInput number:")
        if(textNum.isdigit() and int(textNum)>0 and int(textNum) <= len(TEXTS)):
            text = text_check(TEXTS[int(textNum)-1])
        else:
            print("You choosed wrong text, so text is default!")
            text = text_check(TEXTS[0])
    elif option == "2":
        text = input("Input the text:")
        if(text.isdigit() or len(text)==0):
            print("You enter wrong text, so text is default!")
            text = text_check(TEXTS[0])
    else:
        print("You enter wrong option, so text is default!")
        text = text_check(TEXTS[0])

    option = input("Choose option:\n\t1)Default k and n values (k = 10, n = 4)\n\t2)Your own values\n\nInput option:")
    if option=="1":
        k = K
        n = N

    elif option == "2":
        k = input("Enter k value:")
        if not k.isdigit():
            print("You enter wrong value, so k is default!")
            k = K
        else:
            k = int(k)        

        n = input("Enter n value:")
        if(not n.isdigit()):
            print("You enter wrong value, so n is default!")
            n = N
        else:
            n = int(n)
    else:
        print("You enter wrong option, so values are default!")
        k = K
        n = N

    print("=======================================================\n")
    print(text)
    print("\n=======================================================\n")
    print("\tSentence count: ",sentence_count(text))
    print("\tNondeclarative sentences count: ",nondeclarative_sentence_count(text))
    print("\tAverage sentences length: {0:.2f}".format(average_sentences_length(text)))
    print("\tAverage words length: {0:.2f}".format(average_words_length(text)))
    print("\tTop-{K} {N}-gramms:".format(K=k,N=n))
    top_ngramm(text,n,k)