

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
    
    def getLength(self):
        
        count=0
        head = self.head
        while head is not None:
            count=count+1
            head= head.next
        return count
            
#traverse the String
    def __str__(self):
        ret_str='['
        temp=self.head

        while temp is not None:
            ret_str += str(temp.val)
            if temp.next:
                ret_str += ', '
            temp=temp.next
        
        ret_str=ret_str.rstrip(', ')
        ret_str +=']'
        return ret_str
    
list=linkedlist()
list.push(1)
list.push(3)
list.push(7)
print(list)
print(list.getLength())