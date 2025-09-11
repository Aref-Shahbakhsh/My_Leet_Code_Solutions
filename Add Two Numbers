# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: Optional[ListNode]
        :type l2: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        first_number = ''
        second_number = ''
        l1_list = []
        l2_list = []

        while True:
            if l1.next !=None:
                l1_list.append(int(l1.val))
                l1 = l1.next
            else:
                l1_list.append(int(l1.val))
                break

        while True:
            if l2.next !=None:
                l2_list.append(int(l2.val))
                l2 = l2.next
            else :
                l2_list.append(int(l2.val))
                break

        for node in range(len(l1_list),0,-1):
            first_number = first_number + str(l1_list[node-1])
        for node in range(len(l2_list),0,-1):
           second_number= second_number + str(l2_list[node-1])


        sumention = str(int(first_number) + int(second_number))
        n = ListNode(val=0, next=None)
        for i in range(len(sumention)-1):
            n.val = int(sumention[i])
            temp = ListNode(val=0,next=None)
            temp.next = n
            n=temp
        n.val = int(sumention[-1])
        return n






            
        
