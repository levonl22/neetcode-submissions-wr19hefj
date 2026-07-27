class Solution:
    def isHappy(self, n: int) -> bool:
        seen = set()
        
        while n != 1:
            if n in seen:
                return False
            
            seen.add(n)

            curr_sum = 0
            for i in str(n):
                curr_sum += int(i) ** 2
            
            n = curr_sum
        
        return True