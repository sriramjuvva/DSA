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

def inserting_new_head_at_brgining(head,value):
    new_head = ListNode(value)
    new_head.next = head
    return new_head
head = inserting_new_head_at_brgining(head,10)


def inserting_at_end(head,value):
    curr = head
    while curr.next:
        curr = curr.next
    last_node = ListNode(value)
    curr.next = last_node
    return head
head  = inserting_at_end(head,10)

def inserting_at_position(head,positon,value):
    if positon == 1:
        new_node = ListNode(value)
        new_node.next = head
        return new_node
    curr = head
    count = 1
    while count < positon-1 and curr:
        curr = curr.next 
        count += 1
    new_node = ListNode(value)
    new_node.next = curr.next
    curr.next =new_node
    return head
head  = inserting_at_position(head,4,10)


def print_ll(head):
    cur = head
    while cur:
        print(cur.val, end=" -> ")
        cur = cur.next

print(print_ll(head))


# deleting the head
def deleting_the_head(head):
    if head is None:
        return None
    return head.next
head = deleting_the_head(head)

#deleting the last_node
def deleting_at_the_end(head):
    if head is None or head.next is None:
        return head
    curr = head
    while curr.next.next:
        curr = curr.next
    curr.next =None
    return head
head = deleting_at_the_end(head)


#deleting node at specific postion
def deleting_node_at_specific_position(head,positon):
    if head is None:
        return None
    if positon == 1:
        return head.next
    curr = head
    count = 1
    while count < positon-1 and curr.next:
        curr = curr.next
        count += 1
    if curr.next is None:
        return head
    curr.next = curr.next.next
    return head
head = deleting_node_at_specific_position(head,2)



#printing the list after deletion in ll
def print_del(head):
    curr = head
    while curr:
        print(curr.val,end="-->")
        curr= curr.next
print(print_del(head))






