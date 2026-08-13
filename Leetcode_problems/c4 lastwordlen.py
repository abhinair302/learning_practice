class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        word_list=s.split()
        last_word_len=len(word_list[-1])
        return last_word_len

sol=Solution()
print(sol.lengthOfLastWord("Hello World"))