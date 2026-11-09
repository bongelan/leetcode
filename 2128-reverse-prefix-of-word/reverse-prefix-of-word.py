class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        w=word.find(ch)
        for i in word:
            if i==ch:
                m=word[:w+1]
                return m[::-1]+word[w+1:]
        return word
                

        