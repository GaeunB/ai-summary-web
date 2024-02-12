from typing import List
from konlpy.tag import Okt
from textrankr import TextRank

class OktTokenizer:
    okt: Okt = Okt()

    def __call__(self, text: str) -> List[str]:
        tokens: List[str] = self.okt.phrases(text)
        return tokens

def textrank_summarize(text: str, num_sentences: int, verbose: bool = True) -> str:
    mytokenizer: OktTokenizer = OktTokenizer()
    textrank: TextRank = TextRank(mytokenizer)
    summarized: str = textrank.summarize(text, num_sentences, verbose)
    return summarized

# if verbose = False, it returns a list
# summaries: List[str] = textrank.summarize(text, 3, verbose=False)
# for summary in summaries:
#     print(summary)