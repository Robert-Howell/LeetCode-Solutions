def isPalindrome(self, head: Optional[ListNode]) -> bool:
  curr = head
  list1 = []

  while curr:
      list1.append(str(curr.val))
      curr = curr.next


  str_list = "".join(list1)

  return str_list == str_list[::-1]
