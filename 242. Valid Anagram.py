class Solution(object):
    def isAnagram(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: bool
        """

        if len(s) != len(t):
            return False

        counter_dict = {}
        for char in s:
            if char in counter_dict:
                counter_dict[char] += 1
            else:
                counter_dict[char] = 1
        for char in t:
            if char in counter_dict:
                counter_dict[char] -= 1
                if counter_dict[char] < 0:
                    return False
            else:
                return False

        return True


if __name__=="__main__":
    s = Solution()
    print(s.isAnagram("anagram", "nagaram"))  # True