class Solution(object):
    def isValid(self, word):
        """
        :type word: str
        :rtype: bool
        """
        vowels="aeiouAEIOU"
        alpha_left=65
        alpha_right=122
        numbers="0123456789"
        is_minimum=False
        is_alpha=False
        is_vowel=False
        is_consonent=False
        if(len(word)<3):
            return False
        else:
            is_minimum=True
        for i in word:
            if((alpha_left<=ord(i)<=alpha_right) or (i in numbers)):
                is_alpha=True
                if(i in vowels):
                    is_vowel=True
                elif((i not in vowels) and (i not in numbers)):
                    is_consonent=True
            else:
                return False
        if(is_vowel and is_consonent and is_minimum and is_alpha):
            return True
        return False
        
# Example usage
if __name__ == "__main__":
    solution = Solution()
    print(solution.isValid("UuE6"))  # True