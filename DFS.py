# DFS Traversal code
class Node:
    def __init__(self,value):
        self.value=value
        self.children=[]
def dfs(root):
    if not root:
        return
    print(root.value,end=" ")

    for child in root.children:
        dfs(child)


#Create Nodes
A=Node('A')
B=Node('B')
C=Node('C')
D=Node('D')
E=Node('E')
F=Node('F')
G=Node('G')
H=Node('H')

#Build Tree
A.children = [B,C,D]
B.children = [E,F]
C.children = [G]
D.children = [H]
