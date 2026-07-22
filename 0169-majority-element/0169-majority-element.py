class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        d = {}
        max_len = 0
        result = None
        for num in nums:
            if num not in d:
                d[num] = 1
            else:
                d[num]+=1
        for key,value in d.items():
            if value > max_len:
                max_len = value
                result = key
        return result
        