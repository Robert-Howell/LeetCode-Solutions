def findKthPositive(self, arr: List[int], k: int) -> int:

  arr_set = set(arr)
  count = k

  for i in range(1, 10000):
      if i not in arr_set:
          if count == 1:
              return i
          else:
              count -= 1
      else:
          continue
