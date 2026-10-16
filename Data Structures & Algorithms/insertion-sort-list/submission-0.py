# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        ans = ListNode(head.val)
        head = head.next
        while not head == None:
            prev = None
            ptr = ans
            while not ptr == None:
                if ptr.val >= head.val:
                    ptr = ListNode(head.val, ptr)
                    if not prev == None:
                        prev.next = ptr
                    else:
                        ans = ptr
                    break
                else:
                    prev = ptr
                    ptr = ptr.next
            if ptr == None:
                prev.next = ListNode(head.val)
            head = head.next
        return ans