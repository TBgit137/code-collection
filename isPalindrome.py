class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        for char in [' ', ',', '.', '!', '?', ';', ':', '-', '_', '(', ')', '[', ']', '{', '}', '\"', '\'', '@', '#', '$', '%', '^', '&', '*', '\\']:
            s = s.replace(char, '')

        s_list = list(s)

        for i in range(0, len(s_list) // 2):
            if s_list[i] == s_list[-i - 1]:
                continue
            else:
                return False
        return True
