from textStats import text_check,sentence_count,declarative_sentence_count,average_words_length,average_sentences_length, top_ngramm

text = """Recently I've seen a film called Wonder. 
This film made me think a lot. The main character is a 10-years old boy who was born 
with a face deformity. The plot tells us his story of learning how to live in the 
society. A famous american actress Mrs. Julia Roberts plays a role of boy's mother. She 
is very sensible and always ready to support her son. The film has not a lot of 
special effects but its main effect is that he makes people think. J.P.Roberts...
At 10 p.m. I would like to eat something spicy!
Also i would like to tell you about many things. Butterflies, puzzles, etc. And this is cool!
"""

text = text_check(text)
print(sentence_count(text))
print(declarative_sentence_count(text))
print("{0:.2f}".format(average_sentences_length(text)))
print("{0:.2f}".format(average_words_length(text)))
top_ngramm(text,5,4)