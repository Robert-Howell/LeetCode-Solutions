def isPalindrome(self, x: int) -> bool:
  new_x = str(x)
  return new_x == new_x[::-1]

