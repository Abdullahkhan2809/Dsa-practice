#Student management system using singly linked list

#node for a single student
class node:
    def __init__(self,ID, name, marks):
        self.id=ID
        self.name=name
        self.marks=marks
        self.next=None

class StudentManagement:
    def __init__(self):
        self.head=None

#insertion
    def addStudent(self, id ,Name, Mark):
        new_node=node(id, Name,Mark)
        if self.head is None:
            self.head=new_node
            return self.head
        #insert at the end
        last=self.head
        while last.next:
            last=last.next
        last.next=new_node
        return self.head
#delete Student
    def delete(self, student):
        temp=self.head
        prev=None
        if temp and (temp.name == student or temp.id == student):
            self.head = temp.next
            return
        while temp:
            if(temp.name == student or temp.id == student):
                prev.next=temp.next
                return
            prev=temp
            temp=temp.next
        print("Student not found for deletion")

#count the studentss
    def countStudents(self):
        counter=0
        temp=self.head
        while temp:
            counter=counter+1
            temp=temp.next
        return counter

#search Student 
    def SearchStudent(self,search):
        temp=self.head
        while temp:
            if temp.name == search or temp.id == search:
                print(f"ID: {temp.id}, Name: {temp.name}, Marks: {temp.marks}")
                return
            temp=temp.next
        print("Student not found")
#Display students
    def __str__(self):
        if not self.head:
            return "List is empty"
        result = []
        temp = self.head
        while temp:
            result.append(f"ID: {temp.id}, Name: {temp.name}, Marks: {temp.marks}")
            temp = temp.next
        return "\n".join(result)

if __name__ == "__main__":
    # Create the management system
    sms = StudentManagement()
    
    # Add student nodes
    sms.addStudent(101, "Alice", 85)
    sms.addStudent(102, "Bob", 92)
    sms.addStudent(103, "Charlie", 78)
    
    print(sms)
    print(sms.countStudents())
    sms.SearchStudent('Alice')
