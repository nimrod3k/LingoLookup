from blocks.block import Block
from PyDictionary import Dictionary
import nltk
from nltk.corpus import wordnet
from nltk.tokenize import word_tokenize
from collections import defaultdict
from wordhoard import Antonyms, Synonyms

#nltk.download('punkt')
class Black(Block):
    def __init__(self,hint,length = -1):
        super().__init__(hint, length)

    def solve_top(self):
        return "not implemented"
    
    def solve_mid(self):
        ans = ""
        for i in self.hint:
            ans = i + ans
        return ans
    
    def solve_bot(self):
        list_antonyms = []
        secondary = []
        tertiary = []

        # for syn in wordnet.synsets(self.hint): 
        #     for lemm in syn.lemmas(): 
                
        #         if lemm.antonyms(): 
        #             list_antonyms.append(lemm.antonyms()[0].name())

        #wordhoard
        for i in Antonyms(self.hint).find_antonyms():
            list_antonyms.append(i)
            for j in Synonyms(i).find_synonyms():
                secondary.append(j)

        for i in Synonyms(self.hint).find_synonyms():
            for j in Antonyms(i).find_antonyms():
                secondary.append(j)
                for k in Synonyms(j).find_synonyms():
                    tertiary.append(k)

        ret = {
            'Primary': list(set(list_antonyms)),
            'Secondary': list(set(secondary)),
            'Tertiary': list(set(tertiary))
            }
        return 
    