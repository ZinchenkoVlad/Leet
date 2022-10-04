# work only in leetcode

def middleNode(head:ListNode):
    slow = fast = head
        
    while fast and fast.next:
        
        slow = slow.next
        fast = fast.next.next
    
    return slow
    


def main():
    print(middleNode([1,2,3,4,5]))


if __name__ == "__main__":
    main()
