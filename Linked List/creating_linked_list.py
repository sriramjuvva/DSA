class ListNode():
    def __init__(self,val,next=None):
        self.val = val
        self.next = None

n1 = ListNode(1)
n2 = ListNode(2)
n3 = ListNode(3)

n1.next = n2
n2.next = n3

head = n1

def inserting_new_head(head,value):
    new_head = ListNode(value)
    new_head.next = head
    return new_head
head = inserting_new_head(head,10)


def inserting_at_end(head,value):
    curr = head
    while curr.next:
        curr = curr.next
    last_node = ListNode(value)
    curr.next = last_node
    return head
head  = inserting_at_end(head,10)



def print_ll(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next

print(print_ll(head))


