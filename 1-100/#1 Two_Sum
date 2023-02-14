def twoSum(self, nums: List[int], target: int) -> List[int]:
  hashdict = {} # value, index

  for index,num in enumerate(nums):
    diff = target - num
    if diff in hashdict:
      return [hashdict[diff], num]
    hashdict[num] = index
    
  return 
