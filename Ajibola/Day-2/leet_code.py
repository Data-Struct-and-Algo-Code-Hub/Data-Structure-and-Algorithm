class Solution:
    def hasCycle(self, head):
        next_next = head
        one_next = head

        while one_next and next_next and next_next.next:
            #pointer to the next two 
            next_next = next_next.next.next
            one_next = one_next.next 

            if one_next == next_next:
                return True

        return False