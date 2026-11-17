class Solution:
    def isHappy(self, n: int) -> bool:


        prev_n_str = set()

        while True:
            sum = 0
            while n > 0:
                digit = n % 10
                sum += digit**2
                n //=10
           
            if sum == 1: return True
            else: 
                if sum in prev_n_str: 
                    return False
                prev_n_str.add(sum)
            n = sum
