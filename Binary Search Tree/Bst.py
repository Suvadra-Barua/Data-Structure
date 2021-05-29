class BstNode:
    def __init__(self,data=None):
        self.data=data
        self.leftNode=None
        self.rightNode=None

class BST:
    def __init__(self):
        self.root=None
        self.list=[] #for levelorder
    def insertNode(self,root,data):
        if(root is None):
            root=BstNode(data)
            self.root=root #just to see which is working
            print(f'selfroot {self.root}') # print selfroot
        elif(root.data>=data):
            root.leftNode=self.insertNode(root.leftNode,data)
        else:
            root.rightNode=self.insertNode(root.rightNode,data)
        return root
    
    def searchNode(self,root,data):
         if(root is None):
              print(f'Not Found')
         elif(root.data==data):
              print(f'Yes, This is the address {root} of {root.data}') #print the searched address and data 
         elif(root.data>data):
              self.searchNode(root.leftNode,data)
         else:
              self.searchNode(root.rightNode,data)
    
#DFS         
    def inorderNode(self,root):
        if root:
            self.inorderNode(root.leftNode)
            print(root.data)
            self.inorderNode(root.rightNode)
            
    def preorderNode(self,root):
        if root:
            print(root.data)
            self.preorderNode(root.leftNode)
            self.preorderNode(root.rightNode)
            
    def postorderNode(self,root):
        if root:
            self.postorderNode(root.leftNode)
            self.postorderNode(root.rightNode)
            print(root.data)
            
#BFS
    def levelorderNode(self,root):
        self.list.append(root) #append the main root 15
        while self.list: #loop until the list queue doesn't get empty
            if(root.leftNode): #if leftnode is not null then append
                self.list.append(root.leftNode)
            if(root.rightNode): #if rightnode not null then append
                self.list.append(root.rightNode)
            print(root.data) #print 1st element's of the list data
            self.list.pop(0) #pop it
            if len(self.list)!=0: #if list is not empty then make the 1st element , root
                root=self.list[0]
                
    def findMin(self,root):
        minimum=root.data
        minNode=root
        while root:
            if(root.leftNode is None):
                if root.data<minimum:
                     minimum=root.data
                     minNode=root
                root=root.rightNode
            else:
                if root.data<minimum:
                     minimum=root.data
                     minNode=root
                root=root.leftNode
        return minNode
         
            
    def deleteNode(self,root,data):
        if root is None:
            return root
        elif root.data>data:
            root.leftNode=self.deleteNode(root.leftNode,data)
        elif root.data<data:
            root.rightNode=self.deleteNode(root.rightNode,data)
        else:
            if(root.leftNode is None and root.rightNode is None): # leaf node
                root=None
            elif(root.rightNode is None): # have only left child
                temp=root #take the desired value,root as temp
                root=root.leftNode #assign the leftchild to the root
                temp=None # empty the root 
            elif(root.leftNode is None): # have only right child
                temp=root #take the desired value,root as temp
                root=root.rightNode #assign the leftchild to the root
                temp=None # empty the root 
            else: #have left and right child both
                temp=self.findMin(root.rightNode) # finding minimum from rightportion
                root.data=temp.data #set the root data to minimum number
                self.deleteNode(root.rightNode,temp.data) #deleting the number from the right portion
        return root
                
                
                
                
            
            
bst1=BST()
root=None
root=bst1.insertNode(root,15)
print(f'{root.data} {root.leftNode} {root.rightNode}')
root=bst1.insertNode(root,10)
print(f'{root.data} {root.leftNode} {root.rightNode}')
#root=bst1.insertNode(root,20)
#print(f'{root.data} {root.leftNode} {root.rightNode}')
root=bst1.insertNode(root,20)
print(f'{root.data} {root.leftNode} {root.rightNode}')
root=bst1.insertNode(root,19)
print(f'{root.data} {root.leftNode} {root.rightNode}')

bst1.searchNode(root,20) #to search 10
bst1.searchNode(root,25) #search 25

print(f'Inorder')
bst1.inorderNode(root)
print(f'Preorder')
bst1.preorderNode(root)
print(f'postorder')
bst1.postorderNode(root)
print(f'levelorder')
bst1.levelorderNode(root)
print(f'Delete Node')
bst1.deleteNode(root,15)
print(f'After deletion levelorder')
bst1.levelorderNode(root)