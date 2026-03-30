# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        #loop through lists and compare values
        #put the smaller value into the list
        #put the leftover values in list at end
        dummy = ListNode()
        node = dummy

        while l1 and l2:
            if l1.val < l2.val:
                node.next = l1
                l1 = l1.next
            elif l2.val <= l1.val:
                node.next = l2
                l2 = l2.next
            node = node.next

        if l1:
            node.next = l1
        elif l2:
            node.next = l2
        
        return dummy.next