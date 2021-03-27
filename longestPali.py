class Solution:
    def longestPalindrome(self, s: str) -> int:
        bucket = set()
        paliLength = 0
        for c in s:
            if c in bucket:
                bucket.remove(c)
                paliLength += 2
            else:
                bucket.add(c)
                
        if len(bucket) > 0:
            paliLength += 1
            
        return paliLength
