class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:


        # sol1: product of nums/ nums[i] but cant use division

        # #sol 2: loop twice but we are doing dup *, for res[0], we do 2*4 and same again gor res[3]
        # res = [1 for _ in range(len(nums))]
        # for i in range(len(nums)):
        #     for j in range(len(nums)):
        #         if  i == j: 
        #             pass
        #         else: 
        #             res[i] *= nums[j]

        # return res

        #sol 3: save repeated work by looping for pre and post products
        res = [1]* len(nums) 

        pre = 1
        for i in range(len(nums)):
            res[i] = pre
            pre *= nums[i]

        pos= 1
        for i in range(len(nums) -1, -1, -1):
            res[i] *=pos
            pos *= nums[i]

        return res







        


    