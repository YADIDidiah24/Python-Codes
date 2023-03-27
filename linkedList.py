class Node:

    def __init__(self,data):
        self.data=data
        self.next=None
    def set_data(self, data):
        self.data = data
    # method for getting the data field of the node   
    def get_data(self):
        return self.data
      # method for setting the next field of the node
    def set_next(self, next):
        self.next = next
       # method for getting the next field of the node    
    def get_next(self):
        return self.next
    # returns true if the node points to another node
    def has_next(self):
            return self.next != None
    
class LinkedList(object):
    def __init__(self):
        self.length = 0
        self.head = None
    def addNode(self, node):
        if self.length == 0:
            self.addBeg(node)
        else:
            self.addLast(node)
    def addBeg(self, node):
        new = node
        new.next=self.head
        self.head=new
        self.length+=1
    def addLast(self, node):

        current =self.head
        while current.next != None:
            current=current.next
        new=node
        new.next=None

        current.next=new
        self.length += self.length
    def addAfterValue(self, data, node): 
        new = node
        current = self.head

        while current.next != None or current.data!=data:
            if current.data == data:
                new.next = current.next
                current.next = new
                self.length +=1
                return 
            else:
                current=current.next
        print("value not found!!!")

    def addAtPos(self, pos, node):
        count = 0
        currentnode = self.head
        previousnode = self.head

        if pos > self.length or pos < 0:
            print("does not EXIST!!!")
        else:
            while currentnode.next != None or count < pos:
                count = count + 1
                if count == pos:
                    previousnode.next = node
                    node.next=currentnode
                    self.length+=1
                    return
                else:
                    previousnode=currentnode
                    currentnode.next=currentnode
            print("value not found")

    def print_list(self):
        lis = []
        current = self.head

        while current !=None:
            lis.append(current.data)
            current=current.next

        print(lis)
    def deleteBeg(self):
        if self.length==0:
            print("no values present")

        else:
            self.head = self.head.next
            self.length-=1
    def deleteLast(self):
        if self.length == 0:
            print("The list is empty")
        else:
            current = self.head
            previous = self.head
        
            while current.next!=None:
                previous=current
                current=current.next
            previous.next=None
            self.length-=1

    def deleteValue(self, data):
        currentnode = self.head
        previousnode = self.head
        while currentnode.next != None or currentnode.data != data:
            if currentnode.data == data:
                previousnode.next = currentnode.next
                self.length -= 1
                return
            else:
                previousnode=currentnode
                currentnode=currentnode.next
            print("daata noooot present.....")
    def deleteAtPos(self, pos):
        count = 0
        currentnode = self.head
        previousnode = self.head
 
        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        # to deletle the first position of the linkedlist
        elif pos == 1:
            self.delete_beg()
            self.length -= 1
        else:        
            while currentnode.next != None or count < pos:
                if count ==pos:
                    previousnode.next=currentnode.next
                    self.length -= 1
                    return
                else:
                    previousnode=currentnode
                    currentnode=currentnode.next
            print("daata noooot present.....")
    def getLength(self):
        return self.length
    
    def getFirst(self):
        if self.length ==0:
            print("no value")
        else:
            return self.head.data
    def getLast(self):
        if self.length ==0:
            print("no value")
        else:
            current= self.head
            while current.next!=None:
                current=current.next

            return current.data
        
    def getAtPos(self, pos):
        
        if pos > self.length or pos < 0:
            print("The position does not exist. Please enter a valid position")
        else:
            current=self.head
            count=0
            while current.next!=None or count<pos:
                count+=1
                if count==pos:
                    return current.data
                else:
                    current=current.next
            print("data not founddddddd.")

            
    def hasNext(self,n):
        if n.next == None:
            return False
        return True
    def Next(self,n):

        return n.next.data
    
    def transfer(self,list1):

        current = list1.head.data
        while current !=None:
            self.addNode(current)
            current = current.next




a1 = Node(1)
a2 = Node(2)
a3 = Node(3)

l1=LinkedList()

l1.addNode(a1)
l1.addNode(a2)
l1.addNode(a3)

l2 =LinkedList()
#l2.transfer(l1)
#l2.print_list()
print(l1.head.data)
print(l2.length)