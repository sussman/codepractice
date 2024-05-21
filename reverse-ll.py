#!/usr/bin/env python

class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


def reverse_list(head: ListNode) -> ListNode:
    prev = None
    curr = head
    while curr:
        next_node = curr.next  # Store the next node
        curr.next = prev       # Reverse the current node's pointer
        prev = curr            # Move prev and curr one step forward
        curr = next_node
    return prev  # New head of the reversed list
