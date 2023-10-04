from typing import List

def twoSum(nums: List[int], target: int) -> List[int]:    
    res = []
    i = 0
    while True:
        tmp = target

        a = i

        while a <= len(nums)-1:
            tmp -= nums[a]
            if tmp == 0:     
                res.append(i)
                res.append(a)
                break
  
            a +=1

        if len(res) != 0:
            break
    
        i = i+1
    return res




