def strStr(self, haystack: str, needle: str) -> int:
  if haystack.count(needle) == 0:
      return -1
  else:
      return haystack.index(needle)
