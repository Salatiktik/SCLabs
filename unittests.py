import unittest
from textStats import text_check,sentence_count,nondeclarative_sentence_count,average_words_length,average_sentences_length, top_ngramm

class TestTextCheck(unittest.TestCase):
    
    def test_noEOL(self):
        self.assertEqual(text_check("aaaaaaaaaa"),"aaaaaaaaaa")
        self.assertEqual(text_check(""),"")

    def test_onlyEOL(self):
        self.assertEqual(text_check("\n\n\n\n\n\n\n\n\n\n\n\n\n"),"             ")
       
    def test_simple(self):
        self.assertEqual(text_check("aaa\naaa\naaa"),"aaa aaa aaa")

    def test_initials(self):
        self.assertEqual(text_check("J.K.Roaling"),"J K Roaling")

class SentenceStatisticCheck(unittest.TestCase):

    def test_dot(self):
        self.assertEqual(sentence_count("I love you."),1)
        self.assertEqual(sentence_count("I love you..."),1)

    def test_exclMark(self):
        self.assertEqual(sentence_count("I love you!"),1)
        self.assertEqual(sentence_count("I love you!!!"),1)

    def test_questMark(self):
        self.assertEqual(sentence_count("I love you?"),1)
        self.assertEqual(sentence_count("I love you???"),1)

    def test_questExclMark(self):
        self.assertEqual(sentence_count("I love you?!"),1)
        self.assertEqual(sentence_count("I love you!?"),1)

    def test_abreviation(self):
        self.assertEqual(sentence_count("Mr. J K Smit try to do something at 10 p.m. , but there are some problems: wind, sun, etc."), 1)

    def test_direct(self):
        self.assertEqual(sentence_count("She says, \"The lessons begin at 9 o’clock.\""),1)
    
    def test_onlyNonDeclarative(self):
        self.assertEqual(nondeclarative_sentence_count("She! Me! Us!"),3)

    def test_noNonDeclarative(self):
        self.assertEqual(nondeclarative_sentence_count("She..."),0)

    def test_sentenceLen(self):
        self.assertEqual(average_sentences_length("She..."),3)
        self.assertEqual(average_sentences_length("Nice to meet you! I greatful to yo!"),13)
        self.assertEqual(average_sentences_length("I! I Love! You!"),3)
        self.assertLessEqual(average_sentences_length("Hi! My name is Daniil. I like singing, writing songs and making something greate!")-21.333,0.001)

class WordsStatisticCheck(unittest.TestCase):

    def test_wordLen(self):
        self.assertEqual(average_words_length("Hi"),2)
        self.assertEqual(average_words_length("aaaaaaaaaaaaaaaaaaaa"),20)
        self.assertEqual(average_words_length("10 years"),5)
        self.assertEqual(average_words_length("1234567890"),0)    

unittest.main()