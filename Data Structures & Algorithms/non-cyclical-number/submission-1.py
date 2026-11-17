class Solution:
    def isHappy(self, n: int) -> bool:

        n_str = str(n)

        prev_n_str = set()

        while True:
            sum = 0
            for digit in n_str:
                sum += int(digit)**2
            if sum == 1: return True
            else: 
                n_str = str(sum)
                if sum in prev_n_str: 
                    return False
                prev_n_str.add(sum)
            print(sum)
