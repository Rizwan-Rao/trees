class BST:
    def __init__(self,key):
        self.key = key
        self.lchild = None
        self.rchild = None

    def insert(self,data):
        if self.key is None:
            self.key = data
            return
        if self.key == data:
            return    
        if self.key > data :
            if self.lchild:
                self.lchild.insert(data)
            else:
                self.lchild = BST(data)
        else:
            if self.rchild:
               self.rchild.insert(data)
            else:
                self.rchild = BST(data)


    def search(self,data):
        if self.key == data:
            print("Node is found")
            return
        if data < self.key :
            if self.lchild:
                self.lchild.search(data)
            else:
                print("Node is not found")
        else:
            if self.rchild:
                self.rchild.search(data)
            else:
                print("Node is not found")   


    def preorder(self):
        print(self.key , end = " ")
        if self.lchild:
            self.lchild.preorder()
        if self.rchild:
            self.rchild.preorder()    


    def inorder(self):
        if self.lchild:
            self.lchild.inorder()
        print(self.key , end = " ")
        if self.rchild:
            self.rchild.inorder()    

    def postorder(self):
        if self.lchild:
            self.lchild.postorder()
        if self.rchild:
            self.rchild.postorder()
        print(self.key , end = " ")

    def delete(self,data,curr):
        if self.key is None:
            print("Tree is Empty")
            return
        if data < self.key:
            if self.lchild:
                self.lchild = self.lchild.delete(data) 
            else:
                print("Given Node is not present in the tree")
        
        elif data > self.key :
            if self.rchild:
                self.rchild = self.rchild.delete(data)
            else:
                print("Given Node is not present in the tree") 

        else:  
            if self.lchild is None:
                temp = self.rchild
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None
                return temp                      #These 2 condition will 
            if self.rchild is None :              #delete the node which 
                temp = self.lchild                 #contains 0 or 1 nodes
                if data == curr:
                    self.key = temp.key
                    self.lchild = temp.lchild
                    self.rchild = temp.rchild
                    temp = None
                    return
                self = None                         
                return temp

            node = self.rchild
            while node.lchild:
                node = node.lchild
            self.key = node.key
            self.rchild = self.rchild.delete(node.key) 
        return self        

    def min_node(self):
        current = self
        while current.lchild:
            current = current.lchild
        print("node with smallest key is :",current.key)    

    def max_node(self):
        current = self
        while current.rchild:
            current = current.rchild
        print("Node with largest key is :",current.key)        


# def count(node):
#     if node is None:
#         return 0
#     return 1+count(node.lchild) + count(node.rchild)

root = BST(10) 
list1 = [6,3,1,7,98,100]
for i in list1:
    root.insert(i)
# print(count(root))    
print("preorder")    
root.preorder()
root.min_node()
root.max_node()
# if count(root)>1:
#     root.delete(10,root.key)
# else:
#     print("\ncant perform deletion operation")    
# print("\ntree after deletion")
# root.preorder()

# print()
# print("\ninorder")
# root.inorder()
# print("\npostorder")
# root.postorder()

# root.search(60)    
# print(root.key)
# print(root.lchild)
# print(root.rchild)

# root.lchild = BST(5)
# print(root.lchild.key)
# print(root.lchild.lchild)
# print(root.lchild.rchild)
