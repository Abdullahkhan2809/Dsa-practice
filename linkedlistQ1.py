

#node
class node:
    def __init__(self, value=None):
        self.val=value
        self.next=None 
# singly linked list 
class linkedlist:
    def __init__(self):
        self.head=None

    def push(self,val):
        new_node=node(val)

        #insert at the head
        if self.head is None:
            self.head=new_node
            return self.head
        #insert in the last 
        last = self.head
        while last.next is not None:
            last=last.next
        last.next = new_node
        return self.head
#find the lenght of hte linked list
    def getLength(self):
        
        count=0
        head = self.head
        while head is not None:
            count=count+1
            head= head.next
        return count
            
    
#start from the middle node
    def middleNode(self):
        """
        :type head: Optional[ListNode]
        :rtype: Optional[ListNode]
        """
        count =self.getLength()
        
        middle=count//2
        current = self.head
        i=0
        while i<middle:
            current=current.next
            i+=1
        return current

        
#traverse the String
    def __str__(self):
        ret_str='['
        temp=self.head

        while temp is not None:
            ret_str += str(temp.val)
            if temp.next:
                ret_str += ', '
            temp=temp.next
        
        ret_str = ret_str.rstrip(', ')
        ret_str += ']'
        return ret_str

my_list = linkedlist()
my_list.push(1)
my_list.push(3)
my_list.push(7)
print(my_list)
print(my_list.getLength())
middle = my_list.middleNode()
print(middle.val if middle else None)
