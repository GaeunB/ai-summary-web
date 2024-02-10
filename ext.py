from typing import List
from konlpy.tag import Okt
from textrankr import TextRank

'''class MyTokenizer:
    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = text.split()
        return tokens'''


class OktTokenizer:
    def __init__(self):
        self.okt = Okt()

    def tokenize(self, text: str) -> List[str]:
        tokens: List[str] = self.okt.phrases(text)
        return tokens
    
def summarize_text(text: str) -> List[str]:
    mytokenizer = OktTokenizer()
    textrank = TextRank(mytokenizer)
    return textrank.summarize(text, 3, verbose=False)


# if verbose = False, it returns a list
# summaries: List[str] = textrank.summarize(text, 3, verbose=False)
# for summary in summaries:
#     print(summary)