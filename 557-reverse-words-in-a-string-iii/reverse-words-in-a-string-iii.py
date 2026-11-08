class Solution:
    def reverseWords(self, s: str) -> str:
        s=s.split()
        m=[]
        for i  in range(len(s)):
            m.append(s[i][::-1])
        return " ".join(m)

        