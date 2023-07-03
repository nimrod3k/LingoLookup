from blocks.block import Block
import nltk
from nltk.corpus import wordnet


class White(Block):
    def __init__(self,hint,length = -1):
        super().__init__(hint, length)

    def solve_top(self):
        return "not implemented"
    
    def solve_mid(self):
        return self.hint
    
    def solve_bot(self):
        list_synonyms = []
        for syn in wordnet.synsets(self.hint): 
            for lemm in syn.lemmas(): 
                list_synonyms.append(lemm.name())

        return list(set(list_synonyms))