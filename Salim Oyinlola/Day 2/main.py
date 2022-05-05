class Solution:
    def hasCycle(self, head):
        swift = head
        slow = head
        while slow and swift and swift.next :
            swift = swift.next.next
            slow = slow.next
            if swift == slow:
                return True
        return False
